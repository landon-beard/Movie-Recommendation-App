from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import os
import time
import random

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TMDB_API_KEY = '' # Replace with your actual TMDb API key

def get_movie_data(genre):
    # Adjust the total_pages based on your knowledge of available pages for the genre
    total_pages = 1000
    movies_per_page = 20
    target_recommendations = 8

    selected_movies = []

    while len(selected_movies) < target_recommendations:
        random_page = random.randint(1, total_pages)

        url = 'https://api.themoviedb.org/3/discover/movie'
        params = {
            'api_key': TMDB_API_KEY,
            'language': 'en-US',
            'sort_by': 'popularity.desc',
            'include_adult': 'false',
            'include_video': 'false',
            'with_genres': genre,
            'page': random_page,
            'per_page': movies_per_page,
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json().get('results', [])

            # Randomly select unique movies from the results
            selected_movies.extend(random.sample(data, min(target_recommendations - len(selected_movies), len(data))))
        else:
            print(f"Failed to fetch movie data. Status code: {response.status_code}")
            print(response.content)  # Print the response content for debugging
            break

    return selected_movies



def get_tmdb_link(movie_id):
    return f'https://www.themoviedb.org/movie/{movie_id}'

# Make the get_tmdb_link function available in templates
app.add_template_global(get_tmdb_link, 'get_tmdb_link')

# Route to handle both GET and POST requests for movie recommendations
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    print("Accessed /recommend route")
    if request.method == 'POST':
        # Handle the POST request to get movie recommendations
        user_input_genre = request.form.get('genre')
        movie_data = get_movie_data(user_input_genre)

        # Filter movies with a user score higher than 3/10
        movie_data = [movie for movie in movie_data if movie.get('vote_average', 0) > 3]

        # Ensure that only 8 movies are selected
        movie_data = movie_data[:8]

        # Construct recommendations list with title, TMDb link, and image URL
        recommendations = []
        for movie in movie_data:
            title = movie.get('title')
            tmdb_link = get_tmdb_link(movie.get('id'))
            poster_path = movie.get('poster_path')

            # Additional check for user_score to avoid 'None' values
            user_score = movie.get('vote_average', None)

            # Construct the full image URL
            base_url = 'https://image.tmdb.org/t/p/w500'  # Adjust the size as needed
            image_url = f'{base_url}{poster_path}' if poster_path else None

            # Append the tuple to the recommendations list
            recommendations.append((title, tmdb_link, image_url, user_score))

        print(recommendations)  # Print recommendations to check if it's correct

        # Modified to pass dark_mode_enabled to the template
        dark_mode_enabled = request.cookies.get('dark_mode_enabled', 'false') == 'true'
        return render_template('recommend.html', recommendations=recommendations, dark_mode_enabled=dark_mode_enabled)

    # Modified to pass dark_mode_enabled to the template
    dark_mode_enabled = request.cookies.get('dark_mode_enabled', 'false') == 'true'
    return render_template('index.html', dark_mode_enabled=dark_mode_enabled)



#Bad Moives
@app.route('/recommend_low_rating', methods=['POST'])
def recommend_low_rating():
    # Fetch a random page between 1 and 500 (inclusive)
    random_page = random.randint(1, 500)

    # TMDb API request for movies with a rating between 0.5 and 2
    url = 'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'sort_by': 'vote_average.asc',  # Sort by ascending rating
        'include_adult': 'false',
        'include_video': 'false',
        'vote_average.lte': 2,  # Movies with rating 2 stars or below
        'vote_average.gte': 0.5,  # Movies with rating 0.5 stars or above
        'page': random_page,
        'per_page': 1,  # Fetch only 1 movie
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json().get('results', [])

        # Check if there is at least one movie with a low rating
        if data:
            movie = data[0]
            title = movie.get('title')
            tmdb_link = get_tmdb_link(movie.get('id'))
            poster_path = movie.get('poster_path')

            # Retrieve user score, and handle None or 0 case
            user_score = movie.get('vote_average', 0)

            # Construct the full image URL
            base_url = 'https://image.tmdb.org/t/p/w500'  # Adjust the size as needed
            image_url = f'{base_url}{poster_path}' if poster_path else None

            # Inside the recommend_low_rating route
            return render_template('bad_movies.html', low_rated_movies=[(title, tmdb_link, image_url, user_score)])
        else:
            # No low-rated movies found
            return render_template('no_recommendation.html', page_type='Trash Movie of the Day')

    else:
        print(f"Failed to fetch movie data. Status code: {response.status_code}")
        print(f"Response content: {response.content}")
        return render_template('error.html', status_code=response.status_code)




# Route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)