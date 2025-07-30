from django.shortcuts import render
from .models import AudioGear, Charger

# Create your views here.
def home(request):
    audio_gears = AudioGear.objects.all()
    chargers = Charger.objects.all()
    return render(request, 'pages/index.html', {
        'audio_gears': audio_gears,
        'chargers': chargers
    })