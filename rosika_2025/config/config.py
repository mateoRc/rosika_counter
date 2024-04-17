import logging


class Configuration():
    config = None

    @staticmethod
    def load():
        print("config loading...")
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        # TODO: load config file
