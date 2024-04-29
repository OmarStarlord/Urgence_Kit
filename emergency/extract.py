import requests
from bs4 import BeautifulSoup
import pandas as pd


def fetch_emergency_numbers(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content  
    else:
        print("Failed to fetch data")
        return None


def parse_emergency_numbers(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', class_='wikitable')
    emergency_numbers = {}
    if table:
        rows = table.find_all('tr')[1:]  
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 2:
                country = columns[0].text.strip()
                number = columns[1].text.strip()
                emergency_numbers[country] = number
    return emergency_numbers


url = "https://en.wikipedia.org/wiki/List_of_emergency_telephone_numbers"


html_content = fetch_emergency_numbers(url)

if html_content:
    
    emergency_numbers = parse_emergency_numbers(html_content)
    
    
    classified_data = [{'country': country, 'emergency_number': number} for country, number in emergency_numbers.items()]
    
    
    df = pd.DataFrame(classified_data)
    
    
    file_path = "emergency_numbers.csv"
    df.to_csv(file_path, index=False)
    
    print(f"Emergency numbers saved to {file_path}")
else:
    print("No emergency numbers fetched.")
