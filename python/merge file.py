import pandas as pd

# Đọc file flim name.csv
film_df = pd.read_csv('datasets/Romactic_film_100.csv')

# Đọc file comment định dạng Excel
comment_df = pd.read_excel('datasets/romantic_comments.xlsx')

# Tạo một cột mới trong DataFrame film_df để chứa các bình luận
film_df['comment'] = ''

# Lặp qua từng hàng trong DataFrame film_df và gán hai bình luận từ comment_df vào cột comment
for i, row in film_df.iterrows():
    # Lấy ngẫu nhiên hai bình luận từ comment_df
    comments = comment_df.sample(n=2)['Nội dung bình luận'].tolist()
    # Ghép hai bình luận thành một chuỗi và gán vào cột comment
    film_df.at[i, 'comment'] = ' '.join(comments)

# Lưu kết quả vào file mới
film_df.to_csv('merged_data.csv', index=False)
