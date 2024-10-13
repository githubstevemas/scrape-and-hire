from controller import main_controller
from view import main_view, settings_view


def main():

    while True:

        user_choice = main_view.main_menu()

        if user_choice == '1':
            print("Scrap in progress...")
            main_controller.get_data()

        if user_choice == '4':
            user_settings_choice = settings_view.main_menu()

            if user_settings_choice == "0":
                main()


if __name__ == "__main__":
    main()
