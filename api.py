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
    ingred = []
    i = 0
    if json_data['analyzedInstructions']:
        print(json_data['sourceUrl'])
        j = json_data['extendedIngredients']
        while i < len(j):
            if j[i]['unit']:
                ingred.append({j[i]['name']: [j[i]['amount'], j[i]['unit']]})
                print(str(j[i]['amount']) + " " + j[i]['unit'] + " of " + j[i]['name'])
            else:
                ingred.append({j[i]['name']: [j[i]['amount'], ""]})
                print(str(j[i]['amount']) + " " + j[i]['name'])
            i += 1
    return ingred


def get_recipe_steps(req):
    json_data = json.loads(req.text)
    x = 0
    if json_data['analyzedInstructions']:
        j = json_data['analyzedInstructions'][0]['steps']
        while x < len(j):
            print(str(j[x]['number']) + ": " + j[x]['step'])
            x += 1
        print("********************************************************************************")


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


def compare_quantity(user_input, server_input):
    server_name_list = []
    user_name_list = []
    valid_dic = {}
    for key, value in server_input:
        server_name_list += key
    for key, value in user_input:
        user_name_list += key
    contain_flag = False
    for x in user_name_list:
        for y in server_name_list:
            if x in y:
                contain_flag = True
                break
        if contain_flag:
            valid_dic[y] = server_input[y]
    print(valid_dic)


def struct_user_dic(user_ingredients, user_quantities):
    user_input = {}
    for x in range(len(user_ingredients)):
        try:
            user_input[user_ingredients[x]] = int(user_quantities[x])
        except ValueError:
            user_input[user_ingredients[x]] = 0
    return user_input
