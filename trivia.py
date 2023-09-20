import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Send an HTTP GET request to fetch the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the HTML content of the page
    html_content = response.text
else:
    print("Failed to retrieve the page.")

#Scraping information from infobox

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the infobox table
infobox = soup.find("table", {"class": "infobox"})

# Iterate through rows in the table
for row in infobox.find_all("tr"):
    # Extract the text from each row
    row_text = row.get_text(strip=True)
    print(row_text)

#Scraping trivia from trivia section


soup = BeautifulSoup(html_content, 'html.parser')

# Locate the section or div that contains trivia
trivia_section = soup.find('div', {'class': 'trivia'})

trivia_text = trivia_section.get_text()

# You can further process the text to split it into individual trivia items, if necessary
trivia_items = trivia_text.split('\n')