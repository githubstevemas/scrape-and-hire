import fr_core_news_md

nlp = fr_core_news_md.load()

skills_list = ["python", "sql", "etl"]


def extract_skills(cv_text):

    doc = nlp(cv_text.lower())

    personnal_skills = []

    for word in doc:
        if word.text in skills_list:
            personnal_skills.append(word.text)

    # print(personnal_skills)

    return personnal_skills
