import csv
import re


def process_csv_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csv_input, open(output_file, 'w', newline='', encoding='utf-8') as csv_output:
        reader = csv.reader(csv_input)
        writer = csv.writer(csv_output)

        for row in reader:
            processed_row = process_row(row)
            writer.writerow(processed_row)


def process_row(row):
    processed_row = []
    for item in row:
        item = item.strip()
        item = " ".join(item.split())
        item = re.sub(r"[^\w\s!?]", "", item)
        processed_row.append(item)
    return processed_row


input_file = "comment.csv"
output_file = "comment_output.csv"
process_csv_file(input_file, output_file)
