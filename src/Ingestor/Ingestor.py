from typing import List

from .IngestInterface import IngestInterface
from .QuoteModel import QuoteModel
from .TXTingestor import TXTIngestor
from .CSVingestor import CSVIngestor
from .PDFingestor import PDFIngestor
from .Docxingestor import DOCXIngestor

class Ingestor(IngestInterface):
    ingestors = [TXTIngestor,CSVIngestor,PDFIngestor,DOCXIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
