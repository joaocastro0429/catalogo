from django.contrib import admin
from .models import Curso

@admin.register(Curso)

class cursoAdmin(admin.ModelAdmin):
    list_display=('nome','professor')
    search_fields = ['nome', 'professor']
