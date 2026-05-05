import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
soup = BeautifulSoup(response.text, "html.parser")

paragraph = soup.find_all("p")
with open("21.txt", "w") as file:
    for p in paragraph:
        file.write(p.text + "\n")
