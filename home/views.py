from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Occations
from .forms import BookingForm

# Create your views here.
def index(request):
   
   return render(request,'index.html')

def ABOUT(request):
    return render(request,'about.html')

def BOOKING(request):
    if request.method == "POST":
        form= BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def OCCATIONS(request):
    dict_occ={
        'occations': Occations.objects.all()
    }
    return render(request,'occations.html',dict_occ) 

def CONTACT(request):
    return render(request,'contact.html')

def DEPARTMENT(request):
    dict_dept={
        'dept':Departments.objects.all}
    return render(request,'department.html',dict_dept)