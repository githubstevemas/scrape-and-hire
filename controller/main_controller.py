from dotenv import load_dotenv

from view.cv_view import display_name_cv
from . import scrap
from . import parse
from .cv import create_cv_folder_if_not, extract_pdf_data, get_pdf_file
from .db_manager import insert_cv
from .text_processing import extract_skills

load_dotenv()

job = "data"
location = "Toulouse"

query_link = \
    f"https://fr.indeed.com/jobs?q={job}&l={location}+%2831%29&from=searchOnHP"


def add_new_cv():

    create_cv_folder_if_not()

    pdf_to_upload = get_pdf_file()

    cv_text = extract_pdf_data(pdf_to_upload)

    if cv_text:

        cv_name = display_name_cv()
        skills = extract_skills(cv_text)

        cv_data = {
            "name": cv_name,
            "brute_text": cv_text,
            "key_words": skills
        }

        insert_cv(cv_data)


def get_data():

    content = scrap.get_page_content(query_link)
    parse.get_main_page(content)
