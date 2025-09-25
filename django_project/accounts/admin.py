from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# ...existing code...
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'name', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name',)}),
    )
    search_fields = ('email', 'username', 'name')

# Register the admin class with the model
admin.site.register(CustomUser, CustomUserAdmin)