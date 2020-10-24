from django.db import models
# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitulo = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name="Contenido")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de Edicion")
    class Meta:
        db_table = 'Servicio'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']
    def __str__ (self):
        return self.title
