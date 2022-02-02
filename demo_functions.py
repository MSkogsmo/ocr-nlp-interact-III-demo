# Import tools
import os, io
from google.cloud import vision_v1 as vision
import openai
import sys
from google.cloud.vision_v1 import types
import pandas as pd

###OCR###

#Function for performing OCR on an image

def detect_text(img):
    # Open image
    with open(img, 'rb') as image_file:
        content = image_file.read()

    #Define input and perform ocr to get the response
    image = vision.types.Image(content=content)
    response = client.document_text_detection(
      image=image,
      image_context = {"language_hints": ['en']} #english text
      )
    return response


#Help function to write and read text file
def write_and_read_text_file(path_file_and_name, response):
  file = io.open(path_file_and_name, 'w', encoding='utf-8')
  file.write(response.full_text_annotation.text)
  file.close()
  text_file = open(path_file_and_name, "r", encoding='utf-8')
  text = text_file.read()
  return text