import configparser

import spacy

from view.main_view import no_model_installed

skills_list = ["python", "sql", "etl"]
config = configparser.ConfigParser()


def get_current_nlp_model():
    # Read config ini file and return current NLP model

    config.read('config.ini')
    preferred_model = config['UserPreferences']['preferred_model']

    return preferred_model


def set_config_model(model_to_set):
    # Set new NLP model in config ini file

    config.read('config.ini')
    config['UserPreferences']['preferred_model'] = model_to_set

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def extract_skills(cv_text):

    model_name = get_current_nlp_model()

    if not model_name:

        no_model_installed()
        return

    nlp = spacy.load(model_name)
    doc = nlp(cv_text.lower())

    personnal_skills = []

    for word in doc:
        if word.text in skills_list:
            personnal_skills.append(word.text)

    print(skills_list)

    """
    print("Skills:")
    for skill in personnal_skills:
        print(skill)
    """

    return personnal_skills
