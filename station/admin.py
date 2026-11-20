from django.contrib import admin
from .models import Station, TrainType, Train, Route, Trip, Schedule, Passenger, Ticket

admin.site.register(Station)
admin.site.register(TrainType)
admin.site.register(Train)
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(Schedule)
admin.site.register(Passenger)
admin.site.register(Ticket)
