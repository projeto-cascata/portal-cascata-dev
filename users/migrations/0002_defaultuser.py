# Generated by Django 2.0.4 on 2018-04-15 00:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultUser',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('enrollment', models.CharField(default=users.models.generate_enrollment, max_length=10, unique=True, verbose_name='Matrícula')),
                ('cpf', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='CPF')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('date_birth', models.DateField(verbose_name='Data de Nascimento')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Número de Telefone')),
                ('picture', models.ImageField(default='images/default.svg', upload_to='images/', verbose_name='Foto de Perfil')),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
            },
            bases=('users.account',),
            managers=[
                ('objects', users.models.AccountManager()),
            ],
        ),
    ]