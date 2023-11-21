from Ingestor.Ingestor import Ingestor


doc_file = "./src/_data/DogQuotes/DogQuotesDOCX.docx"
pdf_file = "./src/_data/DogQuotes/DogQuotesPDF.pdf"
csv_file = "./src/_data/DogQuotes/DogQuotesCSV.csv"
txt_file = "./src/_data/DogQuotes/DogQuotesTXT.txt"

print(Ingestor.parse(doc_file))
print(Ingestor.parse(pdf_file))
print(Ingestor.parse(csv_file))
print(Ingestor.parse(txt_file))
