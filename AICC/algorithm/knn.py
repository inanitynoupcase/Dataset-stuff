import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Read the CSV file
csv_file = 'comedy_cmt_vector_update.csv'
df = pd.read_csv(csv_file)

# Step 2: Get user input for idmovie
input_idmovie = 91  # Replace with the desired idmovie

# Step 3: Filter the DataFrame to get all rows with the same idmovie
filtered_df = df[df['idmovie'] == input_idmovie]

# Step 4: Print 'idmovie' and 'iduser' for each row in the filtered DataFrame
print(f"Data for idmovie {input_idmovie}:")
for index, row in filtered_df.iterrows():
    print(f"idmovie: {row['idmovie']}, iduser: {row['iduser ']}")

# Step 5: Extract feature vectors (from column 4 to the end)
feature_vectors = filtered_df.iloc[:, 4:].values

# Step 6: Calculate the mean feature vector for the input idmovie
mean_feature_vector = feature_vectors.mean(axis=0)

# Step 7: Find all unique idmovie values that are not the same as the input
unique_idmovies = df['idmovie'].unique()
unique_idmovies = unique_idmovies[unique_idmovies != input_idmovie]

# Step 8: Calculate the mean feature vector for each unique idmovie
mean_feature_vectors = []
for idmovie in unique_idmovies:
    movie_df = df[df['idmovie'] == idmovie]
    movie_feature_vectors = movie_df.iloc[:, 4:].values
    mean_movie_feature_vector = movie_feature_vectors.mean(axis=0)
    mean_feature_vectors.append(mean_movie_feature_vector)

# Step 9: Calculate cosine similarity between the input mean_feature_vector
# and all other mean_feature_vectors
cosine_similarities = cosine_similarity([mean_feature_vector], mean_feature_vectors)

# Step 10: Find the index of the most similar mean feature vector
most_similar_index = np.argmax(cosine_similarities)

# Step 11: Print the idmovie of the most similar movie
most_similar_idmovie = unique_idmovies[most_similar_index]
print(f"Most similar idmovie: {most_similar_idmovie}")

# Step 12: Print 'idmovie' and 'iduser' for each row in the most similar movie
most_similar_df = df[df['idmovie'] == most_similar_idmovie]
print(f"Data for the most similar idmovie {most_similar_idmovie}:")
for index, row in most_similar_df.iterrows():
    print(f"idmovie: {row['idmovie']}, iduser: {row['iduser ']}")

# Step 13: Calculate the mean feature vector for the most similar movie
most_similar_feature_vectors = most_similar_df.iloc[:, 4:].values
most_similar_mean_feature_vector = most_similar_feature_vectors.mean(axis=0)
print(f"Mean feature vector for the most similar idmovie:")
print(most_similar_mean_feature_vector)
