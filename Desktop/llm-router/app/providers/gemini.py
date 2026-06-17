from google import genai
from dotenv import load_dotenv
import os
import time
from app.providers.base import BaseProvider
import asyncio

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
    )

class GeminiProvider(BaseProvider):
    name = "gemini"
    
    async def generate(self,prompt):
        start = time.time()
        try:
            response = await asyncio.to_thread( 
                client.models.generate_content,
                model = "gemini-2.5-flash",
                contents = prompt
            )
           
            return {
            "text": response.text,
            "time": round(time.time() - start,3)
        }
    
        except Exception as e:
            return {
                "error": f"Gemini error: {str(e)}",
                "time": round(time.time() - start,3)
            }    
