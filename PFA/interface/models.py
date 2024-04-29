from django.db import models

class Tip(models.Model):
    type_of_catastrophe = models.CharField(max_length=100)
    content = models.TextField()

class NutrimentAndSupply(models.Model):
    type_of_catastrophe = models.CharField(max_length=100)
    content = models.TextField()

class EmergencyContact(models.Model):
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)