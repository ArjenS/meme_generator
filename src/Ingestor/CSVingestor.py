from typing import List
import pandas

from .IngestInterface import IngestInterface
from .QuoteModel import QuoteModel


class CsvIngestor(IngestInterface):
    """Helper class implementation of the IngestInterface to parse csv's"""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """parse a file in path if it is a csv"""
        if not cls.can_ingest(path):
            raise Exception("Can not ingest")

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            if row["body"][0] != '"':
                row["body"] = f'"{row["body"]}"'
            new_quote = QuoteModel(row["body"], row["author"])
                
            quotes.append(new_quote)

        return quotes
