import whisper

def transcribe_audio(audio_file_path):
    model = whisper.load_model("base") # Choose a model based on your requirements
    result = model.transcribe(audio_file_path)
    return result["text"]