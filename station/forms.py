from django import forms
from .models import Train, Route, Trip, Passenger, Ticket


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'