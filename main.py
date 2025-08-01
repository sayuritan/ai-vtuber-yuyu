import asyncio
import subprocess
from stt import listen_audio       # ฟังเสียงแล้วแปลงเป็นข้อความ (ในตัวอย่างคือรับข้อความ input)
from chatbot import ask_ollama     # ส่งข้อความไป AI แล้วรอคำตอบ
from text_to_speech import speak_japanese  # แปลงข้อความเป็นไฟล์เสียง

# ฟังก์ชันรัน so-vits-svc แปลงเสียง (ต้องแก้ path ให้ตรงกับของคุณ)
async def convert_voice(input_wav: str, output_wav: str):
    process = await asyncio.create_subprocess_exec(
        "python", "so-vits-svc-fork-main/inference.py",
        "--input", input_wav,
        "--output", output_wav,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    if process.returncode != 0:
        print("Error in voice conversion:", stderr.decode())
        return None
    return output_wav

async def main():
    print("AI VTuber เริ่มต้นแล้ว พูดหรือพิมพ์ exit เพื่อออก")

    while True:
        print("กำลังฟังเสียง...")
        user_text = await listen_audio()  # รับข้อความจากเสียงหรือ input
        if user_text.lower() in ["exit", "quit"]:
            print("ออกจากโปรแกรมแล้ว")
            break

        print(f"คุณพูดว่า: {user_text}")
        ai_response = await ask_ollama(user_text)
        print(f"VTuber ตอบ: {ai_response}")

        # แปลงข้อความเป็นไฟล์เสียง
        output_wav = speak_japanese(ai_response)
        print(f"สร้างไฟล์เสียงที่: {output_wav}")

        # กำหนดไฟล์เสียง input สำหรับแปลงเสียง VTuber
        input_wav = output_wav
        converted_wav = "responses/converted.wav"

        # แปลงเสียงด้วย so-vits-svc
        converted_file = await convert_voice(input_wav, converted_wav)
        if converted_file:
            print(f"เล่นไฟล์เสียงแปลงเสียง: {converted_file}")
            # เปิดเล่นไฟล์เสียงที่แปลงแล้ว (Windows)
            subprocess.Popen(["start", converted_file], shell=True)

if __name__ == "__main__":
    asyncio.run(main())
