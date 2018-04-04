from django.db import models
import datetime


class User(models.Model):
    enrollment = models.models.IntegerField(primary_key=True, default = generate_enrollment)



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