import pandas as pd

# Read the text file
with open('tips.txt', 'r') as file:
    lines = file.readlines()

# Split each line into type_of_catastrophe and content
data = []
for line in lines:
    type_of_catastrophe, content = line.strip().split(': ')
    data.append({'type_of_catastrophe': type_of_catastrophe, 'content': content})

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

print("Conversion completed. CSV file saved as 'output.csv'.")
