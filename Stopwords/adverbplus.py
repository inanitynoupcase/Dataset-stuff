import csv

# Initialize empty list to store the new data
new_data = []

# Read CSV file 1
with open('datasets/adverbs.csv', 'r', encoding='utf-8') as csv_file1:
    csv_reader1 = csv.reader(csv_file1)
    next(csv_reader1)  # Skip the header row
    data1 = list(csv_reader1)

# Read CSV file 2
with open('datasets/word.csv', 'r', encoding='utf-8') as csv_file2:
    csv_reader2 = csv.reader(csv_file2)
    next(csv_reader2)  # Skip the header row
    data2 = list(csv_reader2)
for row in data2:
    new_data.append(row)
# Perform the multiplication and generate new data
for row1 in data1:
    for row2 in data2:
        new_keyword = row1[0] + " " + row2[0]
        new_value = float(row1[1]) * float(row2[1])
        new_data.append([new_keyword, new_value])

# Write the new data to CSV file 3
with open('datasets/result.csv', 'w', encoding='utf-8', newline='') as csv_file3:
    csv_writer = csv.writer(csv_file3)
    csv_writer.writerow(['keyword', 'value'])  # Write the header
    csv_writer.writerows(new_data)

print("CSV file 3 has been created with the new data.")
