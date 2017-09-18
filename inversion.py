#!/usr/bin/env python3
"""inversion.py is a Pillow Script designed to find all the images in a
   given directory and invert them for usage in formal technical reports """

__author__ = "Christopher Sweet"
__author__ = "Thomas Cenova"

from PIL import Image
from PIL import ImageOps
import os
import argparse

'''Finds all the images in the given directory with a .jpg extension
    and inverts them using the ImageOps library. Warning-Destructive
    @param - None'''
def invert(i_dir:str, o_dir:str):
    for f in os.listdir(i_dir):
        try:
            image = Image.open(i_dir +'/'+ f)
            if image.mode == 'RGBA':
                r,g,b,a = image.split()
                rgb_image = Image.merge('RGB', (r,g,b))
                inverted_image = ImageOps.invert(rgb_image)
                r2,g2,b2 = inverted_image.split()
                inverted_image = Image.merge('RGBA', (r2,g2,b2,a))
            else:
                inverted_image = ImageOps.invert(image)
            inverted_image.save(o_dir +'/'+ f)
        except IsADirectoryError as e:
            pass

parser = argparse.ArgumentParser(description="Take in directory locations")
parser.add_argument('-I', '--i_dir', type=str, nargs='?', default='./images/',
    action='store', help="Input directory to invert all images for")
parser.add_argument('-O', '--o_dir', type=str, nargs='?',
    action='store', help="Output directory to place all inverted images in")

args = parser.parse_args()

#Ensure Output Directory Exists before calling invert
try:
    if args.i_dir and args.o_dir:
        if not os.path.isdir(args.o_dir):
            os.mkdir(args.o_dir)
        invert(args.i_dir, args.o_dir)
    elif args.i_dir and not args.o_dir:
        o_dir = args.i_dir+'/inverted'
        if not os.path.isdir(o_dir):
            os.mkdir(o_dir)
        invert(args.i_dir, o_dir)
    else:
        raise FileNotFoundError("Invalid Path Given")
except FileNotFoundError as e:
    print(e)
