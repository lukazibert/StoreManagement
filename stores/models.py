from django.db import models


class Store(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField('employes.Employee', related_name='employees')
