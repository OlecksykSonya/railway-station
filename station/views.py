from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Train, Route, Trip, Passenger, Ticket
from .forms import TrainForm, RouteForm, TripForm, PassengerForm, TicketForm

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contacts(request):
    return render(request, 'contacts.html')
def location(request):
    return render(request, 'location.html')
def schedule(request):
    return render(request, 'schedule.html')
def services(request):
    return render(request, 'services.html')

class TrainListView(ListView):
    model = Train
    template_name = 'trains/train_list.html'
    context_object_name = 'trains'


class TrainDetailView(DetailView):
    model = Train
    template_name = 'trains/train_detail.html'
    context_object_name = 'train'


class TrainCreateView(CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/train_form.html'
    success_url = reverse_lazy('train_list')


class TrainUpdateView(UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/train_form.html'
    success_url = reverse_lazy('train_list')


class TrainDeleteView(DeleteView):
    model = Train
    template_name = 'trains/train_confirm_delete.html'
    success_url = reverse_lazy('train_list')


class RouteListView(ListView):
    model = Route
    template_name = 'routes/route_list.html'
    context_object_name = 'routes'


class RouteDetailView(DetailView):
    model = Route
    template_name = 'routes/route_detail.html'
    context_object_name = 'route'


class RouteCreateView(CreateView):
    model = Route
    form_class = RouteForm
    template_name = 'routes/route_form.html'
    success_url = reverse_lazy('route_list')


class RouteUpdateView(UpdateView):
    model = Route
    form_class = RouteForm
    template_name = 'routes/route_form.html'
    success_url = reverse_lazy('route_list')


class RouteDeleteView(DeleteView):
    model = Route
    template_name = 'routes/route_confirm_delete.html'
    success_url = reverse_lazy('route_list')


class TripListView(ListView):
    model = Trip
    template_name = 'trips/trip_list.html'
    context_object_name = 'trips'


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'
    context_object_name = 'trip'


class TripCreateView(CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'trips/trip_form.html'
    success_url = reverse_lazy('trip_list')


class TripUpdateView(UpdateView):
    model = Trip
    form_class = TripForm
    template_name = 'trips/trip_form.html'
    success_url = reverse_lazy('trip_list')


class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'trips/trip_confirm_delete.html'
    success_url = reverse_lazy('trip_list')


class PassengerListView(ListView):
    model = Passenger
    template_name = 'passengers/passenger_list.html'
    context_object_name = 'passengers'


class PassengerDetailView(DetailView):
    model = Passenger
    template_name = 'passengers/passenger_detail.html'
    context_object_name = 'passenger'


class PassengerCreateView(CreateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'passengers/passenger_form.html'
    success_url = reverse_lazy('passenger_list')


class PassengerUpdateView(UpdateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'passengers/passenger_form.html'
    success_url = reverse_lazy('passenger_list')


class PassengerDeleteView(DeleteView):
    model = Passenger
    template_name = 'passengers/passenger_confirm_delete.html'
    success_url = reverse_lazy('passenger_list')

class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'


class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'tickets/ticket_detail.html'
    context_object_name = 'ticket'


class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket_list')


class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket_list')


class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'tickets/ticket_confirm_delete.html'
    success_url = reverse_lazy('ticket_list')