# Generated by Django 5.2.1 on 2025-05-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('professor', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='cursos/')),
            ],
        ),
    ]
