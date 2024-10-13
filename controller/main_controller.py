from dotenv import load_dotenv

from . import scrap
from . import parse

load_dotenv()

job = "data"
location = "Toulouse"

query_link = \
    f"https://fr.indeed.com/jobs?q={job}&l={location}+%2831%29&from=searchOnHP"


def get_data():

    content = scrap.get_page_content(query_link)
    parse.get_main_page(content)
