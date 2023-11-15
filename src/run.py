from Ingestor import TXTIngestor


#doc_file = './_data/DogQuotes/DogQuotesDOCX.docx'
#pdf_file = './_data/DogQuotes/DogQuotesPDF.pdf'
#csv_file = './_data/DogQuotes/DogQuotesCSV.csv'
txt_file = './_data/DogQuotes/DogQuotesTXT.txt'

#print(DOCXIngestor.parse(doc_file))
#print(PDFIngestor.parse(pdf_file))
#print(CSVIngestor.parse(csv_file))
print(TXTIngestor.parse(txt_file))