import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import operator

# Function to predict a movie's rating and recommend similar movies
def predict_score():
    # Load the movie data (assuming you have a DataFrame called 'movies')
    movies = pd.read_csv('your_movie_data.csv')  # Replace 'your_movie_data.csv' with the actual file path
    
    name = input('Enter a movie title: ')
    new_movie = movies[movies['original_title'].str.contains(name)].iloc[0].to_frame().T
    print('Selected Movie: ', new_movie.original_title.values[0])
    
    def getNeighbors(baseMovie, K):
        distances = []
    
        for index, movie in movies.iterrows():
            if movie['new_id'] != baseMovie['new_id'].values[0]:
                dist = Similarity(baseMovie['new_id'].values[0], movie['new_id'])
                distances.append((movie['new_id'], dist))
    
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
    
        for x in range(K):
            neighbors.append(distances[x])
        return neighbors
    
    K = 10
    avgRating = 0
    neighbors = getNeighbors(new_movie, K)
    print('\nRecommended Movies: \n')
    for neighbor in neighbors:
        avgRating = avgRating + movies.iloc[neighbor[0]][2]  
        print(movies.iloc[neighbor[0]][0] + " | Genres: " + str(movies.iloc[neighbor[0]][1]).strip('[]').replace(' ', '') + " | Rating: " + str(movies.iloc[neighbor[0]][2]))
    
    print('\n')
    avgRating = avgRating / K
    print('The predicted rating for %s is: %f' % (new_movie['original_title'].values[0], avgRating))
    print('The actual rating for %s is %f' % (new_movie['original_title'].values[0], new_movie['vote_average']))

# The rest of your code for calculating cosine similarity can follow here
# ...

# Call the predict_score() function to predict and recommend a movie
predict_score()
