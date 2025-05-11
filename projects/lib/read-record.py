import csv
from robot.api.deco import keyword

@keyword("Read CSV File Test Case")
def read_csv_file_test_case(file_path, rows_to_skip=0, delimiter=',', encoding='utf-8'):
    with open(file_path, mode='r', newline='', encoding=encoding) as file:
        # Use csv.Sniffer to detect the delimiter
        # sniffer = csv.Sniffer()
        # sample = file.read(1024)
        # file.seek(0)
        # detected_dialect = sniffer.sniff(sample)
        cleaned_lines = (delimiter.join(part.strip() for part in line.split(delimiter)) for line in file)
        
        # Read the CSV file using the detected dialect
        csv_reader = csv.reader(cleaned_lines, delimiter=delimiter)
        
        # Skip the specified number of rows
        for _ in range(rows_to_skip):
            next(csv_reader, None)
        
        # Extract the header (keys)
        keys = next(csv_reader, None)
        # print(f"Keys (Header): {keys}")
        # Convert rows to list of dictionaries
        data = [dict(zip(keys, row)) for row in csv_reader]
        return data
        # Print the result
        # for item in data:
            # print(item)

# # Example usage
if __name__ == "__main__":
    file_path = r'D:\\.w\\repositories\\Test\\robotframework101\\projects\\demo1\\10-2025-4-28-14-52-32.csv'
    read_csv_file_test_case(file_path, rows_to_skip=2, delimiter=',', encoding='utf-8')