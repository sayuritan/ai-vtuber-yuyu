import httpx
import asyncio

async def ask_ollama(prompt: str, model: str = "tinyllama:latest") -> str:
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    headers = {"Content-Type": "application/json"}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers, timeout=60)
            response.raise_for_status()
            data = response.json()
            return data.get("message", {}).get("content", "")
    except httpx.HTTPError as e:
        status_code = getattr(e.response, "status_code", "N/A")
        text = getattr(e.response, "text", "N/A")
        print(f"[HTTPError] Status code: {status_code}, Content: {text}")
    except Exception as e:
        print(f"[ERROR in ask_ollama] {e}")
    return ""
