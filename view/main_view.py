

def main_menu():

    print("\nMAIN MENU\n")
    print("[1] Scrap job offers")
    print("[2] CV menu")
    print("[3] ")
    print("[4] Settings\n")
    print("[0] Exit\n")
    user_choice = input("Your choice ? ")

    return user_choice


def clear_screen():

    print("\n" * 100)


def no_model_installed():

    print("No NLP model installed.")
    print("Use for exemple : python -m spacy download fr_core_news_md")
    print("Then set as current in Settings menu\n")
    print("More pipelines at https://spacy.io/models")


def no_job_board_settled():

    print("No job board settled.")
