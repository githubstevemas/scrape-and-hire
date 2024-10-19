import spacy

from controller.job_board import set_config_job_board
from controller.text_processing import set_config_model
from view.settings_view import display_nlp_models, display_job_boards


def set_nlp_model():

    spacy_info = spacy.info()
    models_names = spacy_info["pipelines"]

    choosen_model = display_nlp_models(models_names)

    model_to_set = list(models_names.keys())[int(choosen_model) - 1]

    set_config_model(model_to_set)


def set_job_board():

    job_board_choice = display_job_boards()

    job_board_name = ""

    if job_board_choice == "1":
        job_board_name = "welcome"

    elif job_board_choice == "2":
        job_board_name = "indeed"

    set_config_job_board(job_board_name)
