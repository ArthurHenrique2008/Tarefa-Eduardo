from django.db import models

# Create your models here.
class Categorias(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

# Para Rodar
# python manage.py runserver runserver

# Criar os arquivos de migração com o banco de dados
# python manage.py  makemigrations oladjango

#  python manage.py  sqlmigrate oladjango 0001

# python manage.py shell

# Model, View configurar a URL
#Teste eeeeeeeeeeeeeeeeeeeeeeeeeeasdjflkjalsdfjlsajdlkfjl