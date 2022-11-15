import streamlit

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.text("🫐 Omega 3 & Blueberrt Oatmeal")
streamlit.text("🥙 Kale, Spinich & Rocket Smoothie")
streamlit.text("🥚 Hard-Boiled Free-Range Egg")
streamlit.text("🥑 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

# makeing a pick list here so customers can pick the fruits for smoothie, adding an example choice of smoothie
fruits_selected =streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado","Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvivce api response
streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# formating json response to display
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output the json response in a table
streamlit.dataframe(fruityvice_normalized)
