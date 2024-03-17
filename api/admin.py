from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'auth_provider', 'is_verified']
admin.site.register(User, UserAdmin)