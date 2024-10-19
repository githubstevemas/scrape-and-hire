import configparser

config = configparser.ConfigParser()


def get_current_job_board():
    # Read config ini file and return current job board

    config.read('config.ini')
    job_board_to_scrap = config['UserPreferences']['job_board_to_scrap']

    return job_board_to_scrap


def set_config_job_board(job_board):
    # Set job board name in config ini file

    config.read('config.ini')
    config['UserPreferences']['job_board_to_scrap'] = job_board

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
