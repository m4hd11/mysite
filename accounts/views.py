from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def login_View(request):
    if request.user.is_authenticated:
        return redirect('/')

    next_url = request.POST.get('next') or request.GET.get('next') or '/'

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    context = {'form': form, 'next': next_url}
    return render(request, 'accounts/login.html', context)
    
@login_required
def logout_View(request):
    logout(request)
    return redirect('/')

def signup_View(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:login'))
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')