#extract type_of_catastrofe from the csv and remove duplicates  then save it to a new csv file

import csv
import pandas as pd

#read the csv file
df = pd.read_csv('disaster_supplies.csv')

#extract the type_of_catastrofe column
type_of_catastrofe = df['type_of_catastrofe']

#remove duplicates
type_of_catastrofe = type_of_catastrofe.drop_duplicates()

#save to a new csv file
type_of_catastrofe.to_csv('type_of_catastrofes.csv', index=False)


