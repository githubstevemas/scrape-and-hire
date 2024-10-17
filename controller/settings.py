import spacy

from controller.text_processing import set_config_model
from view.settings_view import display_nlp_models


def set_nlp_model():

    spacy_info = spacy.info()
    models_names = spacy_info["pipelines"]

    choosen_model = display_nlp_models(models_names)

    model_to_set = list(models_names.keys())[int(choosen_model) - 1]

    set_config_model(model_to_set)
