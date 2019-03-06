from bs4 import BeautifulSoup
import sys
import time
import requests
import re

# Simple Python Web Scraper, to retrieve upcoming Warcraft 3 Professional Matches'

print('Choose the tournament type you would like to see:' +'\n' + '1: Major Tournaments' +'\n' + '2: Minor Tournaments' +'\n' + '3: Show Matches' + '\n')

tournament_Type = input()

if tournament_Type == "1":
    url = "https://liquipedia.net/warcraft/Major_Tournaments"
    print('\n' + 'Fetching Major Tournament Data')
elif tournament_Type == "2":
    url = "https://liquipedia.net/warcraft/Minor_Tournaments"
    print('\n' + 'Fetching Minor Tournament Data')
elif tournament_Type == "3":
    url = 'https://liquipedia.net/warcraft/Show_Matches'
    print('\n' + 'Fetching Show Match Data')
else:
    print('\n' + 'Please enter 1, 2, 3 or 4')
    sys.exit()


# Needs work #
##elif tournament_Type == "4":
##    url = "https://liquipedia.net/warcraft/Major_Tournaments"
##    tournament_scrape(url)
##    url = "https://liquipedia.net/warcraft/Minor_Tournaments"
##    tournament_scrape(url)
##    url = 'https://liquipedia.net/warcraft/Show_Matches'
##    tournament_scrape(url)
##    print('\n' + 'Fetching All Data')
##else:
##    print('\n' + 'Please enter 1, 2, 3 or 4')
##    sys.exit()

def tournament_scrape(url):

    #url = "https://liquipedia.net/warcraft/Major_Tournaments"
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(soup.prettify()) # Prettify HTML Content

    h2Body = soup.find_all('h2')
    print('Tournament Type: ' + h2Body[1].text.strip())

    h3Body = soup.find_all('h3')
    print('Upcoming Games In: ' + h3Body[0].text.strip() + '\n')




    #BeauitfulSoup, finds the first table then looks for the first tr, this provides us with the table headers.
    tablez = soup.find('table', attrs={'class':'sortable wikitable smwtable jquery-tablesorter'})
    table_headers = tablez.find_all('tr')
    #For look used to return each table header value within the tr.
    rowz = table_headers[0]
    for row in rowz:
        heds = rowz.find_all('th')
        heds = [ele.text.strip() for ele in heds]

    #Strip extras from Prize($) header
    prizeStrip = heds[2]
    w = re.findall(r"[A-Z][a-z]+", prizeStrip)
    v = w[0] + ' ($)'
    heds[2] = v
    print(heds)
    #print('\n')




    #BeauitfulSoup, finds the first table then looks for the first tbody, followed by the 'tr's and 'td's within the tbody.
    table = soup.find('table', attrs={'class':'sortable wikitable smwtable jquery-tablesorter'})
    table_body = table.find('tbody')
    #For loop, used to return each td value within the tr and strips.
    rows = table_body.find_all('tr')
    rowList = []
    for row in rows:
        cols = row.find_all('td')
        for colls in cols:
            rowList.append(colls.text.strip())
    #print('\n')

    #Take the row list, create a 2D array, create a new list every 6 elements
    new = []
    for i in range(0, len(rowList), 6):
            new.append(rowList[i : i+6])
    #For each row in list:New, find the date and strip it for cleaner answer
    for row in new:
        dateStrip = row[0]
        z = re.findall(r"[A-Z][a-z]+\s[0-9]+", dateStrip)
        if len(z) == 2:
            y = z[0] + ' - ' + z[1]
        else:
            y = z[0]
        row[0] = y
    #For each element in the row of the list: New, print the elements of the row
        for elem in row:
            print(elem, end=', ')
        print()

tournament_scrape(url)

## TO DO ##
##Create modules / functions:
##    Ask for which tournament type [Minor/Major/Show/All]
##    Provide actual upcoming tournaments based on dates, provide older tournaments
##
##List Comprehension / Database:
##    Export the results into an SQLite database
##
##Pick out hyperlinks of the tournament names:
##    Provide hyperlinks to the specific tournament pages for more info on participants, etc.

