from modules.config import *
from modules.filemanager import read_json_file
from modules.sql import db_query_many

class DataCollection:
    """ Collection of data needed to insert new ingredient itewms to database """

    def __init__(self):
        self.foods = read_json_file(FOOD_FILE_JSON)["foods"]
        self.nutrients = db_query_many("select * from nutrienttype")
        self.categories = db_query_many("select * from ingredientcategory order by name")