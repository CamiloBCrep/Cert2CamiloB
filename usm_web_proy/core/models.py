from django.db import models

class nuevo_proyecto(models.Model):
    estudiante=models.TextField(max_length=50)
    profesor=models.TextField(max_length=50, null=True)
    proy=models.TextField(max_length=255)
    tema=models.TextField(max_length=50)

# Create your models here.
