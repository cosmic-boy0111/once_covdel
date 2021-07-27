from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1> Landing Page </h1>"
                        "<button><a class='nav-link' href='/customer'>Cust Login</a></button>"
                        "<button><a class='nav-link' href='/partner'>Part Login</a></button>"
                        "<button><a class='nav-link' href='/logistics'>Log Login</a></button>")
