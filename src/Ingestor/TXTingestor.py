from typing import List

from .IngestInterface import IngestInterface
from .Quote import Quote

class TXTIngestor(IngestInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception('Can not ingest')

        quotes=[]
        with open(path, 'r') as read_file:
            for line in read_file:
                if len(line) > 0:
                    line = line.split('-')                   
                    new_quote = Quote(line[0],line[1])
                    quotes.append(new_quote)
        return(quotes)