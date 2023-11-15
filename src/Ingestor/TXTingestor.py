from typing import List

from .IngestInterface import IngestInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Can not ingest')

        quotes=[]
        with open(path, 'r') as read_file:
            for line in read_file:
                if len(line) > 0:
                    line = line.split('-')                   
                    new_quote = QuoteModel(line[0],line[1])
                    quotes.append(new_quote)
        return(quotes)