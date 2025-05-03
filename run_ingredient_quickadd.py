from alive_progress import alive_bar
from modules.config import *
from modules.filemanager import read_json_file
from modules.inserter.IngredientDataset import IngredientDataset

print("\n")

data = read_json_file(QUICKADD_FILE_JSON)
l = len(data)

with alive_bar(l) as bar:

    exist = 0
    new = 0
    error = 0
    
    for d in data:
        food = IngredientDataset(d[0], d[1], d[2])
        res = food.insert_to_db(logging=False)
        if res == 0: exist += 1
        if res == 1: new += 1
        if res == 2: error += 1
        bar()


print(f"""\n
    Ingredienser i database: {exist}
    Lagt til fra fil:. ..... {new}
    Error ved insert: ...... {error}\n""")