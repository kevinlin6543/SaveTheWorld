import requests


def search_recipe_by_ingredients(ingredients, fill_ingredients=False, number=5, ranking=1):
    ingredients_str = ''
    ingredients_str += '%2C'.join(x for x in ingredients)
    print(ingredients_str)
    if fill_ingredients:
        fill_ingredients_str = 'true'
    else:
        fill_ingredients_str = 'false'
    send_msg = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?fillIngredients="+\
               fill_ingredients_str+"&ingredients="+ingredients_str+"&limitLicense=false&number="+str(number)+\
               "&ranking="+str(ranking)
    return send_msg


message = search_recipe_by_ingredients(['apples', 'flour', 'sugar'])
response = requests.get(message, headers={
    "X-Mashape-Key": "Hx9ZEyctAlmshCVPDIp1VEN8bUstp15VNYtjsnoi0BfLWP2yUF",
    "Accept": "application/json"
  }
)
print(response.text)

'''response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?fillIngredients=false&ingredients=apples%2Cflour%2Csugar&limitLicense=false&number=5&ranking=1",
  headers={
    "X-Mashape-Key": "Hx9ZEyctAlmshCVPDIp1VEN8bUstp15VNYtjsnoi0BfLWP2yUF",
    "Accept": "application/json"
  }
)'''