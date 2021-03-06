# Generated by Django 2.0.4 on 2018-05-13 14:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('first_name', models.CharField(max_length=40, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=80, verbose_name='Sobrenome')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Conta de Usuário',
                'verbose_name_plural': 'Contas de Usuário',
            },
            managers=[
                ('objects', users.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('first_name', models.CharField(max_length=40, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=80, verbose_name='Sobrenome')),
                ('cpf', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'Responsável',
                'verbose_name_plural': 'Dados do Responsável',
            },
        ),
        migrations.CreateModel(
            name='DefaultUser',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('enrollment', models.CharField(default=users.models.generate_enrollment, max_length=10, unique=True, verbose_name='Matrícula')),
                ('cpf', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='CPF')),
                ('rg', models.CharField(max_length=20, verbose_name='RG')),
                ('date_birth', models.DateField(verbose_name='Data de Nascimento')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Número de Telefone')),
                ('picture', models.ImageField(default='images/users/default.png', upload_to='images/users/', verbose_name='Foto de Perfil')),
            ],
            options={
                'verbose_name': 'Usuário Base',
                'verbose_name_plural': 'Usuários Base',
            },
            bases=('users.account',),
            managers=[
                ('objects', users.models.AccountManager()),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('defaultuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.DefaultUser')),
                ('entrance_date', models.DateField(verbose_name='Data de Ingresso no Projeto')),
                ('course', models.CharField(max_length=20, verbose_name='Curso')),
                ('semester', models.CharField(max_length=20, verbose_name='Semestre')),
                ('college_enrollment', models.CharField(max_length=10, verbose_name='Matricula')),
                ('is_member', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
            },
            bases=('users.defaultuser',),
            managers=[
                ('objects', users.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('defaultuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.DefaultUser')),
                ('is_member', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
            },
            bases=('users.defaultuser',),
            managers=[
                ('objects', users.models.AccountManager()),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Student'),
        ),
    ]
