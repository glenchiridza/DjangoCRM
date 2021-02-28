from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

def home_page(request):
    # return HttpResponse("Hi glen")
    leads = Lead.objects.all()
    context ={
        "leads":leads
    }
    return render(request, 'secondpage.html',context)