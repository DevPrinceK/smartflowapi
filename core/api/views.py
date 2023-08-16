from django.shortcuts import render

# import restapi essentials
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

# firebase realtime database config
import pyrebase

from api.models import Humidity, Moisture, Temperature
from api.serializers import HumiditySerializer, MoistureSerializer, TemperatureSerializer
from .firebase_config import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()


class FetchDataAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        '''For fetching data from the firebase realtime database'''
        humidity = database.child("bulkHumidity").get().val()
        moisture = database.child("bulkMoisture").get().val()
        temperature = database.child("bulkTemperature").get().val()
        # # use bulk_save to save multiple objects at once
        # Humidity.objects.bulk_create([Humidity(humidity=humidity[key], date=key) for key in dict(humidity)])
        # Moisture.objects.bulk_create([Moisture(moisture=moisture[key], date=key) for key in dict(moisture)])
        # Temperature.objects.bulk_create([Temperature(temperature=temperature[key], date=key) for key in dict(temperature)]) #noqa
        
        hum_list = []
        temp_list = []
        moist_list = []
        for item in dict(humidity):
            # check if item with same data already exists
            if Humidity.objects.filter(date=item).exists():
                # skip if item already exists
                continue
            hum_list.append(Humidity(humidity=humidity[item], date=item))
            
        for item in dict(moisture):
            # check if item with same data already exists
            if Moisture.objects.filter(date=item).exists():
                # skip if item already exists
                continue
            moist_list.append(Moisture(moisture=moisture[item], date=item))
            
        for item in dict(temperature):
            # check if item with same data already exists
            if Temperature.objects.filter(date=item).exists():
                # skip if item already exists
                continue
            temp_list.append(Temperature(temperature=temperature[item], date=item))
        
        # do bulk create to save multiple objects at once
        print("running bulk_create command...")
        Humidity.objects.bulk_create(hum_list)
        Moisture.objects.bulk_create(moist_list)
        Temperature.objects.bulk_create(temp_list)
        
        print("fetching data...")
        return Response({
            "message": "Database Updated With More Data",
            },
            status=status.HTTP_200_OK
        )


class AllDataAPIView(APIView):
    '''For getting all environmental data from the database'''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_humidity = Humidity.objects.all().order_by('-id')
        all_temperature = Temperature.objects.all().order_by('-id')
        all_moisture = Moisture.objects.all().order_by('-id')
        print("getting all data...")
        return Response({
            "humidity": HumiditySerializer(all_humidity, many=True).data,
            "temperature": TemperatureSerializer(all_temperature, many=True).data,
            "moisture": MoistureSerializer(all_moisture, many=True).data, },
            status=status.HTTP_200_OK
        )


class HumidityAPIView(APIView):
    '''For getting humidity data from the database'''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_humidity = Humidity.objects.all().order_by('-id')
        print("getting humidity data...")
        return Response({
            "humidity": HumiditySerializer(all_humidity, many=True).data, },
            status=status.HTTP_200_OK
        )
        

class TemperatureAPIView(APIView):
    '''For getting temperature data from the database'''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_temperature = Temperature.objects.all().order_by('-id')
        print("getting temperature data...")
        return Response({
            "temperature": TemperatureSerializer(all_temperature, many=True).data, },
            status=status.HTTP_200_OK
        )
        
        
class MoistureAPIView(APIView):
    '''For getting moisture data from the database'''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_moisture = Moisture.objects.all().order_by('-id')
        print("getting moisture data...")
        return Response({
            "moisture": MoistureSerializer(all_moisture, many=True).data, },
            status=status.HTTP_200_OK
        )