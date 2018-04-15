from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Account, DefaultUser, Student, Parent

@admin.register(DefaultUser)
class DefaultUserAdmin(UserAdmin):
    readonly_fields: ('password')
    fieldsets = (
        ('Geral', {
            'fields': (
                'email',
                'password',
                'first_name',
                'last_name',
            )
        }),
        ('Dados Pesoais', {
            'fields': (
                'enrollment',
                'cpf',
                'rg',
                'date_birth',
                'phone_number',
                'picture',
            )
        }),
        ('Permissões', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )

    add_fieldsets = (
        ('Geral', {
            'classes': ('wide',),
            'fields': (
                'email', 
                'password1', 
                'password2',
                'first_name',
                'last_name'
            ),
        }),
        ('Dados Pesoais', {
            'fields': (
                'enrollment',
                'cpf',
                'rg',
                'date_birth',
                'phone_number',
                'picture',
            )
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

class ParentInline(admin.StackedInline):
    model = Parent
    fieldsets = (
        ('Dados do Responsável', {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'cpf',
            ),
        }),
    )

@admin.register(Student)
class StudentAdmin(DefaultUserAdmin):
    inlines = [
        ParentInline
    ]

