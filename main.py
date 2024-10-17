from controller import main_controller
from controller.cv import get_cvs_in_db
from controller.main_controller import add_new_cv
from controller.settings import set_nlp_model
from model.db import create_tables
from view import main_view, settings_view, cv_view
from view.main_view import clear_screen


def main():
    while True:

        clear_screen()
        user_choice = main_view.main_menu()

        if user_choice == '1':
            # Start scraping
            clear_screen()
            print("Scrap in progress...")
            main_controller.get_data()

        if user_choice == '2':
            # CV menu

            clear_screen()
            user_cv_choice = cv_view.main_menu()

            if user_cv_choice == "1":
                # Current CV
                get_cvs_in_db()

            if user_cv_choice == "2":
                # Upload CV
                add_new_cv()
                main()

            if user_cv_choice == "0":
                main()

        if user_choice == '4':
            # Display settings menu

            clear_screen()
            user_settings_choice = settings_view.main_menu()

            if user_settings_choice == "3":
                # Initialize db
                create_tables()
                main()

            if user_settings_choice == "4":
                # Set NLP model
                set_nlp_model()
                main()

            if user_settings_choice == "0":
                main()

        if user_choice == "0":
            exit()


if __name__ == "__main__":
    main()
