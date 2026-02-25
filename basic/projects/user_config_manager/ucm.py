"""User Configuration Manager
Allow users to manage settings
N.B: Project completed from freeCodeCamp

Instructions:
    1. add_setting():
        - function should have two parameters (dict, tuple)
        - Convert key and value in tuple to lowercase
        - Check if the settings exists, if not add to the dict
    2. update_setting():
        - two parameters: dict of settings, tuple of key-values
        - Convert the key and value to lowercase
        - Check of the key setting exists and update, otherwise don't
    3. delete_setting():
        - parameters: dict of settings, key
        - Convert key to lowercase
        - Check if key is in dict and remove the pair, otherwise don't
    4. view_settings():
        - parameter: a dict of settings
        - Displays settings as a strings, or none if dict is empty
"""

def add_setting(settings: dict, pairs: tuple) -> str:
    """Add new settings to the object"""
    system_key = pairs[0].lower()
    system_value = None
    if isinstance(pairs[1], str):
        system_value = pairs[1].lower()
    else:
        system_value = pairs[1]

    # Check for key setting
    for key in settings:
        if key == system_key:
            return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[system_key] = system_value
    return f"Setting '{system_key}' added with value '{system_value}' successfully!"  

def update_setting(settings: dict, pairs: tuple) -> str:
    """Change a specific value in the object"""
    system_key = pairs[0].lower()
    system_value = None
    if isinstance(pairs[1], str):
        system_value = pairs[1].lower()
    else:
        system_value = pairs[1]

    # Check if key exists and update
    for key in settings:
        if key == system_key:
            settings[key] = system_value
            return f"Setting '{system_key}' updated to '{system_value}' successfully!"

    return f"Setting '{system_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key) -> str:
    """Delete items from the object using a specified key value"""
    system_key = key.lower()

    # Check if the key setting exists
    for item in settings:
        if item == system_key:
            settings.pop(system_key)
            return f"Setting '{system_key}' deleted successfully!"

    return 'Setting not found!'

def view_settings(settings: dict) -> str:
    """View the contents of a dicitionary object"""
    if len(settings) < 1:
        return 'No settings available.'

    contents = '''Current User Settings:\n'''
    for key, value in settings.items():
        contents += f'{key.capitalize()}: {value}\n'

    return contents

# Dictionaries of settings to test
test_settings = {'volume': 0, 'light': 'dim', 'theme': 'dark'}
print(delete_setting(test_settings, 'volume'))
