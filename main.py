from controller.cv import get_cvs_in_db
from controller.job_board import get_current_job_board
from controller.main_controller import add_new_cv, get_data
from controller.scrapping_welcome_to import main_scrap
from controller.settings import set_nlp_model, set_job_board
from model.db import create_tables
from view import main_view, settings_view, cv_view
from view.main_view import clear_screen, no_job_board_settled


def main():
    while True:

        clear_screen()
        user_choice = main_view.main_menu()

        if user_choice == "9":

            main_scrap()

        if user_choice == '1':
            # Start scraping
            clear_screen()
            job_board_to_use = get_current_job_board()

            if not job_board_to_use:
                no_job_board_settled()
                set_job_board()
                job_board_to_use = get_current_job_board()

            if job_board_to_use == "welcome":
                print("Scrap Welcome to the Jungle in progress...")
                main_scrap()

            if job_board_to_use == "indeed":
                print("Scrap Indeed in progress...")
                get_data()

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

            if user_settings_choice == "1":
                # Select job board to scrap
                set_job_board()
                main()

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
