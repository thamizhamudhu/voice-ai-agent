import whisper
import tempfile

model = whisper.load_model("base")

def transcribe_audio(audio_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    return result["text"]