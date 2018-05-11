import datetime
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


def generate_enrollment():
    now = datetime.datetime.now()
    year = str(abs(now.year) % 100)

    users = DefaultUser.objects.all()
    if not users:
        return (year + "0000")

    sorted_users = sorted(users, key=lambda user: user.enrollment, reverse=True)

    id = int(sorted_users[0].enrollment[2:])
    id = id+1

    return (year + str(id).zfill(4))


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('e-mail', unique=True)
    first_name = models.CharField('Nome', max_length=40, blank=False)
    last_name = models.CharField('Sobrenome', max_length=80, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'Conta de Usuário'
        verbose_name_plural = 'Contas de Usuário'

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


    def __str__(self):
        return self.email


class DefaultUser(Account):
    enrollment = models.CharField('Matrícula', max_length=10, unique=True, default=generate_enrollment)
    
    cpf = models.CharField('CPF', max_length=11, validators=[MinLengthValidator(11)], blank=False)
    rg = models.CharField('RG', max_length=20, blank=False)
    date_birth = models.DateField('Data de Nascimento', blank=False)
    phone_number = models.CharField('Número de Telefone', max_length=15, blank=False)
    picture = models.ImageField('Foto de Perfil', upload_to='images/users/', default='images/users/default.png')

    class Meta:
        verbose_name = 'Usuário Base'
        verbose_name_plural = 'Usuários Base'

    def __str__(self):
        return self.get_full_name()


class Student(DefaultUser):
    is_member = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


class Member(DefaultUser):
    entrance_date = models.DateField('Data de Ingresso no Projeto', blank=False)
    course = models.CharField('Curso', max_length=20)
    semester = models.CharField('Semestre', max_length=20)
    college_enrollment = models.CharField('Matricula', max_length=10)
    is_member = models.BooleanField(default=True)    

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'

    def get_json(self):
        return {
            'enrollment': self.enrollment, 
            'email': self.email,
            'name': self.first_name + self.last_name,
            'course': self.course,
            'college_enrollment': self.college_enrollment,
        }


class Parent(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    email = models.EmailField('e-mail', unique=True)    
    first_name = models.CharField('Nome', max_length=40, blank=False)
    last_name = models.CharField('Sobrenome', max_length=80, blank=False)
    cpf = models.CharField('CPF', max_length=11, validators=[MinLengthValidator(11)], blank=False)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Dados do Responsável'