from django.db import models

class Asociado(models.Model):
    """"""
    name = models.CharField(max_length=100)
    cedula = models.IntegerField()
    edad = models.IntegerField()
    nivelEducativo = models.CharField(max_length=100)
    familiares = models.CharField(max_length=500)
    familiaresDetalles = models.CharField(max_length=500)
    
    personal1 = models.CharField(max_length=500)
    personal1Detalles = models.CharField(max_length=500)
    personal2 = models.CharField(max_length=500)
    personal3 = models.CharField(max_length=500)
    personal4 = models.CharField(max_length=500)
    
    familiares1 = models.CharField(max_length=500)
    familiares2 = models.CharField(max_length=500)
    familiares2Detalles = models.CharField(max_length=500)
    familiares3 = models.CharField(max_length=500)
    
    pesem1 = models.CharField(max_length=500)
    pesem2 = models.CharField(max_length=500)
    pesem3 = models.CharField(max_length=500)
    
    solidario1 = models.CharField(max_length=500)
    solidario2 = models.CharField(max_length=500)
    solidario3 = models.CharField(max_length=500)
    solidario4 = models.CharField(max_length=500)
    
    coovitel1 = models.CharField(max_length=500)
    coovitel2 = models.CharField(max_length=500)
    coovitel3 = models.CharField(max_length=500)
    coovitel3Detalles = models.CharField(max_length=500)
    coovitel4 = models.CharField(max_length=500)
    coovitel5 = models.CharField(max_length=500)
    coovitel6 = models.CharField(max_length=500)
    
    sugerencia1 = models.CharField(max_length=500)
    sugerencia2 = models.CharField(max_length=500)
    
    def __str__(self):
        return f"Registro asociado {self.name} - {self.cedula}"

class Colaborador(models.Model):
    """"""
    name = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    años = models.IntegerField()
    nivelEducativo = models.CharField(max_length=100)
    
    personal1 = models.CharField(max_length=500)
    personal1Detalles = models.CharField(max_length=500)
    personal2 = models.CharField(max_length=500)
    personal3 = models.CharField(max_length=500)
    personal4 = models.CharField(max_length=500)
    personal5 = models.CharField(max_length=500)
    personal6 = models.CharField(max_length=500)
    
    pesem1 = models.CharField(max_length=500)
    pesem2 = models.CharField(max_length=500)
    pesem3 = models.CharField(max_length=500)
    pesem4 = models.CharField(max_length=500)
    
    solidario1 = models.CharField(max_length=500)
    solidario2 = models.CharField(max_length=500)
    solidario3 = models.CharField(max_length=500)
    solidario4 = models.CharField(max_length=500)
    solidario5 = models.CharField(max_length=500)
    
    coovitel1 = models.CharField(max_length=500)
    coovitel2 = models.CharField(max_length=500)
    coovitel2Detalles = models.CharField(max_length=500)
    coovitel3 = models.CharField(max_length=500)
    coovitel4 = models.CharField(max_length=500)
    
    sugerencia1 = models.CharField(max_length=500)
    sugerencia2 = models.CharField(max_length=500)
    sugerencia3 = models.CharField(max_length=500)
    
    def __str__(self):
        return f"Registro asociado {self.name} - {self.cargo}"

class Dirigente(models.Model):
    name = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    años = models.IntegerField()
    nivelEducativo = models.CharField(max_length=100)
    
    personal1 = models.CharField(max_length=500)
    personal1Detalles = models.CharField(max_length=500)
    personal2 = models.CharField(max_length=500)
    personal3 = models.CharField(max_length=500)
    personal4 = models.CharField(max_length=500)
    personal5 = models.CharField(max_length=500)
    personal6 = models.CharField(max_length=500)
    
    pesem1 = models.CharField(max_length=500)
    pesem2 = models.CharField(max_length=500)
    pesem3 = models.CharField(max_length=500)
    pesem4 = models.CharField(max_length=500)
    
    solidario1 = models.CharField(max_length=500)
    solidario2 = models.CharField(max_length=500)
    solidario3 = models.CharField(max_length=500)
    solidario4 = models.CharField(max_length=500)
    solidario5 = models.CharField(max_length=500)
    
    coovitel1 = models.CharField(max_length=500)
    coovitel2 = models.CharField(max_length=500)
    coovitel2Detalles = models.CharField(max_length=500)
    coovitel3 = models.CharField(max_length=500)
    coovitel4 = models.CharField(max_length=500)
    
    sugerencia1 = models.CharField(max_length=500)
    sugerencia2 = models.CharField(max_length=500)
    sugerencia3 = models.CharField(max_length=500)
    
    def __str__(self):
        return f"Registro asociado {self.name} - {self.cargo}"