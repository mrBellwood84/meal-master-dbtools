import os

ROOT = os.getcwd()
CSV_FOLDER = os.path.join(ROOT, "files", "csv")

FOOD_FILE_JSON = os.path.join(ROOT, "files", "source" "foods.json")
NUTRIENTS_FILE_JSON = os.path.join(ROOT, "files", "source", "nutrients.json")

# Respect the loadorder, data is dependent...
CSV_LOADORDER = [
    "messuretype",
    "messure",
    "sourcetype",
    "nutrienttype",
    "ingredientcategory",
    "recipecategory",
    "recipecontinentorgin",
    "recipecountryorgin",
]