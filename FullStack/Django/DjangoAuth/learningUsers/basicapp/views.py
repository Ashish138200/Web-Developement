from django.shortcuts import render
from basicapp.forms import UserForm,UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html',{'index':index})

def register(request):
    registered = False # assuming that the user is not registered
    if request.method == "POST":
        # Grabbing the information from the form
        userForm = UserForm(data=request.POST)
        profileForm = UserProfileInfoForm(data=request.POST)
        # Checking if the forms are valid or not
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save() # saving the user form
            user.set_password(user.password) #hashing the password
            user.save() # saving the password in db
            profile = profileForm.save(commit=False) #commit=False because error will be occured for overwriting in db
            profile.user = user # One to one relationship
            # Checking for the profile picture
            if 'profilePic' in request.FILES:
                profile.profilePic = request.FILES['profilePic']
            profile.save() # Saving it in DB

            registered = True
        else:
            print(userForm.errors,profileForm.errors)
    else:
        # No request yet
        userForm = UserForm()
        profileForm = UserProfileInfoForm()
    return render(request,'basicapp/registration.html',{'userForm':userForm,
                                                        'profileForm':profileForm,
                                                        'registered':registered})

def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # auto authetication
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                # user login successfully if they pass authentication,is_active than they will be redirected to the index page
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Some tried to login and failed!")
            print("username: {} and password: {} ".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'basicapp/login.html',{})

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You're logged in, Nice!")