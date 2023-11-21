import os
from PIL import Image, ImageDraw, ImageFont


class MemeGenerator():
    """A class to produce a picture with a quote inscribed"""
    def __init__(self, ):
        pass
    
    def load_image(self, path:str) -> Image:
        """load an image
        Argument:
            path: path to the image
        Returns:
            Image"""
        
        return Image.open(path)
    
    def resize_image(self, img: Image, width: int) -> Image:
        """resize the image to a given width, scaling the height proportionally
        Arguments:
            img: Image to be cropped
            width: width to resize the image to
        Returns:
            Image"""
        try:
            ratio = width/float(img.size[0])
        except ValueError as e:
            print(e)
        height = int(ratio * float(img.size[1]))
        return img.resize((width,height), Image.NEAREST)
    
    def add_message(self, img: Image, message: str, author: str) -> Image:
        pass
    
    def save_image(self, img, path) -> None:
        pass
        
        
    
    def make_meme(self, img_path, text, author, width=500)->str:
        pass