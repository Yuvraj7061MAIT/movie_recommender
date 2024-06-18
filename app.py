import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data = requests.get(url).json()
    # Use get method with a default value to handle potential missing 'poster_path' key
    poster_path = data.get('poster_path', '')
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

# Page Title
st.title("🎬 Movie Recommender System")
st.subheader("Discover personalized movie recommendations based on your preferences!")

# Movie Selection Dropdown
select_value = st.selectbox("Select a movie from the dropdown", movies_list, key="movie_dropdown")

# Recommendation Button
if st.button("Show Recommendations", key="recommend_button"):
    movie_name, movie_poster = recommend(select_value)
    
    # Recommendations Layout
    st.write("### Recommended Movies:")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0], use_column_width=True)

    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1], use_column_width=True)

    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2], use_column_width=True)

    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3], use_column_width=True)

    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4], use_column_width=True)

# Custom CSS Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
        }
        .st-Button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            border: none;
        }
        .st-Button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)
