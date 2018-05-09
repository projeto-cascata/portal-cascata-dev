# Generated by Django 2.0.4 on 2018-05-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplines', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disciplinefront',
            options={'verbose_name': 'Frente'},
        ),
        migrations.AddField(
            model_name='discipline',
            name='cover',
            field=models.ImageField(default='images/disciplineCover/default.png', upload_to='images/disciplineCover/', verbose_name='Foto de Capa'),
        ),
        migrations.AlterField(
            model_name='disciplinecomponent',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]