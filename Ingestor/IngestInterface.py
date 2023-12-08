from abc import ABC, abstractmethod
from typing import List
from QuoteModel import QuoteModel


class IngestInterface(ABC):
    """Define an abstract class for ingesting QuoteModels"""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Determine whether the class extension is in allowed_extension
        Arguments:
        path: location of the file to be ingested
        Returns:
        boolean True if extension in allowed_extension
        False otherwise
        """

        ext = path.split(".")[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """abstractmethod for the parse function"""
        pass
