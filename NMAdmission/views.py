from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    if request.method=="POST":
        student = Student()
        student.sid = request.POST.get('id')
        student.name = request.POST.get('name')
        student.save()
        return HttpResponseRedirect(reverse(home))
    return render(request,'home.html')
