from django.shortcuts import render
from .models import AudioGear, Charger, Phonecases

# Create your views here.
def home(request):
    audio_gears = AudioGear.objects.all()
    chargers = Charger.objects.all()
    phonecases = Phonecases.objects.all()
    return render(request, 'pages/index.html', {
        'audio_gears': audio_gears,
        'chargers': chargers,
        'phonecases': phonecases,
    })