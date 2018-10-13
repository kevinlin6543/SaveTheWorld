#import spoonacular as sp

#api = sp.API("u7pl8nuLUymsh3I6GLbaunBr0krep1qNZJSjsnoGMIKjmUx1Da")
#response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1)
#data = response.json()
#response = api.search_recipes_by_ingredients(ingredients=data[0])
#data = response.json()
#print(data[0]['name'])
import requests
ingredients = "apples%2Cflour%2Csugar"
response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?ingredients=" + ingredients + "&number=5&ranking=1",
  headers={
    "X-Mashape-Key": "anjVTvmAtYmshU4QajQrWhAVY2RWp1Efq2vjsnOXbjSNxYJ4OX"
  }
)
print(response.text)

