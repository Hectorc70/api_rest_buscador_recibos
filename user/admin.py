from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from user.forms import(
    CustomUserChangeForm,
    CustomUserCreationForm
)
# Register your models here.
from .models import NewUser

class CustomUserAdmin(UserAdmin):
    form     = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = UserAdmin.fieldsets+ (
        (
            None,{
            'fields':(
                'control',
                )
            }
        ),
    )


@admin.register(NewUser)
class UserAdmin(CustomUserAdmin):
    list_display=(
        'control',      
        'password',
        'is_staff',
        'is_active',
        'is_superuser',          
        'last_login',
        'date_joined'

    )