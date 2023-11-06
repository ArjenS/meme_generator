from typing import List
import docx

from .Quote import Quote

class DOCXIngestor(IngestInterface):
    allowed_extensions = ['docx']

    def parse(cls, path) -> List[Quote]:
        if not cls.can_ingest:
            raise Exception('cannot ingest exception')
        
        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(',')
                new_quote = Quote(parse[0],parse[1])
                quotes.append(new_quote)
        return quotes
