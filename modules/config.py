import os

# root folder for files
FILE_ROOT = os.path.join(os.getcwd(), "files")

# Folder paths
CSV_FOLDER = os.path.join(FILE_ROOT, "csv")
SCRIPTS_FOLDER = os.path.join(FILE_ROOT, "sql_scripts" )

# Script paths
FOOD_FILE_JSON = os.path.join(FILE_ROOT, "source", "foods.json")
NUTRIENTS_FILE_JSON = os.path.join(FILE_ROOT, "source", "nutrients.json")
QUICKADD_FILE_JSON = os.path.join(FILE_ROOT, "misc", "quickadd.json")

# Respect the loadorder, data is dependent...
CSV_LOADORDER = [
    "messure",

    "ingredient",
    "ingredientcategory",
    "ingredient_ingredientcategory",
    "nutrientsource",
    "nutrienttype",
    "nutrientingredient",

    "recipetype",
    "recipecategory",
    "recipe",
    "recipesource",
    "recipeingredient",
    "recipestep",
    "recipe_recipecategory",
    "recipe_recipetype",
]