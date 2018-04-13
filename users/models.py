import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinLengthValidator

def generate_enrollment():
    now = datetime.datetime.now()
    year = str(abs(now.year) % 100)

    users = get_user_model().objects.all()
    if not users:
        return (year + "0000")

    sorted_users = sorted(users, key=lambda user: user.enrollment, reverse=True)

    id = int(sorted_users[0].enrollment[2:])
    id = id+1

    return (year + str(id).zfill(4))

class User(AbstractBaseUser):
    enrollment = models.CharField('Matrícula', max_length=10, primary_key=True, default = generate_enrollment)
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)], blank=False)
    rg = models.CharField(max_length=20, blank=False)
    date_birth = models.DateField(blank=False)
    phone_number = models.IntegerField(blank=False)
    picture = models.ImageField(upload_to='images/', default='images/default.svg')

    USERNAME_FIELD = enrollment
    REQUIRED_FIELDS = [first_name, email]

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

