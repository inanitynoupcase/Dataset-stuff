import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read the CSV file
csv_file = 'algorithm\\action_cmt_vector_update.csv'
df = pd.read_csv(csv_file)

# Step 2: Get user input for idmovie
input_idmovie = 1  # Replace with the desired idmovie
# Step 3: Filter the DataFrame to get all rows with the same idmovie
filtered_df = df[df['idmovie'] == input_idmovie]

feature_vectors = filtered_df.iloc[:, 4:].values

# Step 6: Calculate the mean feature vector for the input idmovie
mean_feature_vector = feature_vectors.mean(axis=0)

# Step 7: Find all unique idmovie values that are not the same as the input
unique_idmovies = df['idmovie'].unique()
unique_idmovies = unique_idmovies[unique_idmovies != input_idmovie]

# Step 8: Calculate the mean feature vector for each unique idmovie
mean_feature_vectors = []
movie_feature_dict = {}
for idmovie in unique_idmovies:
    movie_df = df[df['idmovie'] == idmovie]
    movie_feature_vectors = movie_df.iloc[:, 4:].values
    mean_movie_feature_vector = movie_feature_vectors.mean(axis=0)
    mean_feature_vectors.append(mean_movie_feature_vector)
    movie_feature_dict[idmovie] = mean_movie_feature_vector

# Step 9: Calculate cosine similarity between the input mean_feature_vector
# and all other mean_feature_vectors
cosine_similarities = cosine_similarity([mean_feature_vector], mean_feature_vectors)

# Step 10: Print all idmovie values, their cosine distances, and feature vectors

sorted_movies = sorted(unique_idmovies, key=lambda idmovie: cosine_similarities[0][unique_idmovies.tolist().index(idmovie)], reverse=True)
film_csv_file = 'algorithm\\test1.csv'
film_df = pd.read_csv(film_csv_file)
watching_movie = film_df.loc[film_df.index == input_idmovie-1]['filmname'].values[0]
#watching_movie= film_df.loc[filtered_df['idmovie'] == input_idmovie, 'filmname'].values[0]
print("id movie",input_idmovie," movie watching  ",watching_movie)
print()
print("Sorted Idmovies and Their Cosine Similarity Distances :")
for idmovie in sorted_movies[:10]:  # Take the first 10 movies
    distance = cosine_similarities[0][unique_idmovies.tolist().index(idmovie)]
    movie_name = film_df.loc[film_df.index == idmovie-1]['filmname'].values[0]
   # movie_name = film_df.loc[filtered_df['idmovie'] == input_idmovie, 'filmname'].values[1]
    print(f"idmovie: {idmovie},film name: {movie_name}, Cosine Similarity Distance: {distance}")




    


   








