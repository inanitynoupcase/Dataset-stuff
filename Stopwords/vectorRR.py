import csv

# Read keywords from keyword.csv into a dictionary
keywords = {}
with open('keywords/keywords_comedy.csv', 'r', encoding='utf-8') as keyword_file:
    keyword_reader = csv.reader(keyword_file)
    next(keyword_reader)  # Skip the header row
    for row in keyword_reader:
        if len(row) == 2:
            keyword, value = row
            keyword = keyword.strip()
            value = float(value)
            keywords[keyword] = value

# Read comments from comment.csv and generate vectors
vectors = []
with open('withidmovie/loc_haihuoc_final.csv', 'r', encoding='utf-8') as comment_file:
    comment_reader = csv.reader(comment_file)
    header = next(comment_reader)  # Store the header row
    # Find the index of the "idmovie" column
    idmovie_index = header.index("idmovie")
    # Append the headers and keywords to the vectors list
    vectors.append(header[1:] + list(keywords.keys()))
    for row in comment_reader:
        idmovie = row[idmovie_index]  # Get the value of the "idmovie" column

        # Initialize a vector for the current comment
        vector = [0.0] * len(keywords)

        # Check if each keyword exists in the comment and update the vector
        for i, keyword in enumerate(keywords.keys()):
            if keyword in row[0]:
                vector[i] = keywords[keyword]

        # Append the remaining columns and the generated vector to the vectors list
        vectors.append(row[1:] + vector)

# Write the vectors to an output CSV file
with open('abc/comedy_vector.csv', 'w', newline='', encoding='utf-8') as output_file:
    vector_writer = csv.writer(output_file)
    vector_writer.writerows(vectors)
