USE mealmasterdb;

INSERT INTO MessureType (id, type) VALUES
	(uuid(), "volum"),
	(uuid(), "vekt"),
    (uuid(), "enhet"),
    (uuid(), "energi");
    
INSERT INTO SourceType (id, type) VALUES
	(uuid(), "text"),
    (uuid(), "href");
    
INSERT INTO messure (id, fullname, shortname, relativesize, messuretypeid) VALUES
	(uuid(), "desiliter", "dl", 1, (select id from messuretype where type = "volum")),
    (uuid(), "liter", "l", 10, (select id from messuretype where type = "volum")),
    (uuid(),  "teskje", "ts", 0.05, (select id from messuretype where type = "volum")),
    (uuid(),  "spiseskje", "ss", 0.15, (select id from messuretype where type = "volum")),
    (uuid(),  "kilogram", "kg", 1000, (select id from messuretype where type = "vekt")),
    (uuid(),  "gram", "g", 1, (select id from messuretype where type = "vekt")),
    (uuid(),  "milligram", "mg", 0.01, (select id from messuretype where type = "vekt")),
    (uuid(),  "mikrogram", "µg", 0.0001, (select id from messuretype where type = "vekt")),
    (uuid(), "stykk", "stk", 1, (select id from messuretype where type = "enhet")),
    (uuid(),  "skive", "skive", 1, (select id from messuretype where type = "enhet")),
    (uuid(),  "kilojoule", "kJ", 1, (select id from messuretype where type = "energi")),
    (uuid(),  "kilokalorier", "kcal", 1, (select id from messuretype where type = "energi"));

INSERT INTO NutrientType(id, name, nutrientid, displayIndex, mandatory, messureid) VALUES
	(uuid(), "energi", "Energi", 1, 1, (select id from messure where shortname = "kJ")),
	(uuid(), "kalorier", "Kalori", 2, 1, (select id from messure where shortname = "kcal")),
	(uuid(), "fett", "Fett", 3, 1, (select id from messure where shortname = "g")),
	(uuid(), "- mettede fettsyrer", "Mettet", 4, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c12:0 (laurinsyre)", "C12:0Laurinsyre", 5, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c14:0 (myristinsyre)", "C14:0Myristinsyre", 6, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c16:0 (palmitinsyre)", "C16:0Palmitinsyre", 7, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c18:0 (stearinsyre)", "C18:0Stearinsyre", 8, 0, (select id from messure where shortname = "g")),
	(uuid(), "- transfettsyrer", "Trans", 9, 0, (select id from messure where shortname = "g")),
	(uuid(), "- enumettede fettsyrer", "Enumet", 10, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c16:1 sum (palmitoleinsyre)", "C16:1", 11, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c18:1 sum (oljesyre)", "C18:1", 12, 0, (select id from messure where shortname = "g")),
	(uuid(), "- flerumettede fettsyrer", "Flerum", 13, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c18:2n-6 (linolsyre)", "C18:2n-6Linolsyre", 14, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c18:3n-3 (alfalinolensyre)", "C18:3n-3AlfaLinolensyre", 15, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c20:3n-3 (eikosatriensyre)", "C20:3n-3Eikosatriensyre", 16, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c20:3n-6 (dihomo-gamma-linolensyre, dgla)", "C20:3n-6DihomoGammaLinolensyre", 17, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c20:4n-3 (eikosatetraensyre)", "C20:4n-3Eikosatetraensyre", 18, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c20:4n-6 (arakidonsyre)", "C20:4n-6Arakidonsyre", 19, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c20:5n-3 (eikosapentaensyre, epa)", "C20:5n-3Eikosapentaensyre", 20, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c22:5n-3 (dokosapentaensyre, dpa)", "C22:5n-3Dokosapentaensyre", 21, 0, (select id from messure where shortname = "g")),
	(uuid(), "-- c22:6n-3 (dokosaheksaensyre, dha)", "C22:6n-3Dokosaheksaensyre", 22, 0, (select id from messure where shortname = "g")),
	(uuid(), "- omega-3", "Omega-3", 23, 0, (select id from messure where shortname = "g")),
	(uuid(), "- omega-6", "Omega-6", 24, 0, (select id from messure where shortname = "g")),
	(uuid(), "- kolesterol", "Kolest", 25, 0, (select id from messure where shortname = "mg")),
	(uuid(), "karbohydrat", "Karbo", 26, 1, (select id from messure where shortname = "g")),
	(uuid(), "- kostfiber", "Fiber", 27, 0, (select id from messure where shortname = "g")),
	(uuid(), "- stivelse", "Stivel", 28, 0, (select id from messure where shortname = "g")),
	(uuid(), "- sukkerarter", "Mono+Di", 29, 0, (select id from messure where shortname = "g")),
	(uuid(), "- sukker, tilsatt", "Sukker", 30, 0, (select id from messure where shortname = "g")),
	(uuid(), "- sukker, fritt", "SUGAN", 31, 0, (select id from messure where shortname = "g")),
	(uuid(), "protein", "Protein", 32, 1, (select id from messure where shortname = "g")),
	(uuid(), "alkohol", "Alko", 33, 1, (select id from messure where shortname = "g")),
	(uuid(), "vann", "Vann", 34, 0, (select id from messure where shortname = "g")),
	(uuid(), "vitamin a (rae)", "Vit A", 35, 0, (select id from messure where shortname = "µg")),
	(uuid(), "vitamin a (re)", "Vit A RE", 36, 0, (select id from messure where shortname = "µg")),
	(uuid(), "- betakaroten", "B-karo", 37, 0, (select id from messure where shortname = "µg")),
	(uuid(), "- retinol", "Retinol", 38, 0, (select id from messure where shortname = "µg")),
	(uuid(), "vitamin d", "Vit D", 39, 0, (select id from messure where shortname = "µg")),
	(uuid(), "vitamin e", "Vit E", 40, 0, (select id from messure where shortname = "mg")),
	(uuid(), "vitamin b1 (tiamin)", "Vit B1", 41, 0, (select id from messure where shortname = "mg")),
	(uuid(), "vitamin b2 (riboflavin)", "Vit B2", 42, 0, (select id from messure where shortname = "mg")),
	(uuid(), "vitamin b3 (niacin)", "Niacin", 43, 0, (select id from messure where shortname = "mg")),
	(uuid(), "niacinekvivalenter", "NIAEQ", 44, 0, (select id from messure where shortname = "mg")),
	(uuid(), "vitamin b6 (pyridoksin)", "Vit B6", 45, 0, (select id from messure where shortname = "mg")),
	(uuid(), "vitamin b9 (folat)", "Folat", 46, 0, (select id from messure where shortname = "µg")),
	(uuid(), "vitamin b12 (kobalamin)", "Vit B12", 47, 0, (select id from messure where shortname = "µg")),
	(uuid(), "vitamin c (askorbinsyre)", "Vit C", 48, 0, (select id from messure where shortname = "mg")),
	(uuid(), "kalsium (ca)", "Ca", 49, 0, (select id from messure where shortname = "mg")),
	(uuid(), "kalium (k)", "K", 50, 0, (select id from messure where shortname = "mg")),
	(uuid(), "natrium (na)", "Na", 51, 0, (select id from messure where shortname = "mg")),
	(uuid(), "salt (nacl)", "NaCl", 52, 0, (select id from messure where shortname = "g")),
	(uuid(), "fosfor (p)", "P", 53, 0, (select id from messure where shortname = "mg")),
	(uuid(), "magnesium (mg)", "Mg", 54, 0, (select id from messure where shortname = "mg")),
	(uuid(), "jern (fe)", "Fe", 55, 0, (select id from messure where shortname = "mg")),
	(uuid(), "kobber (cu)", "Cu", 56, 0, (select id from messure where shortname = "mg")),
	(uuid(), "sink (zn)", "Zn", 57, 0, (select id from messure where shortname = "mg")),
	(uuid(), "selen (se)", "Se", 58, 0, (select id from messure where shortname = "µg")),
	(uuid(), "jod (i)", "I", 59, 0, (select id from messure where shortname = "µg"));

    
