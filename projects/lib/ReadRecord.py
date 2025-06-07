import csv
from robot.api.deco import keyword
import absl.logging
import re
# -*- coding: utf-8 -*-

class ReadRecord:
    def __init__(self) -> None:
        absl.logging.set_verbosity('warning')
        pass

    @staticmethod
    def clean_text(text):
        return re.sub(r'[\x00-\x1F\x7F]', '', text)


    @keyword("Read CSV File Test Case")
    def read_csv_file_test_case(self, file_path, rows_to_skip=0, delimiter=',', encoding='utf-8-sig'):
        cleaned_content = []
        with open(file_path, mode='r', newline='', encoding=encoding) as file:
            for line in file:
                parts = line.split(delimiter)
                cleaned_parts = [self.clean_text(part.strip()) for part in parts]
                cleaned_line = delimiter.join(cleaned_parts)
                cleaned_content.append(cleaned_line)

        csv_reader = csv.reader(cleaned_content, delimiter=delimiter)

        for _ in range(rows_to_skip):
            next(csv_reader, None)

        keys = next(csv_reader, None)
        data = [dict(zip(keys, row)) for row in csv_reader]
        return data

# # Example usage
# if __name__ == "__main__":
#     file_path = r'D:\\.w\\repositories\\Test\\robotframework101\\projects\\demo1\\10-2025-4-28-14-52-32.csv'
#     read_csv_file_test_case = ReadRecord()
#     read_csv_file_test_case(file_path, rows_to_skip=2, delimiter=',', encoding='utf-8')
