"""
This script stores all tables from database to csv file. 
Will only add new lines of data to file.
Delete files in "./files/csv/" for clean backup files...
"""

import os
from alive_progress import alive_bar
from modules.config import CSV_FOLDER, CSV_LOADORDER 
from modules.filemanager import read_csv_file, write_csv_file
from modules.sql import db_query_single, db_query_many

print("\n")

l = len(CSV_LOADORDER)
with alive_bar(l) as bar:

    for name in CSV_LOADORDER:

        csv_file_path = os.path.join(CSV_FOLDER, f"{name}.csv")

        column_query = f"show columns from {name}"
        col_name = db_query_many(column_query)
        col_name = [x[0] for x in col_name]

        data_query = f"select * from {name}"
        data = db_query_many(data_query)
        data.insert(0, col_name)
        
        write_csv_file(csv_file_path, data)
        bar()

print("\n")