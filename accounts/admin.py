from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'is_staff']
    list_filter = ['email', 'username', 'name', 'is_staff']
    # cac truong khi edit user???
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('name',)}),)
    # cac truong khi add user
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('name',)}),)
    # cac truong khi tim kiem user
    search_fields = ['email', 'username', 'name']
    # cac truong khi sap xep user
    ordering = ['email']
    
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
