import json
import yaml
import os

def load_configuration(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The specified configuration file does not exist: {config_path}")

    try:
        if config_path.endswith('.json'):
            with open(config_path, 'r') as file:
                return json.load(file)
        elif config_path.endswith(('.yaml', '.yml')):
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported file format. Please provide a .json or .yaml file.")
    except IOError as e:
        raise IOError(f"Error opening file {config_path}: {str(e)}")
