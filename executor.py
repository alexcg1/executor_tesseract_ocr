# Taken from https://towardsdatascience.com/create-simple-optical-character-recognition-ocr-with-python-6d90adb82bb8

from jina import Executor, DocumentArray, requests
from PIL import Image
import numpy as np
import pytesseract
import cv2


def process_image(doc):
    # process image
    img = np.array(Image.open(doc.uri))
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    img = cv2.GaussianBlur(img, (1, 1), 0)

    # extract text
    text = pytesseract.image_to_string(img)

    # store text in a tag
    doc.text = pytesseract.image_to_string(img)

    return doc


class TesseractOCR(Executor):
    @requests
    def extract_text(self, docs: DocumentArray, **kwargs):
        docs.apply(process_image)
