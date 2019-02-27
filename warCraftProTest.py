
from bs4 import BeautifulSoup
import time
import requests
import re

# Simple Python Web Scraper, to retrieve upcoming Warcraft 3 Professional Matches'

url = "https://liquipedia.net/warcraft/Minor_Tournaments"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')
#print(soup.prettify()) # Prettify HTML Content

h2Body = soup.find_all('h2')
print('Tournament Type: ' + h2Body[1].text.strip())

h3Body = soup.find_all('h3')
print('Upcoming Games In: ' + h3Body[0].text.strip() + '\n')

#tableData = soup.find_all('td') # Old Variable


#BeauitfulSoup, finds the first table then looks for the first tr, this provides us with the table headers.
tablez = soup.find('table', attrs={'class':'sortable wikitable smwtable jquery-tablesorter'})
table_headers = tablez.find_all('tr')
#For look used to return each table header value within the tr.
rowz = table_headers[0]
for row in rowz:
    heds = rowz.find_all('th')
    heds = [ele.text.strip() for ele in heds]

#BeauitfulSoup, finds the first table then looks for the first tbody, followed by the 'tr's and 'td's within the tbody.
table = soup.find('table', attrs={'class':'sortable wikitable smwtable jquery-tablesorter'})
table_body = table.find('tbody')
#For look used to return each td value within the tr and strips.
rows = table_body.find_all('tr')
blab = []
for row in rows:
    cols = row.find_all('td')
    for colls in cols:
        blab.append(colls.text.strip())
##        print(blab)
        

#Strip extras from Prize($) header
prizeStrip = heds[2]
w = re.findall(r"[A-Z][a-z]+", prizeStrip)
v = w[0] + ' ($)'
heds[2] = v
print(heds)
print('\n')
print(blab)
#Strip extras from Date value
##dateStrip = cols[0]
##z = re.findall(r"[A-Z][a-z]+\s[0-9]+", dateStrip)
##y = z[0] + ' - ' + z[1]
##cols[0] = y
##print(cols)


### List Comprehension ###
##
##eventInfo = {
##    "Minor": {
##        heds[0]: cols[0],
##        heds[1]: cols[1],
##        heds[2]: cols[2],
##        heds[3]: cols[3],
##        heds[4]: cols[4],
##        heds[5]: cols[5],
##        }
##    }
##
##print('\n' + str(eventInfo))
