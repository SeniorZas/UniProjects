from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
#parent model
class forum(models.Model):
    name=models.CharField(max_length=200,default="Anónimo", verbose_name="Nombre" )
    email=models.CharField(max_length=200,null=True, verbose_name="E-mail")
    topic= models.CharField(max_length=300, verbose_name="Tema")
    description = models.TextField(max_length=1000,blank=True, verbose_name="Descripción")
    header_image = models.ImageField(default="", null=True, blank=True, upload_to="images/", verbose_name="Añadir Imagen (Opcional)")
    link = models.CharField(max_length=100, blank=True, null=True ,verbose_name="Link de referencia (Opcional)")
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)
        
        
#child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE, verbose_name="Foro")
    discuss = models.TextField(max_length=1000, verbose_name="Discusión")
    header_image2 = models.ImageField(default="", null=True, blank=True, upload_to="images/respuestas/", verbose_name="Añadir Imagen (Opcional)")
 
    def __str__(self):
        return str(self.forum)
