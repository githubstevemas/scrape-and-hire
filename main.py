from controller import main_controller
from controller.cv import create_cv_folder_if_not, extract_pdf_data
from controller.db_insert import insert_cv
from model.db import create_tables
from view import main_view, settings_view, cv_view
from view.cv_view import display_name_cv, display_upload_instructions


def main():
    while True:

        user_choice = main_view.main_menu()

        if user_choice == '1':
            # Start scraping

            print("Scrap in progress...")
            main_controller.get_data()

        if user_choice == '2':
            # CV menu

            user_cv_choice = cv_view.main_menu()

            if user_cv_choice == "1":
                # Current CV
                pass

            if user_cv_choice == "2":
                # Upload CV

                create_cv_folder_if_not()
                display_upload_instructions()
                cv_text = extract_pdf_data()

                if cv_text:
                    cv_name = display_name_cv()

                    cv_data = {
                        "name": cv_name,
                        "brute_text": cv_text
                    }

                    insert_cv(cv_data)

                main()

            if user_cv_choice == "0":
                main()

        if user_choice == '4':
            # Display settings menu

            user_settings_choice = settings_view.main_menu()

            if user_settings_choice == "3":
                # Initialize db

                create_tables()
                main()

            if user_settings_choice == "0":
                main()


if __name__ == "__main__":
    main()
