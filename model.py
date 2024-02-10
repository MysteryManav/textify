import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"


def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text
