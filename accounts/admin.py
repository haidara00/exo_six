from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    list_display = ["username", "email", "is_staff"]
admin.site.register(CustomUser,CustomUserAdmin )