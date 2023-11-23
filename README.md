# MemeGenerator
This project contains functionality to create memes, that is images with a quote imposed on them. The project contains logic to ingest quotes from txt, csv, docx, and pdf files and adds them to pictures.
The quotes are listed in the _data/DogQuotes directory, the pictures in _data/photos.
## Setting up and running the program
Dependencies in the project are listed in requirements txt and can be installed with pip install -r requirements.txt

## Submodules
The project consists of the following modules:
- QuoteModel: Defines the quote format
- Ingestor: Ingests quotes from the files in './data/DogQuotes/' and returns them as a list of instances of QuoteModel
- MemeGenerator: Take images from ./_data/photos/, resize them and add a quote as defined in QuoteMode.


