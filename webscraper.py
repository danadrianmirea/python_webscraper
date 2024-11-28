import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "https://github.com/danadrianmirea"
response = requests.get(url)

# Step 2: Check if the request was successful
if response.status_code == 200:
    # Step 3: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract all links
    links = soup.find_all('a')  # Finds all <a> tags
    for link in links:
        print(link.get('href'))  # Prints the href attribute of each link
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
