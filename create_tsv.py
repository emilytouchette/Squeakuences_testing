import csv

# Data to be written to the TSV file
data = [
    ["Processing Time (hours)", "Cores Used"],
    ["17.15", 1],
    ["16.97", 2],
    ["15.98", 4],
    ["14.43", 8]
]

# File path for the TSV file
file_path = "data.tsv"

# Writing to the TSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(data)

print(f"Data has been written to {file_path}")

 