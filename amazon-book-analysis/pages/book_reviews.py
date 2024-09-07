import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("./dataset/customer reviews.csv")
df_top100_books = pd.read_csv("./dataset/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Select a book", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = df_book["book price"].iloc[0]
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(f"{book_title}")
st.subheader(f"Genre: {book_genre}")
col1, col2, col3 = st.columns(3)
col1.metric("Price", f"${book_price:.2f}")
col2.metric("Rating", f"{book_rating:.2f}/5.0")
col3.metric("Year of Publication", book_year)
st.divider()

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])
