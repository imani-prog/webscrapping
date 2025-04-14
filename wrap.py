from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

try:
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    print("Sending request to URL...")
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(request)
    html = response.read()
    response.close()
    print("Request successful, HTML content retrieved.")
except HTTPError as e:
    print(f"HTTP error occurred: {e.code} - {e.reason}")
    exit()
except URLError as e:
    print(f"URL error occurred: {e.reason}")
    exit()
except Exception as e:
    print(f"Unexpected error during HTTP request: {e}")
    exit()

try:
    # Parse HTML
    print("Parsing HTML content...")
    soup = BeautifulSoup(html, 'html.parser')
    print("HTML parsing completed.")

    # Extract first paragraph text
    paragraphs = soup.find_all('p')
    if paragraphs:
        print("First paragraph text:")
        print(paragraphs[0].text)  # Print first paragraph
    else:
        print("No paragraphs found.")

    # Extract table data
    tables = soup.find_all('table')
    if tables:
        print("Tables found!")
        print(tables[0])  # Print first table HTML
    else:
        print("No tables found.")
except AttributeError as e:
    print(f"Attribute error during parsing or data extraction: {e}")
except Exception as e:
    print(f"An unexpected error occurred during parsing or data extraction: {e}")

import pandas as pd

tables = pd.read_html(url)
df = tables[0]  # First table
print(df.head())
df.to_csv("population_data.csv", index=False)
