import asyncio

async def ask_ollama(prompt: str) -> str:
    try:
        process = await asyncio.create_subprocess_exec(
            "ollama", "run", "iapp/chinda-qwen3-4b",
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate(input=prompt.encode())

        if process.returncode != 0:
            return f"Error calling Ollama: {stderr.decode().strip()}"

        return stdout.decode().strip()
    except Exception as e:
        return f"Exception: {str(e)}"
