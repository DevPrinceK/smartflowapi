from django.urls import path
from . import views

urlpatterns = [
    path("all-data/", views.AllDataAPIView.as_view(), name="all_data"),
    path("humidity/", views.HumidityAPIView.as_view(), name="humidity"),
    path("temperature/", views.TemperatureAPIView.as_view(), name="temperature"),
    path("moisture/", views.MoistureAPIView.as_view(), name="moisture"),
    path("populate-db/", views.FetchDataAPIView.as_view(), name="populate"),
]
