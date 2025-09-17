from django.contrib import admin
from accounts.models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')

admin.site.register(Profile)
