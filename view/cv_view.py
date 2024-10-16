

def main_menu():

    print("\nCV MENU\n")
    print("[1] Define a CV to use")
    print("[2] Upload new CV")
    print("[3]")
    print("[0] Exit\n")
    user_choice = input("Your choice ? ")

    return user_choice


def display_upload_instructions(pdf_files):

    print("Choose cv to load\n")
    file_index = 1
    for file in pdf_files:
        print(f"[{file_index}] {file}")
        file_index += 1

    user_choice = input("\nYour choice ? ")

    return user_choice


def display_upload_success():

    print("CV successfully extracted.")
    input("Press Enter to continue.")


def display_name_cv():

    print("Give a name to your CV :")
    cv_name = input("")

    return cv_name


def display_current_cv(current_cv_name):

    print(f"\nCurrrent CV : {current_cv_name}")
    input("Press Enter to continue.")


def display_cvs_in_db(cvs_list):

    print("Choose cv to load\n")

    cv_index = 1
    for cv in cvs_list:
        print(f"[{cv_index}] {cv}")
        cv_index += 1

    user_choice = input("\nYour choice ? ")

    return user_choice


def display_no_cv_found():

    print("\nNo cv found in database.")
    input("Press Enter to continue.")
