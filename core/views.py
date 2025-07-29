from django.shortcuts import render
from .models import AudioGear

# Create your views here.
def home(request):
    audio_gears=AudioGear.objects.all()
    return render(request, 'pages/index.html', {'audio_gears':audio_gears})