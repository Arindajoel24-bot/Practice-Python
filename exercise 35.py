from collections import Counter
import json
bd = {
    "01": "January", 
    "02": "February", 
    "03": "March", 
    "04": "April", 
    "05": "May", 
    "06": "June", 
    "07": "July", 
    "08": "August",
    "09": "September", 
    "10": "October",
    "11": "November",
    "12": "December"
}
months = []
with open("34.json", "r") as file:
    birthdays = json.load(file)

for name, date in birthdays.items():
    day, month, year = date.split("/")
    months.append(bd[month])
counts = Counter(months)
print(counts)
