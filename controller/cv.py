import os

import pdfplumber

from view.cv_view import display_upload_success


def create_cv_folder_if_not():
    # Create cv folder if not exists

    if not os.path.exists("CV"):
        os.makedirs("CV")


def extract_pdf_data():
    # Extract data from cv with pdfplumber

    text = []

    try:
        with pdfplumber.open("CV/cv.pdf") as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                display_upload_success()

    except Exception as e:
        print(e)

    return text
