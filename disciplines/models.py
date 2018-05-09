from django.db import models

# Create your models here.

class DisciplineComponent(models.Model):
    name = models.CharField(max_length=50, blank=False)

class Discipline(DisciplineComponent):
    class Meta:
        verbose_name = 'Disciplina'

class DisciplineFront(DisciplineComponent):
    containing_discipline = models.ForeignKey(to=Discipline, on_delete=models.CASCADE)

class Material(models.Model):
    name = models.CharField(max_length=200, blank=False)
    uploaded_file = models.FileField(upload_to='materials/')
    discipline = models.ForeignKey(to=DisciplineComponent, on_delete=models.CASCADE)
    