import csv


def getStopwordsFromFile(stopword_file):
    stopwords = set()
    with open(stopword_file, 'r', encoding='utf-8') as file:
        for line in file:
            stopwords.add(line.strip())
    return stopwords


def findDuplicateStopwords(stopwords, csv_file, cmt_column):
    duplicate_stopwords = set()
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cmt = row[cmt_column]
            for stopword in stopwords:
                if stopword in cmt:
                    duplicate_stopwords.add(stopword)
    return duplicate_stopwords


def removeStopwords(stopwords_file, csv_file, cmt_column, output_file):
    stopwords = getStopwordsFromFile(stopwords_file)
    with open(csv_file, 'r', encoding='utf-8') as input_file, \
            open(output_file, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            cmt = row[cmt_column]
            words = cmt.lower().split()  # Chuyển thành chữ thường và tách thành từng từ
            # Kiểm tra stopwords ở dạng chữ thường
            filtered_words = [
                word for word in words if word.lower() not in stopwords]
            filtered_cmt = ' '.join(filtered_words)
            row[cmt_column] = filtered_cmt
            writer.writerow(row)
    print('Xuất file thành công')


# Đường dẫn tới file stopword.txt
stopword_file = 'stopwords.txt'
# Đường dẫn tới file comment.csv
csv_file = 'comment.csv'
# Tên cột "cmt" trong file comment.csv
cmt_column = 'cmt'
# Tên file mới để ghi stopword
output_file = 'duplicate_stopwords.txt'
# Tên file mới để xuất kết quả
output_file_final = 'comment_without_stopword.csv'
# Lấy stopwords từ file stopword.txt
stopwords = getStopwordsFromFile(stopword_file)
# Tìm các stopword trùng lặp trong cột "cmt" của file comment.csv
duplicate_stopwords = findDuplicateStopwords(stopwords, csv_file, cmt_column)
# Ghi các stopword trùng lặp vào file mới
with open(output_file, 'w', encoding='utf-8') as file:
    for stopword in duplicate_stopwords:
        file.write(stopword + '\n')
    print('Ghi file thành công')
# Loại bỏ stopword và xuất kết quả ra file comment_without_stopword.csv
removeStopwords(output_file, csv_file, cmt_column, output_file_final)
