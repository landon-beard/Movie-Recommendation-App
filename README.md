# Movie Recommender

Welcome to the Movie Recommender application! This Flask-based web app suggests movie recommendations based on user-selected genres and provides an option to discover low-rated movies for a "Trash Movie of the Day."

## Features

- **Movie Recommendations:** Select a genre and get personalized movie recommendations.
- **Trash Movie of the Day:** Explore movies with low ratings for a surprising movie experience.
- **Dark Mode:** Toggle between light and dark modes for a personalized viewing experience.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Movie-Recommendation-App.git
   cd movie-recommender

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure TMDb API Key:**
    Obtain your TMDb API key from [The Movie Database (TMDb)](https://www.themoviedb.org/documentation/api).
    Replace `TMDB_API_KEY` in `app.py` with your API key.

4. **Run the Application:**

   ```bash
   python app.py
   or
   flask run
   ```

5. **Access the App:**
   Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## Usage

- Visit the home page and select a genre from the dropdown.
- Click on "Get Recommendations" to receive personalized movie suggestions.
- Explore the "Trash Movie of the Day" for low-rated movie surprises.
- Toggle between light and dark modes for a customized visual experience.

Screenshots

Add any additional screenshots as needed.

Contributing
If you'd like to contribute to the project, please follow these steps:

**Contribution Workflow:**

1. **Fork the repository.**
2. **Create a new branch:**

   ```bash
   git checkout -b feature/new-feature
   git commit -am 'Add new feature'
   git push origin feature/new-feature
    ```

Submit a pull request and wait for it to be reviewed.

Acknowledgments
Special thanks to The Movie Database (TMDb) for providing movie data.
