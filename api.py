import requests
import json

def get_recipe(recipe_id):
    request = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/" + str(recipe_id) + \
              "/information?includeNutrition=false"
    return request


def get_ingredients(req):
    json_data = json.loads(req.text)
    i = 0
    j = json_data['extendedIngredients']
    while i < len(j):
        print(str(j[i]['amount']) + " " + j[i]['unit'] + " of " + j[i]['name'])
        # print(j[i]['originalString'])
        i += 1


def get_recipe_steps(req):
    json_data = json.loads(req.text)
    i = 0
    j = json_data['analyzedInstructions'][0]['steps']
    # print(j[1]['step'])
    while i < len(j):
        print(str(j[i]['number']) + ": " + j[i]['step'])
        i += 1
    # print(json_data['instructions'])


r = requests.get(get_recipe(479101),
                 headers={
                     "X-Mashape-Key": "anjVTvmAtYmshU4QajQrWhAVY2RWp1Efq2vjsnOXbjSNxYJ4OX"
                 }
                 )

get_ingredients(r)
get_recipe_steps(r)
