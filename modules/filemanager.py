import csv, json, os
from modules.config import *

def read_json_file(path: str):
    with open(path, "r") as file:
        data = file.read()
        return json.loads(data)


def write_json_file(path:str, data: list[dict]):
    with open(path, "w") as file:
        data = json.dumps(data, indent=2)
        file.write(data)

def read_csv_file(path:str):
    with open(path, "r", newline="") as file:
        result = []
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0:
                result.append(row)
        return result
    
def write_csv_file(path:str, data:list):
    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def add_to_quickadd(name, index, c_index):
    data = []
    if os.path.exists(QUICKADD_FILE_JSON): data = read_json_file(QUICKADD_FILE_JSON)
    data.append([name, index, c_index])
    write_json_file(QUICKADD_FILE_JSON, data)