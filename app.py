import random
import os
import requests
import urllib
from flask import Flask, render_template, abort, request
from Ingestor import Ingestor
from MemeEngine import MemeEngine
from QuoteModel import QuoteModel


app = Flask(__name__)

meme = MemeEngine("./static")


def setup():
    """Load all resources"""

    quote_files = [
        "./_data/DogQuotes/DogQuotesTXT.txt",
        "./_data/DogQuotes/DogQuotesDOCX.docx",
        #"./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]
    
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))           

    images_path = "./_data/photos/dog/"

    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root,name) for name in files]    

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)    
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""
    
    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.       
    # image_url = image_url
    
    img_url = request.form.get("img_url")
    img_path = os.path.join('.','tmp','image.png')  #'.\tmp\image.png'
    urllib.request.urlretrieve(img_url,img_path)
        
    quote = QuoteModel(request.form.get("body"),request.form.get("author"))
    path = meme.make_meme(filename,quote.body,quote.author)

    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
