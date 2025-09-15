from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_View, name='login'),
    path('logout/', views.logout_View, name='logout'),
    path('signup/', views.signup_View, name='signup'),
]