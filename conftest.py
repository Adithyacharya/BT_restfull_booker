import pytest
import json
import os
from datetime import datetime
import configparser

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Add timestamp to report file name
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"



@pytest.fixture
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data


@pytest.fixture
def read_from_ini():
    """Fixture to read data from an INI file."""
    def _read(user, key, filename='data/test_data.ini'):
        """Helper function to read from the INI file."""
        config = configparser.ConfigParser()
        config.read(filename)

        # Check if the user section exists
        if config.has_section(user):
            try:
                # Return the value for the specified key
                return config.get(user, key)
            except KeyError:
                print(f"Key '{key}' not found for user '{user}' in the INI file.")
                return None  # Return None or any default value you prefer
        else:
            print(f"User '{user}' not found in the INI file.")
            return None  # Return None if user not found

    return _read