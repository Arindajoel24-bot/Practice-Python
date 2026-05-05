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
with open("17.txt", "w") as file:
    for title in titles:
        file.write(title.text + "\n")