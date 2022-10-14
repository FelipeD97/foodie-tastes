recipe = {'id': 47890, 'title': 'Blackberry-Apple Pie Filling', 'image': 'https://spoonacular.com/recipeImages/47890-312x231.jpg', 'imageType': 'jpg', 'usedIngredientCount': 2, 'missedIngredientCount': 2, 'missedIngredients': [{'id': 9042, 'amount': 12.0, 'unit': 'oz', 'unitLong': 'ounces', 'unitShort': 'oz', 'aisle': 'Produce', 'name': 'blackberries', 'original': '1 (12-oz.) package frozen blackberries (2 cups)', 'originalName': 'package frozen blackberries (2 cups)', 'meta': ['frozen', '(2 cups)'], 'extendedName': 'frozen blackberries', 'image': 'https://spoonacular.com/cdn/ingredients_100x100/blackberries.jpg'}, {'id': 1001, 'amount': 0.5, 'unit': 'cup', 'unitLong': 'cups', 'unitShort': 'cup', 'aisle': 'Milk, Eggs, Other Dairy', 'name': 'butter', 'original': '1/2 cup butter', 'originalName': 'butter', 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg'}], 'usedIngredients': [{'id': 9003, 'amount': 3.0, 'unit': 'pounds', 'unitLong': 'pounds', 'unitShort': 'lb', 'aisle': 'Produce', 'name': 'apples', 'original': '3 pounds Braeburn apples', 'originalName': 'Braeburn apples', 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/apple.jpg'}, {'id': 1089003, 'amount': 3.0, 'unit': 'pounds', 'unitLong': 'pounds', 'unitShort': 'lb', 'aisle': 'Produce', 'name': 'granny smith apples', 'original': '3 pounds Granny Smith apples', 'originalName': 'Granny Smith apples', 'meta': [], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/grannysmith-apple.png'}], 'unusedIngredients': [], 'likes': 0}

for i in range(len(recipe["missedIngredients"])):
    name = recipe["missedIngredients"][i]["name"]
    amount = recipe["missedIngredients"][i]["amount"]
    unit = recipe["missedIngredients"][i]["unit"]
    print(f'{name}: {amount} {unit}')

for i in range(len(recipe["usedIngredients"])):
    name = recipe["usedIngredients"][i]["name"]
    amount = recipe["usedIngredients"][i]["amount"]
    unit = recipe["usedIngredients"][i]["unit"]
    print(f'{name}: {amount} {unit}')
    
    
ingredients = {}
for x in range(len(recipe["missedIngredients"])):
    ingredient_name = recipe["missedIngredients"][x]["name"]
    ingredient_amount = str(recipe["missedIngredients"][x]["amount"])
    ingredient_unit = recipe["missedIngredients"][x]["unit"]
    ingredients[ingredient_name] = ingredient_amount + " " + ingredient_unit
for y in range(len(recipe["usedIngredients"])):   
    ingredient_name = recipe["usedIngredients"][y]["name"]
    ingredient_amount = str(recipe["usedIngredients"][y]["amount"])
    ingredient_unit = recipe["usedIngredients"][y]["unit"]
    ingredients[ingredient_name] = ingredient_amount + " " + ingredient_unit
    