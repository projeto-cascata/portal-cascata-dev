import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

def generate_enrollment():
    now = datetime.datetime.now()
    year = str(abs(now.year) % 100)

    users = UserData.objects.all()
    if not users:
        return (year + "0000")

    sorted_users = sorted(users, key=lambda user: user.enrollment, reverse=True)

    id = int(sorted_users[0].enrollment[2:])
    id = id+1

    return (year + str(id).zfill(4))

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    enrollment = models.CharField('Matrícula', max_length=10, primary_key=True, default = generate_enrollment)
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)], blank=False)
    rg = models.CharField(max_length=20, blank=False)
    date_birth = models.DateField(blank=False, null=False)
    phone_number = models.CharField(blank=False, max_length=15)
    picture = models.ImageField(upload_to='images/', default='images/default.svg')


