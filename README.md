# 🎬 Movie Recommender System

Welcome to the **Movie Recommender System**! This project provides personalized movie recommendations using a content-based filtering approach, leveraging the similarities between movies based on their genres and overviews. The system allows users to select a movie and get top 5 recommendations along with movie posters.

## 🚀 Features

- **Movie Recommendations**: Get personalized movie suggestions based on a selected movie.
- **Movie Posters**: Display movie posters for each recommended movie.
- **Streamlit Web Interface**: A user-friendly interface built with Streamlit for seamless user experience.
- **Cosine Similarity Algorithm**: The recommendation system uses cosine similarity to find similar movies.

## 🛠️ Tech Stack

- **Python**: Core language used.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: Used for feature extraction and cosine similarity computation.
- **Pickle**: For saving and loading pre-trained models and data.
- **TMDb API**: For fetching movie posters using the movie ID.
- **Streamlit**: For building the web interface.

## 📚 Dataset

The dataset contains details about movies, such as:
- **id**: Unique identifier for each movie.
- **title**: The name of the movie.
- **tags**: A combination of movie overview and genre.
  
This dataset is preprocessed and used to create a content-based recommendation model.

## 📦 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/movie-recommender-system.git
    cd movie-recommender-system
    ```

2. **Install dependencies**:
    Install the required libraries using the following command:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download the Dataset**:
    Place the preprocessed `movies_list.pkl` and `similarity.pkl` files into your project directory.

4. **Run the application**:
    Launch the Streamlit app using the following command:
    ```bash
    streamlit run app.py
    ```

5. **Access the Application**:
    Once the app starts, access it at `http://localhost:8501/` in your browser.

## 🔧 Usage

1. **Select a Movie**: From the dropdown, select a movie you'd like recommendations for.
2. **Show Recommendations**: Click on the "Show Recommendations" button.
3. **View Results**: The top 5 recommended movies will be displayed along with their posters.

## 📂 Files

- **app.py**: Main application file containing the Streamlit interface and recommendation logic.
- **movies_list.pkl**: Preprocessed list of movies.
- **similarity.pkl**: Pre-computed similarity matrix using cosine similarity.
- **requirements.txt**: List of dependencies for the project.

## 🌟 Acknowledgements

- The Movie Database (TMDb) for providing the movie posters via their API.
- Scikit-learn for the cosine similarity algorithm.

## 📧 Contact

For any questions or feedback, feel free to reach out:

- **Email**: yuvraj.singh.mait@gmail.com
- **GitHub**: [Yuvraj7061MAIT](https://github.com/Yuvraj7061MAIT)
