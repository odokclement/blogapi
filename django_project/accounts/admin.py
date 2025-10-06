from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'name', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )
    
    # Replace the += with a complete redefinition
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'name', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('email', 'username', 'name')

admin.site.register(CustomUser, CustomUserAdmin)