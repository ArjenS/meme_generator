import random
import os
import requests
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
        "./_data/DogQuotes/DogQuotesPDF.pdf",
        "./_data/DogQuotes/DogQuotesCSV.csv",
    ]

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    meme = MemeEngine("./static")
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""

    img_url = request.form.get("image_url")
    reponse = requests.get(img_url)
    tmp_img = f"{os.getcwd()}/tmp/{random.randint(0,1000000000)}.png"
    with open(tmp_img, "wb") as img:
        img.write(reponse.content)

    quote = QuoteModel(request.form.get("body"), request.form.get("author"))
    meme = MemeEngine("./static")
    path = meme.make_meme(tmp_img, quote.body, quote.author)
    os.remove(tmp_img)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
