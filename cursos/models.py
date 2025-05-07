from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    professor = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='cursos/',blank=True , null=True)
    
    
    def __str__(self):
        return self.nome
    
