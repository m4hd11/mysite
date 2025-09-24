from django.urls import path, re_path
from website.views import *

app_name= 'website'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('newsletter', newsletter_view, name='newsletter'),
    re_path(r'^.*$', coming_soon_view, name='coming_soon'),
    # path('test', test_view, name='test')
]