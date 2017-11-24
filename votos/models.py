# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    Se decide utilizar este modelo para la clase candidato porque es necesario el nombre 
    y de q distrito pertenece dicho candidato
    """
    
    nombre=models.CharField("Nombre del candidato",max_length=30)
    distrito=models.ForeignKey(Distrito)



class Votos(models.Model):
    """
    Se decide utilizar este modelo para la clase votos porque es necesario
    saber a que candidato se le va a atribuir dicho voto
    """

    candidato=models.ForeignKey(Candidato)
