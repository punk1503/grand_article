"""
A simple program that will run through the pdf file of
the article and count the exact price of posting based on
prices per character and image.
"""
import pdfplumber
from tqdm import tqdm
from math import ceil
from os import listdir
import time
import sys


# prices in rub
BASE_PRICE = 150
IMAGE_PRICE = 50
CHAR_PRICE = 500 # for each 1500 characters

image_counter = 0
character_counter = 0

def count_article_price(article_pdf_object):
    article_characters_counter = 0
    article_images_counter = 0
    for page in tqdm(article_pdf_object.pages):
        article_characters_counter += len(page.chars)
        article_images_counter += len(page.images)

    chars_cost = ceil(article_characters_counter/1500) * CHAR_PRICE
    images_cost = IMAGE_PRICE * article_images_counter

    sys.stdout.write("]\n") # this ends the progress bar
    return chars_cost + images_cost + BASE_PRICE
    

folder_path = input('Folder path (leave blank to user current directory):')
folder_path = '.' if folder_path == '' else folder_path
final_price = 0
for file in listdir(folder_path):
    if file.endswith('.pdf'):
        with pdfplumber.open(folder_path + '/' + file) as article_pdf_object:
            final_price += count_article_price(article_pdf_object)

print("Final price is", final_price)