import requests
from bs4 import BeautifulSoup

import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager

from controller.db_manager import insert_job

MAIN_URL = (
    "https://www.welcometothejungle.com/fr/"
    "jobs?query=Data&refinementList%5Boffices.country_code%5D%5B%5D=FR")


def find_job_content(text_to_parse):

    soup = BeautifulSoup(text_to_parse, "html.parser")

    link = soup.find_all("a", class_="sc-1gjh7r6-0 iPeVkS")

    for li in link:

        job_content = get_main_jobs_content(
            f"https://www.welcometothejungle.com{li["href"]}")

        title = job_content.find("h2").text

        company = job_content.find("a",
                                   class_="sc-jdUcAg eRJzJL").text

        description = job_content.find("div",
                                       class_="sc-1tacsq-1 dVuJea").find_all(
            "p")

        description_text = ' '.join([p.text for p in description])

        new_job = {"title": title,
                   "company": company,
                   "description": description_text
                   }

        insert_job(new_job)

    return


def get_page_content(query_link):
    """
    With Selenium, get page content from query_link url

    return: str with content for one page
    """

    # print("Scraping page in progress...")

    options = webdriver.EdgeOptions()
    options.use_chromium = True

    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options)

    driver.get(query_link)

    page_content = ''

    time.sleep(5)

    try:
        page_content = driver.page_source

    except Exception as e:
        print(e)

    driver.quit()

    return page_content


def get_main_jobs_content(url_to_scrap):
    response = requests.get(url_to_scrap)
    soup = BeautifulSoup(response.text, "html.parser")

    return soup


def main_scrap():
    main_soup = get_page_content(MAIN_URL)
    find_job_content(main_soup)
