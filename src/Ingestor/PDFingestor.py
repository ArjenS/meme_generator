from typing import List
import subprocess
import os
import random

from .Docxingestor import IngestInterface
from .QuoteModel import QuoteModel


class PdfIngestor(IngestInterface):
    """Helper class implementation of the IngestInterface to parse pdf's"""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Can not ingest exception")

        tmp = f"./tmp/{random.randint(0, 1000000)}.txt"
        call = subprocess.check_call(["pdftotext", path, tmp])

        file_ref = open(tmp, "r")
        quotes = []

        for line in file_ref.readlines():
            line = line.strip("\n\r").strip()
            if len(line) > 0:
                parse = line.split(" - ")
                if len(parse) > 1:
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
        os.remove(tmp)
        return quotes
