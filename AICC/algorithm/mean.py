import pandas as pd
csv_file = 'comedy_cmt_vector_update.csv'
df = pd.read_csv(csv_file)
input_idmovie = 91  # Replace with the desired idmovie
filtered_df = df[df['idmovie'] == input_idmovie]
feature_vectors = filtered_df.iloc[:, 4:].values
for index, row in filtered_df.iterrows():
   print(f"idmovie: {row['idmovie']}, iduser: {row['iduser ']}")

mean_feature_vector = feature_vectors.mean(axis=0)

print(f"Mean feature vector for idmovie {input_idmovie}:")
print(mean_feature_vector)
