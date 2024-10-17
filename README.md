<p align="center">
  <img src="https://github.com/githubstevemas/scrape-and-hire/actions/workflows/ci.yml/badge.svg" alt="Build Status">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="Python Version">
</p>

# Scrape & Hire
<br>
 
This Python project allows users to upload their CV in PDF format and matches it with job postings scraped from job board like [Indeed](https://indeed.com). The system extracts key details from the CV and job descriptions, then calculates a matching score to help users find the most relevant job opportunities.

<br>

## Features
<br>

- Scrape job listings from multiple platforms
- Bypass JavaScript-based blocking with Selenium automation
- Upload and extract CV content for analysis
- Store many CVs and offers in SQL db
- Use NLP models for text processing
  
<br>

> [!NOTE]
> This project is currently in its beta phase, and the final version is still under development. See [Upcoming Features](#upcoming-features) for planned future releases.

<br>

## Technologies Used
<br>

- [Python](https://www.python.org/) - Core programming language
- [Flake8](https://flake8.pycqa.org/en/latest/) - For linting
- [Selenium](https://www.selenium.dev/) - For browser automation to bypass restrictions
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - For parsing HTML and extracting data
- [PosrtgreSQL](https://www.postgresql.org/) - For db storage
- [pdfplumber](https://github.com/jsvine/pdfplumber) - For text exctracting from pdf CV file
- [spaCy](https://spacy.io/) - For text processing and tokenization

<br>

## Install and configuration
<br>

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/githubstevemas/scrape-and-hire.git
   ```
   
2. **Install the required dependencies: Navigate to the project directory and run**:
   
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Install trained pipeline for spaCy**:
   
   ```bash
   python -m spacy download fr_core_news_md
   ```
   *(you can find more trained models [here](https://spacy.io/models))*

<br>

## How to run
<br>

*Once the project configuration is completed you can execute the following commands in the project folder to start server :*
```
 python main.py
```

<br>

## Usage
<br>

1. **Set NLP pipeline**:
   
   When trained pipeline is installed, go to Settings Menu, then set the dowloaded one as current. You can install many models and choose one for process.

<br>

## Troubleshooting
<br>

- **OSError: [E050] Can't find model 'fr_core_news_md'** : the trainned pipeline for spaCy is not installed, use ``python -m spacy download fr_core_news_md`` to download it.

<br>

## Upcoming Features
<br>

- Possibility of choosing the sites to scrape
- Possibility of choosing the driver for Selenium
- CV analysis (identify skills, experience, and qualifications from the extracted text)
- Extract relevant information from job descriptions in the database
- Compare the user's CV with the job descriptions in the database to evaluate the match

<br>

## Contact
<br>

Feel free to [mail me](mailto:mas.ste@gmail.com) for any questions, comments, or suggestions.
