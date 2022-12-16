import streamlit
import pandas
streamlit.title('Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text(' 🥣Omega3 & Blueberry Oatmeal')
streamlit.text(' 🥗Kale,SPinach & Rocket Smoothie')
streamlit.text(' 🐔Hard Boiled Free Range Eggs')
streamlit.text('🥑🍞Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
