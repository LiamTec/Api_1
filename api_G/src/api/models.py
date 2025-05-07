from django.db import models

class Supervivientes(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.TextField()
    vida = models.IntegerField()
    image_url = models.URLField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Zombies(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.TextField()
    vida = models.IntegerField()
    habilidad_primaria = models.IntegerField()
    habilidad_secundaria = models.IntegerField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

class Gun(models.Model):
    name = models.CharField(max_length=30)
    balas = models.IntegerField()
    modelo = models.CharField(max_length=30)
    nivel = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30) 

    def __str__(self):
        return self.name
