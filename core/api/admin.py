from django.contrib import admin

from .models import *

admin.site.register(Humidity)
admin.site.register(Moisture)
admin.site.register(Temperature)
