#gathering headlines from ny times hompage using requests and beautiful soup

import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com"

#get request
r = requests.get(url)

#using soup

soup = BeautifulSoup(r.text)
for heading in soup.find_all(class_="story-heading"): 
    if heading.a: 
        print(heading.a.text.replace("\n", " ").strip())
    else: 
        print(heading.contents[0].strip())