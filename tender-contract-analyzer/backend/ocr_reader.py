
from PIL import Image
import numpy as np

import cv2
import pytesseract

from config import TESSERACT_PATH

if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def preprocess_image(image):
    """
    Preprocess image for better OCR accuracy.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    _, threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return threshold


def extract_image_text(image_path: str) -> str:
    """
    Extract text from scanned image using OCR.
    """

    try:
        # Read image using PIL
        image = Image.open(image_path)

        # Convert to OpenCV format
        image = np.array(image)

        # Convert RGB to BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Preprocess image
        processed_image = preprocess_image(image)

        # OCR
        text = pytesseract.image_to_string(
            processed_image,
            lang="eng"
        )

        return text

    except Exception as e:
        print("OCR Error:", e)
        return ""