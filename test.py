import asyncio
from chatbot import ask_ollama

async def main():
    prompt = "Hello from test"
    response = await ask_ollama(prompt, model="tinyllama:latest")
    print(response)

asyncio.run(main())
