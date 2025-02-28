import csv

# Writing to a CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Role"])
    writer.writerow(["Ritesh", "Tester"])
    writer.writerow(["Amit", "Developer"])

# Reading from a CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
