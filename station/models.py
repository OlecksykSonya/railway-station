from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название станции')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    photo = models.ImageField(upload_to='stations/', blank=True, null=True, verbose_name='Фотография')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'


class TrainType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тип поезда')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип поезда'
        verbose_name_plural = 'Типы поездов'


class Train(models.Model):
    number = models.CharField(max_length=20, unique=True, verbose_name='Номер поезда')
    train_type = models.ForeignKey(TrainType, on_delete=models.PROTECT, verbose_name='Тип поезда')
    carriages_count = models.PositiveIntegerField(verbose_name='Количество вагонов')
    photo = models.ImageField(upload_to='trains/', blank=True, null=True, verbose_name='Фотография')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'


class Route(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название маршрута')
    departure_station = models.ForeignKey(
        Station, on_delete=models.PROTECT, related_name='departure_routes',
        verbose_name='Станция отправления'
    )
    arrival_station = models.ForeignKey(
        Station, on_delete=models.PROTECT, related_name='arrival_routes',
        verbose_name='Станция прибытия'
    )
    distance = models.PositiveIntegerField(verbose_name='Расстояние (км)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class Trip(models.Model):
    train = models.ForeignKey(Train, on_delete=models.PROTECT, verbose_name='Поезд')
    route = models.ForeignKey(Route, on_delete=models.PROTECT, verbose_name='Маршрут')
    departure_datetime = models.DateTimeField(verbose_name='Дата и время отправления')
    arrival_datetime = models.DateTimeField(verbose_name='Дата и время прибытия')
    is_delayed = models.BooleanField(default=False, verbose_name='Задержан')

    def __str__(self):
        return f'{self.train} — {self.route}'

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'


class Schedule(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, verbose_name='Рейс')
    station = models.ForeignKey(Station, on_delete=models.PROTECT, verbose_name='Станция')
    arrival_time = models.DateTimeField(blank=True, null=True, verbose_name='Время прибытия')
    departure_time = models.DateTimeField(blank=True, null=True, verbose_name='Время отправления')

    def __str__(self):
        return f'{self.trip} — {self.station}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class Passenger(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='ФИО пассажира')
    passport_number = models.CharField(max_length=20, unique=True, verbose_name='Номер паспорта')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Электронная почта')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пассажир'
        verbose_name_plural = 'Пассажиры'


class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.PROTECT, verbose_name='Пассажир')
    trip = models.ForeignKey(Trip, on_delete=models.PROTECT, verbose_name='Рейс')
    seat_number = models.PositiveIntegerField(verbose_name='Номер места')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    purchase_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')

    def __str__(self):
        return f'Билет №{self.id}'

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'