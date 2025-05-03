"""
Will only work on an empty database. 
Data from csv will highly likely contain duplicate values resulting in total failure ^^
"""

import os
from modules.config import CSV_FOLDER, CSV_LOADORDER 
from modules.filemanager import read_csv_file
from modules.sql import db_insert_many


for name in CSV_LOADORDER:

    existing_data = []
    csv_file_path = os.path.join(CSV_FOLDER, f"{name}.csv")
    csv_file_exist = os.path.exists(csv_file_path)

    if csv_file_exist:
        with open(csv_file_path, "r", newline="") as file:
            existing_data = read_csv_file(csv_file_path)

    col_names = existing_data[0]
    values = [tuple(x) for x in existing_data[1:]]

    db_insert_many(name, col_names, values)
    print(f"{len(values)} inserted in '{name}'")



    