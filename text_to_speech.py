from gtts import gTTS
from playsound import playsound
import tempfile
import os
import asyncio

async def speak(text: str):
    mp3_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as mp3_fp:
            tts = gTTS(text=text, lang='th')
            tts.save(mp3_fp.name)
            mp3_path = mp3_fp.name

        if mp3_path and os.path.exists(mp3_path):
            await asyncio.to_thread(playsound, mp3_path)
        else:
            print(f"❌ ไม่พบไฟล์เสียง: {mp3_path}")

    except Exception as e:
        print(f"❌ Error in TTS: {e}")

    finally:
        if mp3_path and os.path.exists(mp3_path):
            os.remove(mp3_path)
