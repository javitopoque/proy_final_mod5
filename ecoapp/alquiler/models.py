from django.db import models

class Inquilino(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    ci = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    def __str__ (self):
        return self.nombre
        #return (self.nombre, self.apellido, self.ciudad, self.ci, self.created, self.update)

class AmbienteTipo(models.TextChoices):
    CUARTO = 'CUARTO', 'Cuarto'
    DEPARTAMENTO = 'DEPARTAMENTO', 'Departamento'
    MONOBLOCK = 'MONOBLOCK', 'Monoblock'
    DUPLEX = 'DUPLEX', 'Duplex'

class Ambiente(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()    
    tipo = models.CharField(
        max_length=20,
        choices = AmbienteTipo.choices,
        default = AmbienteTipo.CUARTO    
    )
    libre = models.BooleanField(blank = True, default = True)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.tipo

class AmbienteInquilino(models.Model):
    costo = models.DecimalField(decimal_places = 2, max_digits = 10)
    inquilino = models.ForeignKey(Inquilino, on_delete = models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete = models.CASCADE)
    ingreso = models.DateTimeField(auto_now_add = True)
    salida = models.DateTimeField(auto_now = True)

class Servicio(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre

class ServicioAmbiente(models.Model):
    activo = models.BooleanField(blank = True, default = True)
    ambiente = models.ForeignKey(Ambiente, on_delete = models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE)

    def __all__(self):
        return self
