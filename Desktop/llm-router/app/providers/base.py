from abc import ABC, abstractmethod

class BaseProvider(ABC):
    name: str

    @abstractmethod
    async def generate(self, prompt: str):
        pass