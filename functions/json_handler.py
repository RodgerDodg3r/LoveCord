import json
import os

def json_file_exists(path: str) -> bool:
    return os.path.exists(path)

def json_get_file_data(path: str = "") -> dict:
    if (not os.path.exists(path)):
        return {}
    with open(path, 'r') as file:
        try:
            return json.load(file)
        except Exception as error:
            print(f"An Error accoured while loading {path}: {error}")
            return {"error": error}

def json_save(path: str, data: dict):
    with open(path, "w") as file:
        try:
            json.dump(data, file, indent = 4)
        except Exception as error:
            print(f"An Error accoured while loading {path}: {error}")
            return
    
def json_set_value(key: str, value, data: dict):
    data[key] = value

def json_get_value(key: str, data: dict):
    if (key not in data):
        return
    return data[key]

def json_remove_value(key: str, data: dict):
    if (key not in data):
        return
    del data[key]

def json_add_value(key: str,value, data: dict):
    if (key in data):
        return
    data[key] = value

