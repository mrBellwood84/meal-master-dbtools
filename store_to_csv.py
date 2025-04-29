"""
This script stores all tables from database to csv file. 
Will only add new lines of data to file.
Delete files in "./files/csv/" for clean backup files...
"""

import os
from modules.config import CSV_FOLDER, CSV_LOADORDER 
from modules.filemanager import read_csv_file, write_csv_file
from modules.sql import db_query


for name in CSV_LOADORDER:

    existing_data = []
    csv_file_path = os.path.join(CSV_FOLDER, f"{name}.csv")
    csv_file_exist = os.path.exists(csv_file_path)

    if csv_file_exist:
        with open(csv_file_path, "r", newline="") as file:
            existing_data = read_csv_file(csv_file_path)

    column_query = f"show columns from {name}"
    col_name = db_query(column_query)
    col_name = [x[0] for x in col_name]

    data_query = f"select * from {name}"
    data = db_query(data_query)

    if col_name not in existing_data:
        existing_data = [col_name] + existing_data

    ids = [x[0] for x in existing_data[1:]]

    for row in data:
        if row[0] not in ids:
            existing_data.append(row)
    
    write_csv_file(csv_file_path, existing_data)