INSERT INTO IngredientCategory (id, name) VALUES 
	(uuid(), "belgvekst"),
    (uuid(), "bær"),
	(uuid(), "bakevarer"),
    (uuid(), "grønnsak"),
    (uuid(), "diverse"),
    (uuid(), "egg"),
    (uuid(), "fett"),
    (uuid(), "fisk"),
    (uuid(), "frukt"),
    (uuid(), "frø"),
    (uuid(), "fugl"),
    (uuid(), "korn"),
    (uuid(), "kjøtt"),
    (uuid(), "krydder"),
    (uuid(), "meieri"),
    (uuid(), "melk"),
    (uuid(), "nøtter"),
    (uuid(), "skalldyr"),
    (uuid(), "sukker"),
    (uuid(), "urter");

INSERT INTO RecipeCategory (id, name) VALUES
	(uuid(), "sunn"),
    (uuid(), "rask"),
    (uuid(), "familie"),
    (uuid(), "kos"),
    (uuid(), "gjester"),
    (uuid(), "tradisjon"),
    (uuid(), "grillmat");

INSERT INTO RecipeType (id, name) VALUES
	(uuid(), "bakst"),
	(uuid(), "dessert"),
    (uuid(), "drikke"),
	(uuid(), "forrett"),
	(uuid(), "frokost"),
    (uuid(), "kake"),
    (uuid(), "lunsj"),
    (uuid(), "middag"),
    (uuid(), "salat"),
	(uuid(), "suppe"),
    (uuid(), "saus"),
    (uuid(), "smårett"),
	(uuid(), "tapas"),
    (uuid(), "tilbehør");
    
    

    
