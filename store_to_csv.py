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

    csv_file_path = os.path.join(CSV_FOLDER, f"{name}.csv")

    column_query = f"show columns from {name}"
    col_name = db_query(column_query)
    col_name = [x[0] for x in col_name]

    data_query = f"select * from {name}"
    data = db_query(data_query)
    
    write_csv_file(csv_file_path, data)

