import csv

def read_csv_rows(file_path):

    with open(
        file_path,
        mode="r",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            yield row