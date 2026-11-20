from django.shortcuts import render
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