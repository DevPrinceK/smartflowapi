from django.db import models

class Humidity(models.Model):
    '''records humidity data'''
    humidity = models.IntegerField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)

class Temperature(models.Model):
    '''records temperature data'''
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)
    
    
class Moisture(models.Model):
    '''records moisture data'''
    moisture = models.IntegerField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return str(self.date)