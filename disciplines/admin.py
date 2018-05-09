from django.contrib import admin
from .models import Discipline, DisciplineFront


class DisciplineFrontInline(admin.StackedInline):
    model = DisciplineFront

    fk_name = 'containing_discipline'
    
    fields = (
        'name',
    )

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    fieldsets = (
        'Disciplina', {
            'fields': (
                'name',
            ),
        },
    ),

    inlines = [
        DisciplineFrontInline,
    ]