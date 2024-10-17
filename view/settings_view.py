
def main_menu():

    print("\nSETTINGS MENU\n")
    print("[1] Select platforms to scrap")
    print("[2] Change query search")
    print("[3] Initialize db")
    print("[4] Set NLP model")
    print("[0] Return\n")
    user_choice = input("Your choice ? ")

    return user_choice


def display_nlp_models(models_names):

    print("\nINSTALLED MODELS\n")

    model_index = 1
    for model_name in models_names:

        print(f"[{model_index}] {model_name}")
        model_index += 1

    print("[0] Return\n")
    user_choice = input("Your choice ? ")

    return user_choice
