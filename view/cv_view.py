

def main_menu():

    print("\nCV MENU\n")
    print("[1] Current CV")
    print("[2] Upload new CV")
    print("[3]")
    print("[0] Exit\n")
    user_choice = input("Your choice ? ")

    return user_choice


def display_upload_instructions():

    print("\nSubmit your CV in pdf format in the CV folder.")
    input("Then press Enter to continue.")


def display_upload_success():

    print("CV successfully extracted.")
    input("Press Enter to continue.")


def display_name_cv():

    print("Give a name to your CV :")
    cv_name = input("")

    return cv_name
