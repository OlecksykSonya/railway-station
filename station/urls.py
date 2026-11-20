
from django.urls import path
from . import views

urlpatterns = [
    # Основные страницы
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('location/', views.location, name='location'),
    path('schedule/', views.schedule, name='schedule'),
    path('services/', views.services, name='services'),

    # Поезда
    path('trains/', views.TrainListView.as_view(), name='train_list'),
    path('trains/create/', views.TrainCreateView.as_view(), name='train_create'),
    path('trains/<int:pk>/', views.TrainDetailView.as_view(), name='train_detail'),
    path('trains/<int:pk>/edit/', views.TrainUpdateView.as_view(), name='train_update'),
    path('trains/<int:pk>/delete/', views.TrainDeleteView.as_view(), name='train_delete'),

    # Маршруты
    path('routes/', views.RouteListView.as_view(), name='route_list'),
    path('routes/create/', views.RouteCreateView.as_view(), name='route_create'),
    path('routes/<int:pk>/', views.RouteDetailView.as_view(), name='route_detail'),
    path('routes/<int:pk>/edit/', views.RouteUpdateView.as_view(), name='route_update'),
    path('routes/<int:pk>/delete/', views.RouteDeleteView.as_view(), name='route_delete'),

    # Рейсы
    path('trips/', views.TripListView.as_view(), name='trip_list'),
    path('trips/create/', views.TripCreateView.as_view(), name='trip_create'),
    path('trips/<int:pk>/', views.TripDetailView.as_view(), name='trip_detail'),
    path('trips/<int:pk>/edit/', views.TripUpdateView.as_view(), name='trip_update'),
    path('trips/<int:pk>/delete/', views.TripDeleteView.as_view(), name='trip_delete'),

    # Пассажиры
    path('passengers/', views.PassengerListView.as_view(), name='passenger_list'),
    path('passengers/create/', views.PassengerCreateView.as_view(), name='passenger_create'),
    path('passengers/<int:pk>/', views.PassengerDetailView.as_view(), name='passenger_detail'),
    path('passengers/<int:pk>/edit/', views.PassengerUpdateView.as_view(), name='passenger_update'),
    path('passengers/<int:pk>/delete/', views.PassengerDeleteView.as_view(), name='passenger_delete'),

    # Билеты
    path('tickets/', views.TicketListView.as_view(), name='ticket_list'),
    path('tickets/create/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/<int:pk>/edit/', views.TicketUpdateView.as_view(), name='ticket_update'),
    path('tickets/<int:pk>/delete/', views.TicketDeleteView.as_view(), name='ticket_delete'),
]
