import asyncio
from chatbot import query_ollama  # นำเข้าฟังก์ชันจากไฟล์ chatbot.py

async def main():
    prompt = "Hello, how are you?"
    print(f"Prompt sent: {prompt}")
    response = await query_ollama(prompt)
    print(f"Response from Ollama: {response}")

if __name__ == "__main__":
    asyncio.run(main())
