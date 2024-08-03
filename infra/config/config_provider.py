import os
import configparser
from pathlib import Path

# Initialize configuration dictionaries
configuration = {}
slas = {}

# Get the path to the config.ini file
path = Path(__file__).parent
config_file_path = path / "../../config.ini"

def init_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    config_sections_list = config.sections()
    for config_section in config_sections_list:
        for key in config[config_section]:
            configuration[key] = config[config_section][key]

# Call the function to initialize the configuration
init_config(config_file_path)