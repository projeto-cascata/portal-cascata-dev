from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserData

class UserDataInline(admin.StackedInline):
    model = UserData
    can_delete = False
    verbose_name_plural = "Dados Pessoais"

class UserAdmin(BaseUserAdmin):
    inlines = (UserDataInline, )

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

