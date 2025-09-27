import streamlit as st
import pandas as pd

#load the saved dataframe
df = pd.read_csv('final_books_recommend.csv')

#Display the title of the app
st.title("Popularity Based Recommendation System")
st.subheader("Top 10 Recommend books")

#row1 five books images and title
col1,col2,col3,col4,col5  = st.columns(5)
for i,col in enumerate([col1,col2,col3,col4,col5]):
    if i<len(df):
        col.image(df.loc[i,'Image-URL-M'],width=100)
        col.markdown(f"**{df.loc[i,'Book-Title']}**")
        col.write(f"**Number of ratings: {df.loc[i, 'Number']:,}**")


#row1 five books images and title
col6,col7,col8,col49,col10  = st.columns(5)
for i,col in enumerate([col1,col2,col3,col4,col5]):
    if i+5<len(df):
        col.image(df.loc[i+5,'Image-URL-M'],width=100)
        col.markdown(f"**{df.loc[i+5,'Book-Title']}**")
        col.write(f"**Number of ratings: {df.loc[i+5, 'Number']:,}**")
