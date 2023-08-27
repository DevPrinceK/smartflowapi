from rest_framework import serializers

from .models import *


class EnvironmentalDataSerializer(serializers.ModelSerializer):
    '''serializes environmental data'''

    class Meta:
        model = EnvironmentalData
        fields = '__all__'


class HumiditySerializer(serializers.ModelSerializer):
    '''serializes humidity data'''

    class Meta:
        model = Humidity
        fields = '__all__'
        
        
class MoistureSerializer(serializers.ModelSerializer):
    '''serializes moisture data'''

    class Meta:
        model = Moisture
        fields = '__all__'
        
        
class TemperatureSerializer(serializers.ModelSerializer):
    '''serializes temperature data'''

    class Meta:
        model = Temperature
        fields = '__all__'