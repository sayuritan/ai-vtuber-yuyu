from datetime import datetime

def save_conversation(user_text, bot_text):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("conversation_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] คุณ: {user_text}\n")
        f.write(f"[{timestamp}] ยูยุ: {bot_text}\n")
