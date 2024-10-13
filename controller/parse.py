from bs4 import BeautifulSoup

from controller.scrap import get_page_content


def get_job_data(page_content):
    """
    With content page get data for one job

    arg: str with content for bs4
    return:
    """

    page_soup = BeautifulSoup(page_content, "html.parser")

    if page_soup:

        # GET TITLE
        title = page_soup.find(
            'h1',
            class_="jobsearch-JobInfoHeader-title css-1b4cr5z e1tiznh50"
        ).text

        # GET JOB TYPES
        div_job_types = page_soup.find_all(
            'div',
            class_='js-match-insights-provider-tvvxwd ecydgvn1'
        )

        job_types = []

        for job_type in div_job_types:

            job_type = job_type.text
            if job_type:
                job_types.append(job_type)

        # GET COMPANY
        company = page_soup.find(
            'div', {'data-company-name': 'true'}
        )
        company_name = company.find('a').text

        # GET DESCRIPTION
        job_description = page_soup.find('div', {'id': 'jobDescriptionText'})
        job_text = job_description.get_text(separator='\n').strip()

        print(f"\n{title} / {job_types} / {company_name}")
        print(job_text)
    else:
        print(f"Something get wrong with parsing.")


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

            get_job_data(content_job_page)

    else:
        print(f"No jobs found in {page_content}")

    return
