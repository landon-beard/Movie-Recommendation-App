import csv

def load_movie_data(file_path):
    """
    Load movie data from a CSV file and return a list of dictionaries.
    Each dictionary represents a movie with 'id', 'title', and 'genre'.
    """
    movies = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append(row)
    return movies

if __name__ == "__main__":
    # For testing purposes
    file_path = 'movies.csv'
    movies = load_movie_data(file_path)
    print(movies)
