import csv, json

def read_json_file(path: str):
    with open(path, "r") as file:
        data = file.read()
        return json.loads(data)


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


def read_sql_file(path:str):
    with open(path, "r") as file:
        script = file.read()
        return script