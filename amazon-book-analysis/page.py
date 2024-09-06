import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("./dataset/customer reviews.csv")
df_top100_books = pd.read_csv("./dataset/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.title("Book Reviews").slider("Price Range", price_min, price_max, price_max)

df_top100_books[df_top100_books["book price"] <= max_price]