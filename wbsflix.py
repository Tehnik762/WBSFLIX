import streamlit as st
import pandas as pd
import joblib
from functions import search_movies


popular10 = joblib.load('./ml-latest-small/ten')
film_r = joblib.load('./ml-latest-small/matrix10')
user_db = joblib.load('./ml-latest-small/user_db')

st.title('Top 10 Movies of all the time')

st.dataframe(popular10[["Movie", "Rating"]], hide_index=True)

st.title('Choose a film - and then look for similar ones!')
data = pd.read_csv('./ml-latest-small/movies.csv')
query = st.text_input('Type here movie name', '')

results = search_movies(data, query)
if results.empty:
    st.write('Nothing found')
else:
    st.write('Search results:')
    selected_movie_id = st.selectbox('Choose a movie', results['movieId'],
                                     format_func=lambda x: results[results['movieId'] == x]['title'].values[0],
                                    index=None)
    if selected_movie_id:
        st.write("Similar films:")
        temp = film_r[selected_movie_id]
        for step in temp:
            st.write(data.loc[data.movieId == step, "title"].values[0])

st.title('And if you are a user - you can look for suggestions for you!')
query2 = st.text_input('Type your id', '')

if query2 != '':
    query2 = int(query2)

    if query2 in user_db.keys():
        st.write("Here are our suggestions:")
        temp = user_db[query2]
        for movie_id in temp:
            st.write(data.loc[data.movieId == movie_id, "title"].values[0])
    else:
        st.write("User not found")
