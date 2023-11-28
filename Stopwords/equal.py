import pandas as pd

# Đọc dữ liệu từ tệp CSV gốc
# Thay 'merged_file.csv' bằng tên tệp CSV kết quả trước đó
df = pd.read_csv('vector/merged_2.csv')

# Tạo một cột "class" dựa trên giá trị trong cột "genre"
df['class'] = df['genre'].apply(lambda x: {
    1: 'action',
    2: 'romance',
    3: 'comedy',
}.get(x, 'unknown'))  # Nếu không khớp với bất kỳ giá trị nào, sẽ được gán là 'unknown'

# Lưu bảng kết quả vào một tệp CSV mới
# Tên tệp CSV mới là 'final_file.csv'
df.to_csv('vector/merge_comment.csv', index=False)
