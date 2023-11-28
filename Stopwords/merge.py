import pandas as pd

# Đọc dữ liệu từ file1.csv và file2.csv
df1 = pd.read_csv('vector/merged_1.csv')
df2 = pd.read_csv('vector/romantic_vector.csv')

# Merge (ghép) hai bảng dựa trên các cột "rate", "genre", "idmovie", và "iduser"
merged_df = df1.merge(
    df2, on=['rate', 'genre', 'idmovie', 'iduser'], how='outer')

# Điền giá trị NaN bằng 0
merged_df = merged_df.fillna(0)

# Hiển thị kết quả
merged_df.to_csv('vector/merged_2.csv', index=False)
