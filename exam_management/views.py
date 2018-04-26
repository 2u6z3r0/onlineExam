from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
@login_required
def home_page(request):
    return HttpResponse("<h1> Home Page </h1>")
