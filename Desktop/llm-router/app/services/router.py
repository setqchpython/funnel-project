import asyncio
import time

class Router:
    def __init__(self, providers):
        self.providers = providers
        
    async def _call(self,provider,prompt):
        start = time.time()
        
        try:
            result = await provider.generate(prompt)
            
            return {
                "provider": provider.name,
                "result": result,
                "time": round(time.time() - start, 3)
            }
        except Exception as e:
            return {
                "provider": provider.name,
                "error": str(e),
                "time": round(time.time() - start,3)
            }
            
    async def ask_all(self,prompt:str):
        tasks = [
            self._call(p, prompt)
            for p in self.providers
        ]
        
        return await asyncio.gather(*tasks)