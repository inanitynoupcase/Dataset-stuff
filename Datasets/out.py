import pandas as pd
import unicodedata

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('vector/action_vector.csv')

# Hàm để loại bỏ dấu từ một chuỗi


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


# Loại bỏ dấu trên các tiêu đề cột
df.columns = [remove_accents(col) for col in df.columns]

# Lưu dữ liệu đã xử lý vào một tệp CSV mới
df.to_csv('vector/action-dau.csv', index=False)

print("Loại bỏ dấu trên tiêu đề cột thành công!")
