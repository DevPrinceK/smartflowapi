from rest_framework import serializers
from rest_framework.response import Response

from .models import *


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