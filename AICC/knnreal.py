import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import csv
import time

start = time.time()
# Step 1: Read the CSV file
csv_file = 'action_cmt_vector_update.csv'
df = pd.read_csv(csv_file)

# Step 2: Get user input for idmovie
input_idmovie = 3 # Replace with the desired idmovie

# Step 3: Filter the DataFrame to get all rows with the same idmovie
filtered_df = df[df['idmovie'] == input_idmovie]

feature_vectors = filtered_df.iloc[:, 4:].values

# Step 6: Calculate the mean feature vector for the input idmovie
mean_feature_vector = feature_vectors.mean(axis=0)

# Step 7: Find all unique idmovie values that are not the same as the input
unique_idmovies = df['idmovie'].unique()
unique_idmovies = unique_idmovies[unique_idmovies != input_idmovie]

# Step 8: Create a dictionary to map idmovie to its mean feature vector
movie_feature_dict = {}
for idmovie in unique_idmovies:
    movie_df = df[df['idmovie'] == idmovie]
    movie_feature_vectors = movie_df.iloc[:, 4:].values
    mean_movie_feature_vector = movie_feature_vectors.mean(axis=0)
    movie_feature_dict[idmovie] = mean_movie_feature_vector

# Step 9: Determine the number of neighbors
k = 10
# Perform K-nearest neighbors using cosine similarity
neigh = NearestNeighbors(n_neighbors=k, metric='cosine')
neigh.fit(list(movie_feature_dict.values()))
distances, indices = neigh.kneighbors([mean_feature_vector])

# Step 10: Sort the similar movies by ascending cosine similarity
sorted_indices = indices[0]
sorted_distances = distances[0]

# Step 11: Print the top movies with the highest cosine similarity

# Save movie_feature_dict to a CSV file
with open('movie_feature_dict.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for idmovie, feature_vector in movie_feature_dict.items():
        writer.writerow([idmovie] + feature_vector.tolist())

film_csv_file = 'test1.csv'
film_df = pd.read_csv(film_csv_file)
watching_movie = film_df.loc[film_df['idmovie'] == input_idmovie]['filmname'].values[0]
genre_input_movie = film_df.loc[film_df['idmovie'] == input_idmovie]['genre'].values[0]

genre_map = {1: 'Action', 2: 'Romance', 3: 'Comedy'}

print("id movie", input_idmovie, " movie watching  ", watching_movie, "Genre: ", genre_map.get(genre_input_movie, 'Unknown'))
print()
print("Top similar movies: (knn)")
for i in range(k):
    index = sorted_indices[i]
    idmovie = list(movie_feature_dict.keys())[index]
    similarity = 1 - sorted_distances[i]  # Convert cosine distance to cosine similarity
    movie_name = film_df.loc[film_df['idmovie'] == idmovie]['filmname'].values[0]
    genre_movie = film_df.loc[film_df['idmovie'] == idmovie]['genre'].values[0]
    #print(f"idmovie: {idmovie}, film name: {movie_name}, Genre: {genre_map.get(genre_movie, 'Unknown')}, Cosine Similarity: {similarity}")
    #print(f"idmovie: {idmovie}, film name: {movie_name}, Genre: {genre_map.get(genre_movie, 'Unknown')}")
    print(f"{idmovie}", end=' ')

end = time.time()
print("time: ", end - start)