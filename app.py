from flask import Flask, render_template, request
from recipe import Recipe
import requests

search_url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients'
ingredients_url = 'https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1003464/ingredientWidget.json'

API_KEY = "dbfe372d7cmsh162db6e20083938p19337fjsn72173c08cc03"
API_HOST = "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"

header = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}

search_params = {
    "ingredients": "flour,sugar,apples"
}

ingredient_params = {
    "id": None
}

recipe_objects = []

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/recipes", methods=['POST'])
def find_recipes():
    ingredients = request.form.get("ingredients")
    search_params["ingredients"] = ingredients
    recipe_list_data = requests.get(search_url, headers=header, params=search_params).json()
    
    for recipe in recipe_list_data:    
        recipe_obj = Recipe(recipe['id'], recipe['title'], recipe['image'])
        recipe_objects.append(recipe_obj)
    
    return render_template("index.html", recipe_list=recipe_objects)

@app.route("/<int:recipe_id>/<recipe_name>")
def get_recipe(recipe_id, recipe_name):
    ingredient_params["id"] = recipe_id
    print(recipe_name)
    # print(recipe_image)
    # requested_recipe = None
    recipe_data = requests.get(ingredients_url, headers=header, params=ingredient_params).json()
    recipe_ingredients = recipe_data["ingredients"]
    return render_template("recipe.html", ingredients=recipe_ingredients, name=recipe_name)


# @app.route("/ingredients", methods=['GET','POST'])
# def recipe():
#     name = request.args.get("food-title")
    
#     return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)