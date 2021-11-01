from bs4 import BeautifulSoup
import requests

def getstrippedcontent(url):
    try:
        page = requests.get(url)
    except TypeError:
        print('TypeError thrown, are you sure you entered a valid URL?')
    def remove_tags(html):
        soup = BeautifulSoup(html, "html.parser")
        for data in soup(['style', 'script']):
            data.decompose()
        return ''.join(soup.stripped_strings)
    return remove_tags(page.content)
