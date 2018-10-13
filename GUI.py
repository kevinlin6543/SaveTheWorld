import kivy
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import api
import requests
# from kivy.properties import ObjectProperty

import io
import os
import argparse

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
# from google.cloud import storage

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/kevin/Desktop/HackCooper2018-f61123ce506b.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()
ing = "tmp"
ingredientlayout = BoxLayout(orientation='vertical', padding=15, spacing=15)
mainbutton1 = Button(text='Label')
ingredients = []


class Screen1(Screen):
        def __init__(self, **kwargs):
            super(Screen1, self).__init__(**kwargs)
            submitbtn = Button(text='Submit Recipe')
            submitbtn.bind(on_press=self.submitRecipe)
            ingredientlayout.add_widget(submitbtn)
            addIng = Button(text='Add Ingredient')
            ingredientlayout.add_widget(addIng)
            addIng.bind(on_press=self.changer)
            self.add_widget(ingredientlayout)

        def changer(self, *args):
            self.manager.current = 'screen2'


        def submitRecipe(self, *args):
            # for ingredient in ingredients:
            #     print(ingredient)
            r = requests.get(api.search_recipe_by_ingredients(ingredients),
                             headers={
                                 "X-Mashape-Key": "anjVTvmAtYmshU4QajQrWhAVY2RWp1Efq2vjsnOXbjSNxYJ4OX"
                             }
                             )
            test = api.title_to_id(r)
            # id_list = list(test.values())
            for key, value in test.items():
                req_id = requests.get(api.get_recipe(value),
                                      headers={
                                          "X-Mashape-Key": "anjVTvmAtYmshU4QajQrWhAVY2RWp1Efq2vjsnOXbjSNxYJ4OX"
                                      }
                                      )
                api.get_ingredients(req_id)
                api.get_recipe_steps(req_id)


class Screen2(Screen):

    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        file_name = 'C:/Users/kevin/Documents/HackCooper/hotdog.png'

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        mainlayout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        wimg = Image(source=file_name)
        mainlayout.add_widget(wimg)

        layout = BoxLayout()

        dropdown1 = DropDown()
        for inglabel in labels:

            btn = Button(text='%s' % inglabel.description, size_hint_y=None, height=44)

            btn.bind(on_release=lambda btn: dropdown1.select(btn.text))

            dropdown1.add_widget(btn)

        # create a big main button
        labelinput = TextInput(size_hint_y=None, height=44)
        labelinput.bind(on_double_tap=lambda labelinput: dropdown1.select(labelinput.text))
        dropdown1.add_widget(labelinput)
        mainbutton1.bind(on_release=dropdown1.open)
        dropdown1.bind(on_select=lambda instance, x: setattr(mainbutton1, 'text', x))
        layout.add_widget(mainbutton1)

        textinput = TextInput()
        layout.add_widget(textinput)

        dropdown2 = DropDown()

        btn2 = Button(text='oz', size_hint_y=None, height=44)
        btn2.bind(on_release=lambda btn2: dropdown2.select(btn2.text))
        dropdown2.add_widget(btn2)
        btn3 = Button(text='g', size_hint_y=None, height=44)
        btn3.bind(on_release=lambda btn3: dropdown2.select(btn3.text))
        dropdown2.add_widget(btn3)
        btn4 = Button(text='fl oz', size_hint_y=None, height=44)
        btn4.bind(on_release=lambda btn4: dropdown2.select(btn4.text))
        dropdown2.add_widget(btn4)
        btn5 = Button(text='# of items', size_hint_y=None, height=44)
        btn5.bind(on_release=lambda btn5: dropdown2.select(btn5.text))
        dropdown2.add_widget(btn5)

        # create a big main button
        mainbutton2 = Button(text='Units')
        mainbutton2.bind(on_release=dropdown2.open)
        dropdown2.bind(on_select=lambda instance, x: setattr(mainbutton2, 'text', x))
        layout.add_widget(mainbutton2)

        mainlayout.add_widget(layout)

        sendbtn = Button(text="Add Ingredient")
        sendbtn.bind(on_press=self.changer)
        mainlayout.add_widget(sendbtn)

        self.add_widget(mainlayout)

    def changer(self,*args):
        labelx = Label(text=mainbutton1.text)
        ingredients.append(mainbutton1.text)
        ingredientlayout.add_widget(labelx)
        ingredientlayout.do_layout()
        self.manager.current = 'screen1'


class TestApp(App):

        def build(self):
            my_screenmanager = ScreenManager()
            screen1 = Screen1(name='screen1')
            screen2 = Screen2(name='screen2')
            my_screenmanager.add_widget(screen1)
            my_screenmanager.add_widget(screen2)
            my_screenmanager.current='screen1'
            return my_screenmanager


if __name__ == '__main__':
    TestApp().run()


