from abc import ABC, abstractmethod
from typing import List

from .Quote import Quote

class IngestInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        pass


