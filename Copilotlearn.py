import csv

def parse_csv_file(file_path):
    """
    Parses a CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV file.
    """
    with open(file_path, 'r') as csv_file:
        return [row for row in csv.DictReader(csv_file)]
import csv

def parse_csv_file(file_path):
    """
    Parses a CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV file.
    """
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            rows = [row for row in csv_reader]
        return rows
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []