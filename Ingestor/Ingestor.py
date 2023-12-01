from typing import List
from QuoteModel import QuoteModel

from .IngestInterface import IngestInterface
from .TxtIngestor import TxtIngestor
from .CsvIngestor import CsvIngestor
#from .PdfIngestor import PdfIngestor TODO: Enable PDF
from .Docxingestor import DocxIngestor


class Ingestor(IngestInterface):
    """Realiziation of the IngestorInterface encapsulating helper classes for
    txt, csv, pdf and docx"""
    #TODO: enable PDF
    #ingestors = [TxtIngestor, CsvIngestor, PdfIngestor, DocxIngestor]
    ingestors = [TxtIngestor, CsvIngestor, DocxIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse method to call the separate functions in the helper classes.
        Argument:
            path: Location of the file to be parsed
        Returns: A list of QuoteModels for the permitted extensions
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
