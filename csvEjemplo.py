import csv

labels = ['Name', 'Age', 'Country']
dct_arr = [
  {'Name': 'John', 'Age': '23', 'Country': 'USA'},
  {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'},
  {'Name': 'Anne', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}
]

print(dct_arr)
print('\n\n')
print(dct_arr[0])

try:
    with open('csv_dct.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in dct_arr:
            writer.writerow(elem)
except IOError:
    print("I/O error")