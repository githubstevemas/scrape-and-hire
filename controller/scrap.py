import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager


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

    if driver:
        page_content = driver.page_source
    else:
        print(f"Something get wrong with {query_link} url.")

    time.sleep(2)

    driver.quit()

    return page_content
