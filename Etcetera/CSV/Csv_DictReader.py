import csv

"""
DictReader function is converting csv file to a dictionary composing key and value for each ?line?


"""
with open('books_small.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

print(csv_reader)


