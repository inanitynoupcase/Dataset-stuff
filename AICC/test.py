import csv

# Function to read keywords and their values from a CSV file
def read_keyword_csv(file_name):
    keywords = {}
    with open(file_name, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                keyword, value = row[0].strip(), float(row[1].strip())
                keywords[keyword] = value
    return keywords

# Function to convert a string to a vector using keywords
def string_to_vector(input_string, keywords):
    words = input_string.split()
    vector = [keywords.get(word, 0) for word in words]
    return vector

# File name for the keyword CSV (assuming it's in the same folder as the script)
csv_file_name = "keyword_comedy.csv"

# Read keywords and their values from the CSV file
keyword_dict = read_keyword_csv(csv_file_name)

# Input string
input_string = "this movie is very funny"

# Convert the input string to a vector
output_vector = string_to_vector(input_string, keyword_dict)

# Print the output vector
print(output_vector)
