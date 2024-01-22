from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demo(request):
    return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")

def staff(request):
    return render(request,"staffs.html")

def events(request):
    return render(request,"events.html")