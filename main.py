from selenium import webdriver
from selenium.webdriver.edge.service import Service
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from webdriver_manager.microsoft import EdgeChromiumDriverManager

load_dotenv()

job = "data"
location = "Toulouse"

query_link = \
    f"https://fr.indeed.com/jobs?q={job}&l={location}+%2831%29&from=searchOnHP"


def get_page_content():
    """
    With Selenium, get page content from query_link url

    return: str with content for one page
    """

    options = webdriver.EdgeOptions()
    options.use_chromium = True

    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options)

    driver.get(query_link)

    page_content = ''

    if driver:
        page_content = driver.page_source
    else:
        print("Something get wrong with query_link url.")

    return page_content


def get_jobs_main_page(page_content):
    """
    With content page get all jobs url for one page

    arg: str with content for bs4
    return: list of urls jobs for one page
    """

    main_soup = BeautifulSoup(page_content, "html.parser")

    jobs_content = main_soup.find_all(
        'h2',
        class_='jobTitle css-198pbd eu4oa1w0'
    )

    jobs_list = []

    if jobs_content:

        for job_content in jobs_content:

            job_link = job_content.find('a')
            job_url = f"indeed.com{job_link['href']}"
            jobs_list.append(job_url)

    else:
        print(f"No jobs found in {page_content}")

    return jobs_list


content = get_page_content()

jobs_urls_list = get_jobs_main_page(content)
