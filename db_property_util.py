# util/db_property_util.py
import configparser

class DBPropertyUtil:
    @staticmethod
    def get_db_connection_string(property_file):
        config = configparser.ConfigParser()
        config.read(property_file)
        
        try:
            return config['database']['connection_string']
        except KeyError as e:
            raise KeyError(f"Missing required configuration: {e}")
