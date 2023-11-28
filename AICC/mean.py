import pandas as pd

# Step 1: Read the CSV file
csv_file = 'data.csv'
df = pd.read_csv(csv_file)

# Step 2: Get user input for idmovie
input_idmovie = 91  # Replace with the desired idmovie

# Step 3: Filter the DataFrame to get all rows with the same idmovie
filtered_df = df[df['idmovie'] == input_idmovie]

# Step 4: Extract feature vectors (from column 4 to the end)
feature_vectors = filtered_df.iloc[:, 4:].values

# Step 5: Calculate the mean of the feature vectors
mean_feature_vector = feature_vectors.mean(axis=0)

print(f"Mean feature vector for idmovie {input_idmovie}:")
print(mean_feature_vector)
