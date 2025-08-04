import asyncio
from stt import listen_audio
from chatbot import ask_ollama
from text_to_speech import speak
from utils import clean_response, is_valid_reply, clean_reply, save_conversation
from translate import translate_to_th, translate_to_en

async def main():
    print("✨ Yuyu AI VTuber พร้อมใช้งานแล้ว ✨")
    print("🎤 พูดภาษาไทยกับยูยุได้เลย...")

    try:
        while True:
            print("\n🎧 กำลังฟัง...")
            try:
                user_input_th = await listen_audio()
            except Exception as e:
                print(f"❌ เกิดข้อผิดพลาดขณะฟังเสียง: {e}")
                continue

            if not user_input_th or len(user_input_th.strip()) < 1:
                print("❌ ไม่ได้รับเสียงหรือไม่เข้าใจ กรุณาพูดใหม่อีกครั้ง")
                continue

            if any(word in user_input_th.lower() for word in ["หยุด", "เลิก", "ออก", "bye", "exit"]):
                print("👋 ขอบคุณที่ใช้บริการ Yuyu AI VTuber ลาก่อนค่ะ!")
                break

            user_input_en = translate_to_en(user_input_th)
            if not user_input_en:
                print("❌ แปลภาษาอังกฤษไม่สำเร็จ กรุณาพูดใหม่อีกครั้ง")
                continue

            prompt = (
                "You are Yuyu, a cute and polite anime VTuber girl. "
                "Always respond briefly, in a kind and moe style.\n"
                f"User: {user_input_en}\n"
                "Yuyu:"
            )

            try:
                raw_response = await ask_ollama(prompt)
                if not raw_response:
                    print("❌ Ollama ไม่ตอบกลับ กรุณาพูดใหม่อีกครั้ง")
                    continue
            except Exception as e:
                print(f"❌ เกิดข้อผิดพลาดจาก Ollama: {e}")
                continue

            cleaned = clean_response(raw_response)

            if is_valid_reply(cleaned):
                final_en = clean_reply(cleaned)
            else:
                final_en = "I'm a bit confused~ Can you say it another way?"

            final_th = translate_to_th(final_en)
            if not final_th:
                final_th = "ขอโทษค่ะ ฉันยังไม่เข้าใจ ลองพูดใหม่อีกครั้งนะ"

            print(f"🎀 ยูยุ (ภาษาไทย): {final_th}")

            try:
                await speak(final_th)
            except Exception as e:
                print(f"❌ Error in TTS: {e}")

            try:
                save_conversation(user_input_th, final_th)
            except Exception as e:
                print(f"⚠️ ไม่สามารถบันทึกบทสนทนาได้: {e}")

            await asyncio.sleep(0.5)
    except KeyboardInterrupt:
        print("\n👋 ออกโปรแกรมเรียบร้อย ขอบคุณที่ใช้บริการค่ะ!")

if __name__ == "__main__":
    asyncio.run(main())
