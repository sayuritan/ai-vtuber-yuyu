from datetime import datetime

def clean_response(raw: str) -> str:
    return raw.strip()

def is_valid_reply(text: str) -> bool:
    return bool(text and len(text.strip()) > 0 and "Request error" not in text)

def clean_reply(text: str) -> str:
    return ' '.join(text.split())

def save_conversation(user_text: str, bot_text: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("conversation_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] User: {user_text}\n")
            f.write(f"[{timestamp}] Yuyu: {bot_text}\n\n")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดขณะบันทึกบทสนทนา: {e}")
