import time
from deep_translator import GoogleTranslator

def translate_to_en(text: str, retries=3, delay=1) -> str:
    for attempt in range(retries):
        try:
            return GoogleTranslator(source='th', target='en').translate(text)
        except Exception as e:
            print(f"❌ แปลไทย→อังกฤษไม่สำเร็จ (ครั้งที่ {attempt+1}): {e}")
            time.sleep(delay)
    print("⚠️ คืนข้อความเดิมโดยไม่แปล (ไทย→อังกฤษ)")
    return text

def translate_to_th(text: str, retries=3, delay=1) -> str:
    for attempt in range(retries):
        try:
            return GoogleTranslator(source='en', target='th').translate(text)
        except Exception as e:
            print(f"❌ แปลอังกฤษ→ไทยไม่สำเร็จ (ครั้งที่ {attempt+1}): {e}")
            time.sleep(delay)
    print("⚠️ คืนข้อความเดิมโดยไม่แปล (อังกฤษ→ไทย)")
    return text
