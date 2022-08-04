from __future__ import division
from django.db import models

# Create your models here.
class Topology(models.Model):
    class Division(models.TextChoices):
        Production_division="Production division"
        Marketing_division = "Marketing division"
        General_division="General division"
        Personnel_division ="Personnel division"
        Human_resource_division ="Human resource division"
        Advertising_division="Advertising division"
    class TypeTopology(models.TextChoices):
        Bus_topology="Bus topology"
        Star_topology="Star topology"
        Ring_topology="Ring topology"
    full_name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    division = models.CharField(max_length=255,choices=Division.choices)
    type_topology = models.CharField(max_length=255,choices=TypeTopology.choices)