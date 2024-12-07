import os
import json

DATA = {"counter": 0,"n":1,"o":"+"}

def read_json_file(file_path):
    """
    Reads data from a JSON file. If the file does not exist, it creates it with {"counter": 0}.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        # If file does not exist, create it and write {"counter": 0}
        with open(file_path, "w") as file:
            json.dump(DATA, file)
    else:
        # If file exists, read from it
        with open(file_path, "r") as file:
            data = json.load(file)

    return DATA


def update_json_file(file_path, update_value):
    """
    Updates the "counter" value in the JSON file.
    """

    # Write the updated data back to the file
    with open(file_path, "w") as file:
        json.dump(update_value, file)

# 初始化文件
def reset_json_file(file_path):
    """
    Reads data from a JSON file. If the file does not exist, it creates it with {"counter": 0}.
    """
    # Check if the file exists=
        # If file does not exist, create it and write {"counter": 0}
    os.remove(file_path)