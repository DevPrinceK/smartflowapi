import random
import time
from datetime import datetime
from django.shortcuts import render

# import restapi essentials
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

# firebase realtime database config
import pyrebase

from api.models import EnvironmentalData, Humidity, Moisture, Temperature
from api.serializers import EnvironmentalDataSerializer, HumiditySerializer, MoistureSerializer, TemperatureSerializer
from core.utils.utilities import generate_data
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
            "message": "Welcome to the API for SmartFlow: The IoT-Based Smart Irrigation and Environmental Data Gathering System.",
            "endpoints": [
                {"endpoint": "all-data",
                    "description": "Get all the data from the database"},
                {"endpoint": "humidity",
                    "description": "Get all the humidity data from the database"},
                {"endpoint": "temperature",
                    "description": "Get all the temperature data from the database"},
                {"endpoint": "moisture",
                    "description": "Get all the moisture data from the database"},
                {"endpoint": "populate-db",
                    "description": "Fetch data from the firebase realtime database and save it to the django database"},
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
        all_data = dict(database.child("data").get().val())
        all_data_values = list(all_data.values())
        all_data_list = []

        for item in all_data_values:
            stamp = datetime.fromtimestamp(item['timestamp'])
            if EnvironmentalData.objects.filter(timestamp=stamp).exists():
                continue
            else:
                all_data_list.append(
                    EnvironmentalData(
                        humidity=item['humidity'],
                        temperature=item['temperature'],
                        moisture=item['moisture'],
                        timestamp=stamp,
                    )
                )
        # save the data to the database all at once
        EnvironmentalData.objects.bulk_create(all_data_list)
        return Response({
            "message": "Database Updated With More Data",
        },
            status=status.HTTP_200_OK
        )


class AllDataAPIView(APIView):
    '''For getting all environmental data from the database'''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_data = EnvironmentalData.objects.all().order_by("-id")
        return Response({
            "data": EnvironmentalDataSerializer(all_data, many=True).data,
        },
            status=status.HTTP_200_OK
        )


class HumidityAPIView(APIView):
    '''For getting humidity data from the database'''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_data = EnvironmentalData.objects.all().order_by("-id")
        all_humidity = [{"humidity": i.humidity, "timestamp": i.timestamp,
                         "created_at": i.created_at} for i in all_data]
        return Response({
            "humidity": all_humidity},
            status=status.HTTP_200_OK
        )


class TemperatureAPIView(APIView):
    '''For getting temperature data from the database'''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_data = EnvironmentalData.objects.all().order_by("-id")
        all_temperature = [{"temperature": i.temperature, "timestamp": i.timestamp,
                            "created_at": i.created_at} for i in all_data]
        return Response({
            "temperature": all_temperature, },
            status=status.HTTP_200_OK
        )


class MoistureAPIView(APIView):
    '''For getting moisture data from the database'''
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        all_data = EnvironmentalData.objects.all().order_by("-id")
        all_moisture = [{"moisture": i.moisture, "timestamp": i.timestamp,
                         "created_at": i.created_at} for i in all_data]
        return Response({
            "moisture": all_moisture, },
            status=status.HTTP_200_OK
        )


class GenerateRandomEnvData(APIView):
    '''Use to generate random environmental data'''
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            generate_data(frequency=20)
        except Exception as er:
            print(er)
            return Response({
                "message": str(er),
            }, status=status.HTTP_417_EXPECTATION_FAILED)
        else:
            print("Data Successfully Generated")
            return Response({
                "message": "Data Successfully Generated",
            }, status=status.HTTP_200_OK)
