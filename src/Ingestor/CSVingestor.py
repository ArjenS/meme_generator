from typing import List
import pandas

from .IngestInterface import IngestInterface
from .Quote import Quote

class CSVIngestor(IngestInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path:str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception('Can not ingest')
        
        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = Quote(row['body'],row['author'])
            quotes.append(new_quote)
    
        return quotes
