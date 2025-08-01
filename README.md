# AI VTuber - Voice Chatbot with Ollama and so-vits-svc Voice Conversion

โปรเจกต์นี้เป็นระบบ VTuber ที่รองรับการพูดคุยด้วย AI ผ่าน Ollama Model (Chinda Qwen3-4B)  
และแปลงข้อความเป็นเสียงภาษาญี่ปุ่นด้วย TTS โมเดล Kokoro  
พร้อมแปลงเสียงเป็นเสียง VTuber ด้วย so-vits-svc (voice conversion)

---

## ฟีเจอร์หลัก

- รับข้อความจากผู้ใช้ (ตัวอย่างใช้ `input()` แทนการฟังเสียงจริง)  
- ส่งข้อความให้ Ollama AI ตอบกลับแบบ async  
- แปลงข้อความ AI เป็นไฟล์เสียง `.wav` ด้วยโมเดล TTS  
- แปลงเสียงเป็นเสียง VTuber ด้วย so-vits-svc  
- เล่นไฟล์เสียงที่แปลงเสร็จทันที (Windows)

---

## โครงสร้างไฟล์

├── chatbot.py # ฟังก์ชันเรียก Ollama AI
├── stt.py # ฟังก์ชันรับข้อความจากผู้ใช้ (แทน speech-to-text)
├── text_to_speech.py # ฟังก์ชันแปลงข้อความเป็นเสียง (TTS)
├── main.py # โปรแกรมหลักรันลูป AI VTuber
├── so-vits-svc-fork-main/ # โฟลเดอร์โปรเจกต์ so-vits-svc สำหรับแปลงเสียง
└── responses/ # โฟลเดอร์เก็บไฟล์เสียงผลลัพธ์

---

## การติดตั้ง

1. ติดตั้ง Python 3.8+ (แนะนำ 3.11) และตั้ง PATH ให้เรียก python ได้จาก terminal

2. ติดตั้งไลบรารีหลักด้วยคำสั่ง:

```bash
pip install TTS asyncio
ติดตั้งและตั้งค่า Ollama CLI และโมเดล iapp/chinda-qwen3-4b ตาม เว็บไซต์ Ollama

ดาวน์โหลดและติดตั้ง so-vits-svc โปรเจกต์ so-vits-svc-fork (หรือโฟลเดอร์ที่คุณใช้)

ตั้งค่าไฟล์โมเดลเสียงตามคู่มือในโฟลเดอร์นี้

ทดสอบรัน inference.py แยกก่อน
วิธีรัน
รันโปรแกรมหลัก

bash
Copy
Edit
python main.py
พิมพ์ข้อความในคอนโซล (แทนพูดเสียงจริง) แล้วกด Enter

ระบบจะส่งข้อความให้ Ollama AI ตอบกลับ

คำตอบจะถูกแปลงเป็นเสียงและแปลงเสียง VTuber พร้อมเล่นเสียงออกลำโพง

พิมพ์ exit หรือ quit เพื่อออกจากโปรแกรม

หมายเหตุ
โปรแกรมนี้ตัวอย่างใช้ input() รับข้อความแทนการแปลงเสียงจริง (Speech-to-Text)

สามารถต่อยอดระบบให้เชื่อมกับไมโครโฟนและแปลงเสียงพูดจริงได้

โฟลเดอร์ responses/ เก็บไฟล์เสียง .wav ที่สร้างขึ้น

คำสั่ง subprocess.Popen(["start", converted_file], shell=True) ใช้สำหรับ Windows หากใช้ระบบอื่นต้องเปลี่ยนคำสั่งเล่นเสียง

ติดต่อ
GitHub: https://github.com/sayuritan/yuyu
Email:eukkgcddhjk@gmail.com
