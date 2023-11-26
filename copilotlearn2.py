import csv

def read_csv_file(file_path):
    """
    Reads a CSV file and returns the data as a list of lists.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: The data from the CSV file as a list of lists.
    """
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Unit test
def test_read_csv_file():
    """
    Unit test for the read_csv_file function.
    """
    file_path = '/path/to/your/csv/file.csv'
    expected_data = [['header1', 'header2', 'header3'], ['data1', 'data2', 'data3']]
    assert read_csv_file(file_path) == expected_data

test_read_csv_file()
