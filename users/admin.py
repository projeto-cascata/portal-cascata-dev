from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserData, Student

class UserDataInline(admin.StackedInline):
    model = UserData
    can_delete = False
    verbose_name_plural = "Dados Pessoais"

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Geral', {
            'fields': ('username', 'password', 'email', 'first_name', 'last_name')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')
        })
    )
    inlines = (UserDataInline, )

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

