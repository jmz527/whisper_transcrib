from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .whisper_utils import transcribe_audio

# Create your views here.

def index(response):
	return HttpResponse("Hello World!")

def transcribe_view(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('240325_1920.mp3')
        if audio_file:
            transcription = transcribe_audio(audio_file)
            return JsonResponse({'transcription': transcription})
        else:
            return JsonResponse({'error': 'No audio file provided'})
    return render(request, 'transcribe.html')