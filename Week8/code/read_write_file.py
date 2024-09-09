#Read and Write TXT files

# Read files
import csv
with open('example.txt', 'r') as file:
    lines = file.readlines()

# Iterate over each line and print
for line in lines:
    print(line)


#Write files
# Open a file in write mode ('w') and write some text
with open('example.txt', 'w') as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

# Open the file in append mode ('a') and add new text
with open('example.txt', 'a') as file:
    file.write("This is an additional line.\n")



#Read and Write CSV files

# Writing to a CSV file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Writing the header (optional)
    writer.writerow(["Name", "Age", "Occupation"])

    # Writing some rows
    writer.writerow(["Alice", 30, "Engineer"])
    writer.writerow(["Bob", 25, "Doctor"])
    writer.writerow(["Charlie", 35, "Teacher"])


# Reading from a CSV file
with open('example.csv', 'r') as file:
    reader = csv.reader(file)

    # Loop through the rows and print them
    for row in reader:
        print(row)

# ['Name', 'Age', 'Occupation']
# ['Alice', '30', 'Engineer']
# ['Bob', '25', 'Doctor']
# ['Charlie', '35', 'Teacher']


# Reading from a CSV file using DictReader
with open('example.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Loop through the rows and print them as dictionaries
    for row in reader:
        print(row)

# {'Name': 'Alice', 'Age': '30', 'Occupation': 'Engineer'}
# {'Name': 'Bob', 'Age': '25', 'Occupation': 'Doctor'}
# {'Name': 'Charlie', 'Age': '35', 'Occupation': 'Teacher'}




