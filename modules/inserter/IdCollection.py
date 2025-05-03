from modules.sql import db_query_single

class IdCollection:
    """Collection of Ids used to create and insert ingredients to database"""

    def __init__(self):
        self.messure_dl = db_query_single("select id from messure where shortname = 'dl'")[0]
        self.messure_skive = db_query_single("select id from messure where shortname = 'skive'")[0]
        self.messure_stk = db_query_single("select id from messure where shortname = 'stk'")[0]
        self.messure_g = db_query_single("select id from messure where shortname = 'g'")[0]
        self.nutrient_kj_id = db_query_single("select id from nutrienttype where name = 'energi'")[0]
        self.nutrient_kcal_id = db_query_single("select id from nutrienttype where name = 'kalorier'")[0]