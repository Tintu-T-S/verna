from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages, auth

from .forms import Personform 
from .models import Course, Person_profile

# Create your views here.

def Create_Person(request):
    form = Personform()
    if request.method == 'POST':
        form = Personform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Personapp:order_confirm')
    return render(request,"studdetails.html", {'form': form})

def Confirm(request):
    corn = Person_profile.objects.all()
    return render(request,"confirm.html",{'corn':corn})

def logout(request):
    auth.logout(request)
    return  redirect ('login')

# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdownlist_option.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)