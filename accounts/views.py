from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.

def login_View(request):
    return render(request, 'accounts/login.html')

# def logout_View(request):
#     return render(request, 'accounts/logout.html')

def signup_View(request):
    return render(request, 'accounts/signup.html')