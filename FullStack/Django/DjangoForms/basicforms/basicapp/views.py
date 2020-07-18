from django.shortcuts import render
from . import forms

def index(request):
    return render(request,'basicapp/index.html')

def formNameView(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation success!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
    return render(request,'basicapp/FormPage.html',{'form':form})