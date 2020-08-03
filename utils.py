import configparser


def information_parser(config_read):
    # Reading Configs
    config = configparser.ConfigParser()
    config.read(config_read)

    # Setting configuration values
    api_id = config["Telegram"]["api_id"]
    api_hash = config["Telegram"]["api_hash"]
    api_hash = str(api_hash)

    phone = config["Telegram"]["phone"]
    username = config["Telegram"]["username"]
    return tuple([phone, username, api_id, api_hash])
