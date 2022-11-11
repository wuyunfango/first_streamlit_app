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

# makeing a pick list here so customers can pick the fruits for smoothie
streamlit.multiselect("Pick some fruits:", list(my_fruit_list))

# display the table on the page
streamlit.dataframe(my_fruit_list)
