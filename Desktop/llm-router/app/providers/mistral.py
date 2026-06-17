from app.providers.base import BaseProvider
from dotenv import load_dotenv
import httpx
import os
import time
from app.providers.base import BaseProvider


load_dotenv()



class MistralProvider(BaseProvider):
    name = "mistral"

    async def generate(self, prompt: str):
        start = time.time()
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.mistral.ai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "mistral-small-latest",
                    "messages":[
                        {"role":"user","content":prompt}
                    ],
                    "temperature": 0.7
                }
            )
        data = response.json()
        
        return {
            "text": data["choices"][0]["message"]["content"],
            "time": round(time.time() - start,3)
        }