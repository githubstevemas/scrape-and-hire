from bs4 import BeautifulSoup

from controller.db_insert import insert_job
from controller.scrap import get_page_content


def get_job_data(page_content):
    """
    With content page get data for one job

    arg: str with content for bs4
    return:
    """

    page_soup = BeautifulSoup(page_content, "html.parser")
    job_data = {}

    if page_soup:

        try:
            # GET TITLE
            title = page_soup.find(
                'h1',
                class_="jobsearch-JobInfoHeader-title css-1b4cr5z e1tiznh50"
            ).text

            # GET COMPANY
            company = page_soup.find(
                'div', {'data-company-name': 'true'}
            )
            company_name = company.find('a').text

            # GET DESCRIPTION
            job_text = page_soup.find('div', {'id': 'jobDescriptionText'})
            description = job_text.get_text(separator='\n').strip()

            print(f"\nOK -> {title} / {company_name}")

            job_data = {
                "title": title,
                "company": company_name,
                "description": description
            }

        except Exception as e:
            print(f"error -> {e}")

    else:
        print("Something get wrong with parsing.")

    return job_data


def get_main_page(page_content):
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

    if jobs_content:

        for job_content in jobs_content:

            job_link = job_content.find('a')
            job_url = f"https://www.indeed.com{job_link['href']}"

            content_job_page = get_page_content(job_url)
            job_data = get_job_data(content_job_page)

            # Insert data to db
            insert_job(job_data)

    else:
        print(f"No jobs found in {page_content}")

    return
