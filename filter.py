import re

def is_valid_reply(text: str) -> bool:
    if not text or len(text.strip()) < 2:
        return False
    if not re.search(r'[\u0E00-\u0E7F]', text):  # ภาษาไทย
        return False
    if re.search(r'(https?://|www\.|\.com|\.net|\.io|\.org)', text, re.IGNORECASE):
        return False
    return True

def clean_response(raw: str) -> str:
    text = raw.strip()
    
    # ตัดอิโมจิและอักขระแปลก ๆ ยกเว้นตัวอักษร, ตัวเลข, .,!?() และเว้นวรรค
    text = re.sub(r'[^\u0E00-\u0E7Fa-zA-Z0-9\s.,!?()]+', '', text)

    # แยกบรรทัดแล้วเก็บเฉพาะที่มีภาษาไทย
    lines = [line.strip() for line in text.splitlines() if re.search(r'[\u0E00-\u0E7F]', line)]

    if not lines:
        return ""

    first_line = lines[0]
    return first_line[:150].rstrip() + ("..." if len(first_line) > 150 else "")

def clean_reply(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

# 🧪 ทดสอบด้วยข้อความตัวอย่าง
raw_text = """
[🌸ยูยุ]: สวัสดีค่า~ วันนี้อากาศดีจังเลย! 🌞✨
ลองไปเดินเล่นกันไหมคะ? https://example.com
"""

# 🔄 ใช้ฟังก์ชันทั้งหมด
if is_valid_reply(raw_text):
    cleaned = clean_response(raw_text)
    final = clean_reply(cleaned)
    print("✅ ข้อความที่สะอาดแล้ว:", final)
else:
    print("❌ ข้อความไม่ผ่านการตรวจสอบ")
