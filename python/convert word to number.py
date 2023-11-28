import pandas as pd

# Đọc file extracted_keywords.csv
df_test = pd.read_csv('extracted_keywords.csv')

# Đọc file result.csv
df_result = pd.read_csv('datasets/result.csv')

# Hàm để tìm giá trị số từ DataFrame df_result


def find_value(keyword):
    row = df_result[df_result['keyword'] == keyword.strip()]
    if len(row) > 0:
        return row.iloc[0]['value']
    return 0


# Biến đổi dòng 'keywords' thành cặp "keyword, value"
df_test['keywords'] = df_test['keywords'].fillna('').apply(lambda x: ' '.join(
    [str(find_value(keyword)) for keyword in str(x).split('.')]
))

df_test.to_csv('keyword_to_number.csv', index=False)
