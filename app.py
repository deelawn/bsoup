import requests, os
from bs4 import BeautifulSoup

# send a GET request to the New York Times
r = requests.get("http://www.nytimes.com/")

# convert the response to text
r_html = r.text

# pass the text to BS
soup = BeautifulSoup(r_html)

# create a list of titles by finding all of the H2s within the class type story-heading
title_list = soup.find_all("h2", attrs={"class": "story-heading"})

# create standard out to a text file -- w means the application will override whatever is in our file
os.sys.stdout = open('output.txt','w')

# iterate through the titles and strip the text
# as long as the title isn't an empty string, encode our output and print to the file
for title in title_list:
    title = title.text.strip()
    if title!="":
        print(title).encode('utf-8')
