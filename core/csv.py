import datetime
import csv
import os


def to_csv(people: list):
    date = datetime.datetime.now()

    month = str(date.strftime("%B"))
    year = str(date.year)

    file = month + '_' + year + '.csv'

    fieldnames = ['name', 'time_in_seconds', 'salary']

    with open(file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if os.stat(file).st_size == 0:
            writer.writeheader()
        writer.writerows(people)
