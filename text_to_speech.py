import os
import uuid
from TTS.api import TTS

tts = TTS(model_name="tts_models/ja/kokoro/tacotron2-DDC", progress_bar=False, gpu=False)

def speak_japanese(text: str) -> str:
    if not os.path.exists("responses"):
        os.makedirs("responses")
    filename = f"responses/{uuid.uuid4().hex}.wav"
    tts.tts_to_file(text=text, file_path=filename)
    return filename
