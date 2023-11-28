import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import time
import joblib
start = time.time()
# Step 1: Read the CSV file
csv_file = 'action_cmt_vector_update.csv'
df = pd.read_csv(csv_file)

# Step 2: Get user input for idmovie
input_idmovie = 3  # Replace with the desired idmovie

# Step 3: Filter the DataFrame to get all rows with the same idmovie
filtered_df = df[df['idmovie'] == input_idmovie]

feature_vectors = filtered_df.iloc[:, 4:].values

# Step 4: Apply SVD to the feature vectors
n_components = 50# You can adjust the number of components as needed
svd = TruncatedSVD(n_components=n_components, random_state=42)
svd_vectors = svd.fit_transform(feature_vectors)

# Step 5: Calculate the mean SVD feature vector for the input idmovie
mean_svd_feature_vector = svd_vectors.mean(axis=0)

# Step 6: Find all unique idmovie values that are not the same as the input
unique_idmovies = df['idmovie'].unique()
unique_idmovies = unique_idmovies[unique_idmovies != input_idmovie]

# Step 7: Calculate the mean SVD feature vector for each unique idmovie
mean_svd_feature_vectors = []
movie_feature_dict = {}
for idmovie in unique_idmovies:
    movie_df = df[df['idmovie'] == idmovie]
    movie_feature_vectors = movie_df.iloc[:, 4:].values
    movie_svd_vectors = svd.transform(movie_feature_vectors)
    mean_movie_svd_feature_vector = movie_svd_vectors.mean(axis=0)
    mean_svd_feature_vectors.append(mean_movie_svd_feature_vector)
    movie_feature_dict[idmovie] = mean_movie_svd_feature_vector

# Step 8: Calculate cosine similarity between the input mean_svd_feature_vector
# and all other mean_svd_feature_vectors
cosine_similarities = cosine_similarity([mean_svd_feature_vector], mean_svd_feature_vectors)

# Step 9: Print the top 10 movies with the highest cosine similarity
sorted_movies = sorted(unique_idmovies, key=lambda idmovie: cosine_similarities[0][unique_idmovies.tolist().index(idmovie)], reverse=True)[:10]

svd_model_filename = 'svd_model.pkl'
joblib.dump(svd, svd_model_filename)

film_csv_file = 'test1.csv'
film_df = pd.read_csv(film_csv_file)
watching_movie = film_df.loc[film_df['idmovie'] == input_idmovie]['filmname'].values[0]

print("id movie", input_idmovie, " movie watching ", watching_movie)
print()
print("Top 10 similar movies: (svd)")
for idmovie in sorted_movies:
    distance = cosine_similarities[0][unique_idmovies.tolist().index(idmovie)]
    movie_name = film_df.loc[film_df['idmovie'] == idmovie]['filmname'].values[0]
    print(f"{idmovie}", end=' ')

end = time.time()
print("time: ", end - start)