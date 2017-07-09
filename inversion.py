"""Inversion.py is a Pillow Script designed to find all the images in a
   given directory and invert them for usage in formal technical reports """

__author__ = "Christopher Sweet"

from PIL import Image
from PIL import ImageOps
import os

'''Finds all the images in the given directory with a .jpg extension
    and inverts them using the ImageOps library. Warning-Destructive
    @param - None'''
def invert():
    for file in os.listdir('./images'):
        if (file.endswith('.jpg')):
            image = Image.open("./images/"+file)
            inverted_image = ImageOps.invert(image)
            inverted_image.save("./inverted/"+file)

invert()
