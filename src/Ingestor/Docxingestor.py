from typing import List
import docx
from Ingestor import IngestInterface

from .QuoteModel import QuoteModel

class DOCXIngestor(IngestInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        if not cls.can_ingest:
            raise Exception('cannot ingest exception')
        
        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                print(para.text)
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0],parse[1])
                quotes.append(new_QuoteModel)
        return quotes
