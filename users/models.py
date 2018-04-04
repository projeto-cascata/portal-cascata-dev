from django.db import models
import datetime

def generate_enrollment():
    now = datetime.datetime.now()
    year = str(abs(now.year) % 100)

    users = Users.objects.all()
    if not users:
        return (year + "0000")

        users.sort(key=lambda user: user.enrollment, reverse=True)

        id = int(users[0].enrollment[2:])
        id = id+1

        return (year + str(id).zfill(4))

class User(models.Model):
    enrollment = models.CharField(max_length=10, primary_key=True, default = generate_enrollment)
    name = models.CharField(max_length=200, null=False, blank=False)
    cpf = models.IntegerField(blank=False)
    RG  = models.IntegerField(blank=False)
    date_birth = models.DateField(blank=False)
    number = models.IntegerField(blank=False)
    email = models.CharField(max_length=200, blank=False)
