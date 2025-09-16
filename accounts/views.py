from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

User = get_user_model()

def login_View(request):
    if request.user.is_authenticated:
        return redirect('/')

    next_url = request.POST.get('next') or request.GET.get('next') or '/'

    if request.method == "POST":
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            try:
                user_obj = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                user_obj = None

        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)
            if user:
                login(request, user)
                return redirect(next_url)

        context = {
            'form': AuthenticationForm(request=request),
            'error': 'Invalid Username/Email or Password',
            'next': next_url
        }
        return render(request, 'accounts/login.html', context)

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