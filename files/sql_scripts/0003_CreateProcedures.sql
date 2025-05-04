# Only procedures expected to be consumed by application are createad

USE MealMasterDb;
DELIMITER //


-- Ingredient Procedures --
CREATE PROCEDURE IngredientCategorySelectAll ()
	BEGIN
		SELECT * FROM IngredientCategory ORDER BY Name ASC;
    END //
    
    
-- Messure Procedures --
CREATE PROCEDURE MessureSelectAll ()
	BEGIN
		SELECT m.Id, m.ShortName, m.FullName, m.RelativeSize, m.Type FROM Messure as m
			JOIN MessureType as mt ON m.MessureTypeId = mt.Id;
	END //


-- Nutrient Procedures --
CREATE PROCEDURE NutrientTypeSelectAll ()
	BEGIN
		SELECT 	nt.Id, nt.Name, nt.DisplayIndex, nt.Mandatory,
				m.Id, m.ShortName, m.FullName, m.RelativeSize, mt.Type
			FROM NutrientType AS nt
			JOIN Messure AS m ON nt.MessureId = m.Id
				JOIN Messuretype AS mt ON m.MessureTypeId = mt.id
			ORDER BY nt.DisplayIndex ASC;
	END //
    
-- Recipe Procedures --
CREATE PROCEDURE RecipeCategorySelectAll ()
	BEGIN
		SELECT * FROM RecipeCategory ORDER BY Name ASC;
	END //

CREATE PROCEDURE RecipeTypeSelectAll ()
	BEGIN
		SELECT * FROM RecipeType ORDER BY Name ASC;
	END //