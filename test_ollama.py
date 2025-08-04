import asyncio
from chatbot import ask_ollama

async def main():
    response = await ask_ollama("Hello, how are you?", model="tinyllama:latest")
    print(response)

asyncio.run(main())
