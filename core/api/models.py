from django.db import models


class EnvironmentalData(models.Model):
    '''records environmental data from the sensor'''
    humidity = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    moisture = models.IntegerField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.timestamp


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