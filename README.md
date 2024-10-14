<p align="center">
  <img src="https://github.com/githubstevemas/scrape-and-hire/actions/workflows/ci.yml/badge.svg" alt="Build Status">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python Version">
</p>

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
- [Flake8](https://flake8.pycqa.org/en/latest/) - For linting
- [Selenium](https://www.selenium.dev/) - For browser automation to bypass restrictions
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - For parsing HTML and extracting data
- [PosrtgreSQL](https://www.postgresql.org/) - For db storage
- [pdfplumber](https://github.com/jsvine/pdfplumber) - For text exctracting from pdf CV file

<br>

## Install and configuration

1. **Clone the repository**:
   ```bash
   git clone https://github.com/githubstevemas/scrape-and-hire.git
   ```
2. **Install the required dependencies: Navigate to the project directory and run**:
   ```bash
   pip install -r requirements.txt
   ```

<br>

## How to run

*Once the project configuration is completed you can execute the following commands in the project folder to start server :*
```
 python main.py
```

<br>

## Usage

*Soon*

<br>

## Troubleshooting

*Soon*

<br>

## Changelog

*Soon*

<br>

## Contact

Feel free to [mail me](mailto:mas.ste@gmail.com) for any questions, comments, or suggestions.
