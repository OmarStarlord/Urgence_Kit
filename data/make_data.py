import csv

# Read the text file and split it into lines
with open("file.txt", "r") as file:
    lines = file.readlines()

# Initialize variables
data = []
current_catastrophe = ""

# Iterate over each line in the file
for line in lines:
    # Strip any leading/trailing whitespace
    line = line.strip()
    # Check if the line contains a catastrophe
    if line.endswith(":"):
        current_catastrophe = line[:-1]  # Remove the ":" from the catastrophe name
    else:
        # If not a catastrophe, append the data to the list
        data.append((current_catastrophe, line))

# Write the data to a CSV file
with open("disaster_supplies.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "type_of_catastrophe", "content"])  # Write header
    for idx, (catastrophe, content) in enumerate(data, start=1):
        writer.writerow([idx, catastrophe, content])
