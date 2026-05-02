import requests
from bs4 import BeautifulSoup


#url = requests.get("http://www.nytimes.com/")

#soup = BeautifulSoup(url.text, "html.parser")
#titles = soup.find_all("p", class_=True)
#for title in titles:
    #print(title.text)
url = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(url.text, "html.parser")
titles = soup.find_all("span", class_="titleline")
for title in titles:
    print(title.text)