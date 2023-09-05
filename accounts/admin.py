from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
# Register your models here.


admin.site.unregister(Group)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'telephone']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('telephone',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('telephone',)}),)
    


admin.site.register(CustomUser, CustomUserAdmin)