from django.db import models
from django.utils import timezone
# Create your models here.


class Empleado(models.Model):
    no_control = models.CharField(primary_key=True, max_length=8,unique=True)
    nombre     = models.CharField('Nombre de Empleado', max_length=100)
    apellido_p = models.CharField('Apellido Paterno', max_length=100)
    apellido_m = models.CharField('Apellido Materno', max_length=100)


class Recibo(models.Model):
    id_recibo       = models.AutoField(primary_key=True, unique=True)
    nombre_archivo  = models.CharField('Nombre de Archivo', max_length=200)
    ruta_archivo    = models.CharField('Ruta de Archivo', max_length=500)
    periodo         = models.CharField('Periodo', max_length=6)
    tipo_nomina     = models.CharField('Tipo de Nomina', max_length=100)
    no_control      = models.ForeignKey(Empleado, null=False, blank=False, on_delete=models.CASCADE, related_name='recibos')


    def __str__(self):
        return '%d: %s'%(self.id_recibo, self.ruta_archivo)


