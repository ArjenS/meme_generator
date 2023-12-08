"""MemeGenerator class to generate memes."""

import os
from PIL import Image, ImageDraw, ImageFont

from QuoteModel import QuoteModel


class MemeEngine():
    """A class to produce a picture with a quote inscribed."""
    
    def __init__(self, path: str):
        """Initialize the class."""        
        self.path = path        
        # self.text = text
        # self.author = author
        # self.width = width
    
    def load_image(self, path:str) -> Image:
        """Load an image.
        
        Argument:
            path: path to the image
        Returns:
            Image
        """        
        return Image.open(path)
    
    def resize_image(self, img: Image, width: int) -> Image:
        """Resize the image to a given width, scaling the height proportionally.
        
        Arguments:
            img: Image to be cropped
            width: width to resize the image to
        Returns:
            Image
        """
        try:
            ratio = width/float(img.size[0])
        except ValueError as e:
            print(e)
        height = int(ratio * float(img.size[1]))
        return img.resize((width,height), Image.NEAREST)    
    
    def add_message(self, img: Image, message: str, author: str) -> Image:
        """Add a message to an image.
        
        Arguments:
            img: Image to add a message to
            message: the message to be added
            author: the author of the message
        """
        try:
            draw = ImageDraw.Draw(img)
        except Exception as e:
            print(e)
        try:
            quote = QuoteModel(message, author)
            draw.text((10,30), str(quote))
        except Exception as e:
            print('Exception in add_message:', e)
        return img
        
    
    def save_image(self, img, path) -> None:
        """Save the image as a file.
        
        Arguments:
            img: the image to be saved
            path: the location where the image is to be saved
        Return:
            None
        """
        output_path = os.path.join(path,'meme.jpg')
        img.save(output_path)
        return output_path
        
        
    
    def make_meme(self, img_path, text, author, width=500)->str:
        """Create a meme using the methods in the MemeGenerator.
        
        Arguments:
            img_path: the location of the input image
            text: the body of the quote in the meme
            author: the author of the quote in te meme
            width: the width to which the image shoud be sized 
        Returns path on which the image is saved
        """
        if self.path:
            save_path = self.path
        image = self.load_image(path = img_path)
        image = self.resize_image(img = image, width = width)
        image = self.add_message(img = image, message = text, author = author)
        return self.save_image(img = image,path=save_path)