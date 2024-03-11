import json
import os
from os.path import dirname, join, abspath

from jsonschema.validators import validate
from referencing import jsonschema


def get_filename(filename):
    # here is the directory of json_reader.py
    here = dirname(abspath(__file__))
    # Go up only one level from `here` to the project root (not two)
    project_root = dirname(here)
    # Construct the path to the filename in the config directory
    output = join(project_root, filename)
    return output


def get_config_data():
    filename = get_filename(os.path.join('config','config.json'))
    with open(filename, 'r') as file:
        config = json.load(file)
        validate_config(config)
        return config


def get_json(file):
    filename = get_filename(file)
    with open(filename, 'r') as file:
        config = json.load(file)
        return config


def validate_config(config_data):
    filename = get_filename(os.path.join('config','config_schema.json'))
    with open(filename, 'r') as file:
        schema_data = json.load(file)
    try:
        validate(instance=config_data, schema=schema_data)
    except jsonschema.exceptions.ValidationError as ve:
        raise ValueError(f"Configuration is invalid: {ve}")
