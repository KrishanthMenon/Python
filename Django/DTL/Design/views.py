from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    #return HttpResponse("<h1> Welcome </h1>")
    return render(request, 'home.html', {'name':'Tom'})

def add(request):
    value_1 = int(request.POST['number 1'])
    value_2 = int(request.POST['number 2'])
    res = value_1+value_2
    return render(request,'result.html',{'result':res})
