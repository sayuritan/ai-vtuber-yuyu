import speech_recognition as sr
import asyncio

async def listen_audio() -> str:
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎙️ กำลังรอฟังเสียงของคุณ...")
            r.adjust_for_ambient_noise(source, duration=2)
            audio = await asyncio.to_thread(r.listen, source, timeout=10, phrase_time_limit=15)
    except sr.WaitTimeoutError:
        print("❌ ไม่มีเสียงภายในเวลาที่กำหนด")
        return ""
    except OSError as e:
        print(f"❌ ไม่พบไมโครโฟน หรือไมค์ใช้งานไม่ได้: {e}")
        return ""
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการรับเสียง: {e}")
        return ""

    try:
        text = await asyncio.to_thread(r.recognize_google, audio, language='th-TH')
        return text
    except sr.UnknownValueError:
        print("❌ ไม่เข้าใจเสียง กรุณาพูดใหม่อีกครั้ง")
        return ""
    except sr.RequestError as e:
        print(f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อบริการ STT: {e}")
        return ""
