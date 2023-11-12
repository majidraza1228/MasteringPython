import csv

def parse_csv_file(file_path):
    """
    Parses a CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV file.
    """
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(row)
        return rows
