"""Helper for loading DOCX's"""
from typing import List
import docx
from QuoteModel import QuoteModel
from Ingestor import IngestInterface


class DocxIngestor(IngestInterface):
    """Helper class implementation of IngestInterface for docx documents"""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """parse the docx document
        Arguments:
            path: location of the docx document
        Returns:
            list of QuoteModels"""

        if not cls.can_ingest:
            raise Exception("cannot ingest exception")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(" - ")
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        return quotes
