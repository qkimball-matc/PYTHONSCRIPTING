#!/usr/bin/env python3

import requests, bs4

res = requests.get("http://notpurple.com")
res.raise_for_status()
purp = bs4.BeautifulSoup(res.text, 'html.parser')

title = purp.select('title')
print("The title of this webpage is:",title[0].getText())

siteLink = purp.select('a')
linkTotal = len(siteLink)
i = 0
print("The following links on the webpage are:")
while i < linkTotal:
    print(siteLink[i].getText())
    i+=1