from django.shortcuts import render
from django.http import HttpResponse
from firstApp.models import Topic,WebPage,AccessRecord

def index(request):
    webpageList = AccessRecord.objects.order_by('date')
    dateDict = {'access_records':webpageList}
    # return HttpResponse("Hello world")
    #myDict = {'insert_me':"Hello I'm from views.py from firstApp"}
    return render(request,'firstApp/index.html',context=dateDict)
