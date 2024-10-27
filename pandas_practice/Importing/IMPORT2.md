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
r = requests.get(url)  # packages the requests, send the request, and packages the response
html = r.text
soup = BeautifulSoup(html)