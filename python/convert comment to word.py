import pandas as pd

# Đọc file test.csv
df_test = pd.read_csv('merged_data.csv')
df_test['comment'] = df_test['comment'].str.lower()
df_test['comment'] = df_test['comment'].str.replace('.', '')

# Đọc file result.csv
df_result = pd.read_csv('datasets/result.csv')

# Tạo một tập hợp từ khóa từ cột thứ nhất của DataFrame df_result
keyword_set = set(df_result.iloc[:, 0])

# Hàm để trích xuất các từ khóa chính từ câu


def extract_keywords(text):
    words = text.split()
    keywords = []
    n = len(words)
    for i in range(n):
        # Trích xuất từ khóa từ cụm từ có độ dài 1 từ
        if words[i] in keyword_set and words[i] not in keywords:
            keywords.append(words[i])

        for j in range(i + 2, min(i + 5, n) + 1):
            phrase = ' '.join(words[i:j])
            if phrase in keyword_set and phrase not in keywords:
                keywords.append(phrase)
    return '. '.join(keywords)


# Áp dụng hàm extract_keywords lên cột 'comment' của DataFrame df_test
df_test['keywords'] = df_test['comment'].apply(extract_keywords)
df_result = df_test[['Film name', 'keywords']]

# Lưu kết quả vào file mới
df_result.to_csv('extracted_keywords.csv', index=False)
