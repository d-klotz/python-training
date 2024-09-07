import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Top 100 Trending Books in Amazon")

df_reviews = pd.read_csv("./dataset/customer reviews.csv")
df_top100_books = pd.read_csv("./dataset/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.title("Book Reviews").slider("Price Range", price_min, price_max, price_max)

df_books = df_top100_books[df_top100_books["book price"] <= max_price]

df_books

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)