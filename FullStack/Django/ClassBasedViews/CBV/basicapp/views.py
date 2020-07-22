from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

'''
#-------------------------------------------------Method views----------------------------------------------------------

def index(request):
    return render(request,'index.html')  
    
#-----------------------------------------------Class Based Views-------------------------------------------------------

class CBView(View):
    def get(self,request):
        return HttpResponse("Class based views are cool")
        
'''
#----------------------------------Template based views-----------------------------------------------------------------

class IndexViews(TemplateView):
    template_name = 'index.html'

    #OOP predefined method
    #kwargs: keyword arguments
    #**kwargs : will give you all kwargs except for those corresponding parameter as a dictionary. 
    #Dict don't have an order
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context


#------------------------------------------------ListView---------------------------------------------------------------
class SchoolListView(ListView):
    model = models.School
    '''This take the model i.e. School convert it into lowercase i.e. school and add _list to it and returns school_list
    If you don't wanna use the default context name you can change it:
    context_object_name = 'schools'
    '''
    #template_name = 'school_list.html'

#-----------------------------------------------DetailView--------------------------------------------------------------
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basicapp/school_details.html'
    # this returns just lower model name i.e. school

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('principal','name')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    #template_name = 'basicapp/school_confirm_delete.html'
    success_url = reverse_lazy("basicapp:list")