from Ingestor.Ingestor import Ingestor


doc_file = "./_data/DogQuotes/DogQuotesDOCX.docx"
pdf_file = "./_data/DogQuotes/DogQuotesPDF.pdf"
csv_file = "./_data/DogQuotes/DogQuotesCSV.csv"
txt_file = "./_data/DogQuotes/DogQuotesTXT.txt"

print(Ingestor.parse(doc_file))
print(Ingestor.parse(pdf_file))
print(Ingestor.parse(csv_file))
print(Ingestor.parse(txt_file))
