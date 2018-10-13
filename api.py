import requests
import json


def get_recipe(recipe_id):
    request = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/" + str(recipe_id) + \
              "/information?includeNutrition=false"
    return request


def convert_units(unit, name, amt):
    unit_resp = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/convert?"
                             "ingredientName=" + name + "&sourceAmount=" + str(amt) + "&sourceUnit=" + unit +
                             "&targetUnit=grams",
                             headers={
                                    "X-Mashape-Key": "anjVTvmAtYmshU4QajQrWhAVY2RWp1Efq2vjsnOXbjSNxYJ4OX",
                                }
                             )
    gram_ing = json.loads(unit_resp.text)
    return gram_ing['targetAmount']


def get_ingredients(req):
    json_data = json.loads(req.text)
    i = 0
    print(json_data['sourceUrl'])
    j = json_data['extendedIngredients']
    while i < len(j):
        if j[i]['unit']:
            print(str(convert_units(j[i]['unit'], j[i]['name'], j[i]['amount'])) + " " + j[i]['unit'] + " of " + j[i]['name'])
            # print(str(j[i]['amount']) + " " + j[i]['unit'] + " of " + j[i]['name'])
        else:
            print(str(j[i]['amount']) + " " + j[i]['name'])
        i += 1


def get_recipe_steps(req):
    json_data = json.loads(req.text)
    x = 0
    if json_data['analyzedInstructions']:
        j = json_data['analyzedInstructions'][0]['steps']
        while x < len(j):
            print(str(j[x]['number']) + ": " + j[x]['step'])
            x += 1
    # print(json_data['instructions'])


def search_recipe_by_ingredients(ingredients, fill_ingredients=False, number=10, ranking=1):
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


def title_to_id(response_msg):
    response_list = json.loads(response_msg.text)
    response_dic = {}
    for x in response_list:
        response_dic[x['title']] = x['id']
    return response_dic


# def print_recipe(ing):
