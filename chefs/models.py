from django.db import models


class Chef(models.Model):
    # Datos basicos
    nombre = models.CharField(verbose_name='Nombre', max_length=256)
    apellido = models.CharField(verbose_name='Apellido', max_length=256)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')

    # Informacion de contacto
    telefono = models.CharField(max_length=32, null=True, blank=True, verbose_name='Número de Teléfono/Celular')
    correo_electronico = models.CharField(max_length=128, null=True, blank=True, verbose_name='Correo Electrónico')

    # Adicional
    foto_perfil = models.ImageField(upload_to='avatares', null=True, blank=True, verbose_name='Imagen de perfil')
    descripcion =  models.TextField(verbose_name='Descripción')



class ImagenChef(models.Model):
    imagen = models.ImageField(upload_to='imagenes', verbose_name='Imagen')
    chef = models.ForeignKey('Chef', related_name='imagenes_chef', on_delete=models.CASCADE)
