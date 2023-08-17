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

# initialize firebase realtime database
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()



class OVerviewAPIView(APIView):
    '''For getting the overview of the data'''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        print("getting overview data...")
        return Response({
            "message": "Welcome to the API for the Smart Farming Project.",
            "endpoints": [
                {"endpoint": "all-data", "description": "Get all the data from the database"},
                {"endpoint": "humidity", "description": "Get all the humidity data from the database"},
                {"endpoint": "temperature", "description": "Get all the temperature data from the database"},
                {"endpoint": "moisture", "description": "Get all the moisture data from the database"},
                {"endpoint": "populate-db", "description": "Fetch data from the firebase realtime database and save it to the django database"},
                ],
            "url_format": "http://127.0.0.1:8000/api-v1/<endpoint>/",
           },
            status=status.HTTP_200_OK
        )


class FetchDataAPIView(APIView):
    '''
    Fetches data from the firebase realtime database 
    and saves it to the django database
    '''
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        '''For fetching data from the firebase realtime database'''
        humidity = database.child("bulkHumidity").get().val()
        moisture = database.child("bulkMoisture").get().val()
        temperature = database.child("bulkTemperature").get().val()
        hum_list = []
        temp_list = []
        moist_list = []
        for item in dict(humidity):
            if Humidity.objects.filter(date=item).exists():
                continue
            hum_list.append(Humidity(humidity=humidity[item], date=item))
            
        for item in dict(moisture):
            if Moisture.objects.filter(date=item).exists():
                continue
            moist_list.append(Moisture(moisture=moisture[item], date=item))
            
        for item in dict(temperature):
            if Temperature.objects.filter(date=item).exists():
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