def query_food_data(data: list[dict], foodName: str):
    print(f"SØK: \"{foodName}\"\n")
    for i,v in enumerate(data):
        if foodName.lower() in v["foodName"].lower():
            print(f"{i}: {v["foodName"]}")

def enumerate_category_ingredients(data: list[tuple]):
    print("KATEGORIER FOR INGREDIENSER:\n")
    for i,v in enumerate(data):
        if (i+1) % 5 == 0:
            print("{:>2}: {}".format(i,v[1]))
            continue
        print("{:>2}: {:20}".format(i,v[1]), end="")

def input_ingredient_index(min:int, max:int, name:str):
    text = "Sett index for \"{}\"".format(name)
    anwser = int(input(text))
    if anwser < min or anwser > max: 
        raise Exception("Ingrediens index is out of range")
    return anwser

def input_ingredient_name(queryName:str, dataName:str):
    text = "Sett navn for \"{}\". La stå for: \"{}\"".format(dataName, queryName)
    return input(text)

def input_ingredientcategory_index(min:int, max:int, name:str):
    text = "Sett indeks kategorier for \"{}\". Bruk komma dersom flere.".format(name)
    answer = input(text).split(",")
    answer = [int(x) for x in answer]
    for a in answer:
        if a < min or a > max:raise Exception("Ingredienskategori is out of range!")
    return answer
    

