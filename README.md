# Bsoup

A simple exercise using beautiful soup.

## Setup

>*Note*: Beautiful Soup 3 has been replaced by Beautiful Soup 4. Beautiful Soup 3 only works on Python 2.x, but Beautiful Soup 4 also works on
Python 3.x.  Beautiful Soup 4 is faster, has more features, and works with third-party parsers
like lxml and html5lib. You should use Beautiful Soup 4 for all new projects.

## Install

```bash
$ mkdir soupex
$ cd soupex
$ virtualenv env
$ source env/bin/activate
$ pip install beautifulsoup4
$ pip install requests
$ pip freeze > requirements.txt
$ deactivate
```

## Instructions

1. Import `requests`, `os`, and `BeautifulSoup`

  ```py
  import requests, os
  from bs4 import BeautifulSoup
  ```
2. Using the requests library, send a git request to `http://nytimes.com/` and assign the response to a variable `r`.
3. Next, convert the response to text using a built-in Python method `.text()` and assign the result to a new variable.
4. After that, pass that new variable to BeautifulSoup, passing the result from THAT to a new variable.
5. Next, we need to find all of the H2s within the class type `story-heading`. First create a variable called `title_list`. Assign that to the result of calling BeautifulSoup's `find_all()` function. Consult the [Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for more information.
6. Then, tell your application to print the output to a file called `output.txt`. The second parameter should indicate that, when printing, the application should override whatever text exists in that file.
7. Finally, iterate through the titles and strip the text. Create a for loop, then create a temporary variable to hold the result of stripping the text from the titles (hint: use `strip()`).
8. Then, as long as the title isn't an empty string, encode our output and print to the file using `.encode('utf-8')`.

Find all of the finished code in app.py in this repo.
