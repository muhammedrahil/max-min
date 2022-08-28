from django.shortcuts import render
from django.http import  JsonResponse
# Create your views here.
from products.models import *
from django.views.generic import ListView



def dashboard(request):
    return render(request,'admin_template/dashboard.html')


