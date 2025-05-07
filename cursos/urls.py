from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('criar', views.criar_curso, name='criar_cursos'),
    path('curso/<int:curso_id>/', views.detalhes_curso, name='detalhes_curso'),
    path('curso/excluir/<int:curso_id>/', views.excluir_curso, name='excluir_curso'),
    ]