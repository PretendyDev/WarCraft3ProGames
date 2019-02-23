
from bs4 import BeautifulSoup
import time
import requests
import re

# Simple Python Web Scraper, to retrieve upcoming Warcraft 3 Professional Matches'

url = "https://liquipedia.net/warcraft/Major_Tournaments"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup.prettify())

h2Body = soup.find_all('h2')
print('Tournament Type: ' + h2Body[1].text.strip())

h3Body = soup.find_all('h3')
print('Upcoming Games In: ' + h3Body[0].text.strip() + '\n')

tableData = soup.find_all('td')

# Match Dates #
spans = tableData[1].find_all('span')
dateSpan = spans[1].text.strip()
print('Tournament Dates: ' + dateSpan)

# Tournament Name #
tounamentName = tableData[2].text.strip()
print('Tournament Name: ' + tounamentName)

# Prize Money #
prizeMoney = tableData[3].text.strip()
print('Prize Money: ($)' + prizeMoney)

# Location #
locationGet = tableData[4].text.strip() + ' - ' + tableData[4].img.get('alt', '')
print('Held: ' + locationGet)

# Winner #
winner = tableData[5].text.strip()
print('Winner: ' + winner)

# Runner Up #
runnerUp = tableData[6].text.strip()
print('Runner-up: ' + runnerUp)


# List Comprehension #

##eventInfo = {
##    "Major": {
##        "Date": dateSpan,
##        "Tournament Name": h2Body,
##        "Prize ($)": prizeMoney,
##        "Location": locationGet,
##        "Winner": winner,
##        "Runner-up": runner-Up
##        }
##    }
