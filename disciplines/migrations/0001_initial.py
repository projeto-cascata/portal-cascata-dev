# Generated by Django 2.0.4 on 2018-05-13 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplineComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uploaded_file', models.FileField(upload_to='materials/')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('disciplinecomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disciplines.DisciplineComponent')),
                ('cover', models.ImageField(default='images/disciplineCover/default.png', upload_to='images/disciplineCover/', verbose_name='Foto de Capa')),
            ],
            options={
                'verbose_name': 'Disciplina',
            },
            bases=('disciplines.disciplinecomponent',),
        ),
        migrations.CreateModel(
            name='DisciplineFront',
            fields=[
                ('disciplinecomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disciplines.DisciplineComponent')),
                ('containing_discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplines.Discipline')),
            ],
            options={
                'verbose_name': 'Frente',
            },
            bases=('disciplines.disciplinecomponent',),
        ),
        migrations.AddField(
            model_name='material',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disciplines.DisciplineComponent'),
        ),
    ]
