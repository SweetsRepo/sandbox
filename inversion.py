"""inversion.py is a Pillow Script designed to find all the images in a
   given directory and invert them for usage in formal technical reports """

__author__ = "Christopher Sweet"

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
            image = Image.open(i_dir + f)
            inverted_image = ImageOps.invert(image)
            inverted_image.save(o_dir + f)
        except TypeError as e:
            raise e

parser = argparse.ArgumentParser(description="Take in directory locations")
parser.add_argument('-I', '--i_dir', type=str, nargs='?', default='./images/',
    action='store', help="Input directory to invert all images for")
parser.add_argument('-O', '--o_dir', type=str, nargs='?',
    action='store', help="Output directory to place all inverted images in")

args = parser.parse_args()
#Check input for directory structure and append / if needed
if args.i_dir[-1] != '/':
    args.i_dir = args.i_dir+'/'
if args.o_dir[-1] != '/':
    args.o_dir = args.o_dir+'/'

try:
    if args.i_dir and args.o_dir:
        invert(args.i_dir, args.o_dir)
    elif args.i_dir and not args.o_dir:
        o_dir = '../'+i_dir+'/inverted'
        if os.isdir(o_dir):
            invert(args.i_dir, o_dir)
        else:
            os.mkdir(o_dir)
            invert(args.i_dir, o_dir)
    else:
        raise FileNotFoundError("Invalid Path Given")
except FileNotFoundError as e:
    print(e)
