from django.contrib import admin
from users.models import Account, DefaultUser

# Register your models here.
admin.site.register(Account)
admin.site.register(DefaultUser)
