from django.contrib import admin
from users.models import Account, DefaultUser, Student, Parent

class ParentInline(admin.StackedInline):
    model = Parent

class StudentAdmin(admin.ModelAdmin):
    inlines = [
        ParentInline
    ]

# Register your models here.
admin.site.register(Account)
admin.site.register(DefaultUser)
admin.site.register(Student, StudentAdmin)
