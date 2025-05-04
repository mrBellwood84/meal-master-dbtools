from modules.inserter.DataCollection import DataCollection
from modules.inserter.IdCollection import IdCollection
from modules.sql import create_connetion, db_query_single
from uuid import uuid4


class IngredientDataset:
    """ Create values to be inserted in database """
    
    def __init__(self, name:str, food_index: int, category_index: list[int] ):
        self.name = name
        self.c_index = category_index
        self.index = food_index

        self.ids = IdCollection()
        self.data = DataCollection()

        self.food_item = self.data.foods[food_index]

        self.ingredient_entity = self._create_ingredient_entity()
        self.source_entity = self._create_source_entity()
        self.category_entities = self._create_category_entities()
        self.nutrient_entities = self._create_nutrient_entities()

        self.entities_exist = db_query_single(f"select * from nutrientsource where text = \"{self.source_entity["text"]}\"")

        self.ingredient_insert_command = self.__create_command("ingredient", self.ingredient_entity.keys())
        self.source_insert_command = self.__create_command("nutrientsource", self.source_entity.keys())
        self.category_insert_command = self.__create_command("ingredient_ingredientcategory", self.category_entities[0].keys())
        self.nutrient_insert_command = self.__create_command("nutrientingredient", self.nutrient_entities[0].keys())

    def _create_ingredient_entity(self):
        messure_id, ratio = self.__resolve_messure()

        return {
            "id": self.__gen_id(),
            "name": self.name.lower(),
            "volumeWeightRatio": ratio,
            "messureId": messure_id,
        }

    def _create_source_entity(self):
        return {
            "id": self.__gen_id(),
            "text": self.food_item["uri"],
            "ingredientId": self.ingredient_entity["id"],
            "sourceTypeId": db_query_single("select id from sourcetype where type = 'href'")[0]
        }
    
    def _create_category_entities(self):
        if not self.c_index: raise Exception("No category selected for this entity")
        result = []
        for i in self.c_index:
            result.append({
                "id": self.__gen_id(),
                "ingredientId": self.ingredient_entity["id"],
                "ingredientCategoryId": self.data.categories[i][0]
            })
        return result
    
    def _create_nutrient_entities(self):

        result = []
        n_data = [x for x in self.food_item["constituents"] if x["sourceId"] != "10" and x["quantity"] > 0]
        
        result.append({
            "id": self.__gen_id(),
            "ingredientId": self.ingredient_entity["id"],
            "nutrientTypeId": self.ids.nutrient_kj_id,
            "value": self.food_item["energy"]["quantity"]
        })

        result.append({
            "id": self.__gen_id(),
            "ingredientId": self.ingredient_entity["id"],
            "nutrientTypeId": self.ids.nutrient_kcal_id,
            "value": self.food_item["calories"]["quantity"]
        })

        for n in n_data:
            nt_id = [x for x in self.data.nutrients if x[4] == n["nutrientId"]][0][0]
            result.append({
            "id": self.__gen_id(),
            "ingredientId": self.ingredient_entity["id"],
            "nutrientTypeId": nt_id,
            "value": n["quantity"]          
            })
        
        return result

    def insert_to_db(self, logging:bool = True):

        if self.entities_exist:
            if logging: print(f"'{self.name}' already exist in database!")
            return 0
        
        with create_connetion() as connection:
            try:
                cursor = connection.cursor()
                cursor.execute(self.ingredient_insert_command, list(self.ingredient_entity.values()))
                cursor.execute(self.source_insert_command, list(self.source_entity.values()))
                cursor.executemany(self.category_insert_command, [list(x.values()) for x in self.category_entities])
                cursor.executemany(self.nutrient_insert_command, [list(x.values()) for x in self.nutrient_entities])
                connection.commit()
                if logging: print(f"'{self.name}' inserted to database")
                return 1
            except:
                if logging: print(f"'{self.name}' was not inserted due to error")
                return 2

    def __gen_id(self):
        return str(uuid4())
    
    def __resolve_messure(self):
        porsions = self.food_item["portions"]
        names = [x["portionName"] for x in porsions]
        
        if "desiliter" in names: 
            i = names.index("desiliter")
            return self.ids.messure_dl, porsions[i]["quantity"]
        
        if "stk" in names: 
            i = names.index("stk")
            return self.ids.messure_stk, porsions[i]["quantity"]
        
        if "skive" in names: 
            i = names.index("skive")
            return self.ids.messure_skive, porsions[i]["quantity"]
        
        return self.ids.messure_g, 1

    def __create_command(self, table_name:str, col_names:str):
        return f"insert into {table_name} ({", ".join(col_names)}) values ({", ".join(["%s" for _ in col_names])})" 
