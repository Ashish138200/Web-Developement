from django.shortcuts import render

def index(request):
    contextDict = {'text':'hello world','number':100}
    return render(request,'basicapp/index.html',contextDict)

def other(request):
    return render(request,'basicapp/other.html')

def relative(request):
    return render(request,'basicapp/relativeURL.html')