# Scrape & Hire
 
This Python project allows users to upload their CV in PDF format and matches it with job postings scraped from job board like [Indeed](https://indeed.com). The system extracts key details from the CV and job descriptions, then calculates a matching score to help users find the most relevant job opportunities.

<br>

## Features

- Scrape job listings from multiple platforms
- Bypass JavaScript-based blocking with Selenium automation
- Parse and extract relevant job details with BeautifulSoup
- Upload and extract CV for analysis
- Store many CVs and offers

<br>

## Technologies Used

- [Python](https://www.python.org/) - Core programming language
- [Selenium](https://www.selenium.dev/) - For browser automation to bypass restrictions
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - For parsing HTML and extracting data
- [PosrtgreSQL](https://www.postgresql.org/) - For db storage
- [pdfplumber](https://github.com/jsvine/pdfplumber) - For text exctracting from pdf CV file

<br>

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/githubstevemas/scrape-and-hire.git
   ```
2. **Install the required dependencies: Navigate to the project directory and run**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   python main.py
   ```

<br>

## Usage

Modify the scraping targets: In the main.py file, you can define the target URLs for scraping.

<br>

## Contact

Feel free to [mail me](mailto:mas.ste@gmail.com) for any questions, comments, or suggestions.