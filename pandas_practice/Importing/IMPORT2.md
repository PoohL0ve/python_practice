# Importing Data in Python Part 2

## Importing from the Web
The **urllib** package provides an interface for getting data from the web. It provides the **urlopen()** function that accepts urls:
```python
from urllib.request import urlretrieve
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
urlretrieve(url, 'winequality-white.csv')  # saves the file locally

df = pd.read_csv(url, sep=';')
# For excel: pd.read_csv()
```
HTTP request to import files and data:
```python
from urllib.request import urlopen, Request
url = 'https://www.autismspeaks.org/what-autism'
request = Request(url)
response = urlopen(request)
html = response.read()  # reads the HTML
response.close()
```
A simpler way is to use the request package:
```python
import requests
url = 'https://www.threads.net/?hl=en'
r = requests.get(url)
text = r.text  # HTML as a string
```

Beautiful Soup is a library used to parse and extract structured data from HTML.
```python
from bs4 import BeautifulSoup
import requests
url = 'https://www.umassglobal.edu/'
r = requests.get(url)  # packages the requests, send the request, and catches the response
html = r.text
soup = BeautifulSoup(html)
```

## Interacting with APIs
Application Programming Interfaces are protocols and routines used for creating and interacting with software applications. JavaScript Object Notation (JSON) is used for real-time server to browser communication and is human readable. They are similar to dictionaries:
```js
{'Songs': 'Rock with You',
'Dance': 'MJ'}
```
JSON files can be loaded in Python:
```python
import json
with open('dance.json', 'r') as json_file:
    data = json.load(json_file)

# Iterate and print key-value pairs
# json.loads() for parsing strings
for key, value in data.items():
    print(f'{key}: {value}')
```
Connecting to an API in Python
```python
import requests
# The ? in the URL is a query where t means title
url = 'http://www.funtimeapi.com?t=hackers'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
    print(f'{key}: {value}')
```

APIs and Authentication
```python
import tweepy, json
access_token
acess_token_secret
consumer_key
consumer_secret
# Stream live data
stream = tweepy.Stream(consumer_key, consumer_secret, access_token, access_token_secret)
# Filter by keywords
stream.filter(track=['lgbtq', 'love'])
```
**NB** : Notes taken from DataCamp's Intermediate Importing Data in Python course.
