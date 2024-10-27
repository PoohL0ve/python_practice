from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/~guido/'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, features="html.parser")
# pretty_soup = soup.prettify()

# Get the title and text
title = soup.title
guido_text = soup.get_text()
print(title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))
