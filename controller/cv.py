import os

import pdfplumber

from controller.db_manager import get_cvs, define_cv_to_use, unset_current_cv
from view.cv_view import display_upload_instructions, display_cvs_in_db, \
    display_no_cv_found, display_current_cv


def get_cvs_in_db():
    # Get all cvs in db, then display them

    cvs_list = get_cvs()

    if cvs_list:
        cv_choice = display_cvs_in_db(cvs_list)
        cv_to_use = cvs_list[int(cv_choice) - 1]

        unset_current_cv()
        define_cv_to_use(cv_to_use)

        display_current_cv(cv_to_use)

    else:
        display_no_cv_found()


def get_pdf_file():
    """
    Get all pdf files in CV folder, ask user to choose one,
    then return pdf name file
    """

    files_list = []

    for file in os.listdir("CV/"):
        if file.endswith('.pdf'):
            files_list.append(file)

    file_choice = display_upload_instructions(files_list)
    file_to_upload = f"{files_list[int(file_choice) - 1]}"

    return file_to_upload


def create_cv_folder_if_not():
    # Create cv folder if not exists

    if not os.path.exists("CV"):
        os.makedirs("CV")


def extract_pdf_data(pdf_file_name):
    # Extract data from cv with pdfplumber

    text = []

    try:
        with pdfplumber.open(f"CV/{pdf_file_name}") as pdf:
            for page in pdf.pages:
                text = page.extract_text()

    except Exception as e:
        print(e)

    return text
