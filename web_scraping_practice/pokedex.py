# Scrapes pokemon data from the web and makes a table out of it.
from bs4 import BeautifulSoup
import urllib.request
import ssl
import requests
import re
import pandas as pd

mypokedex = []
myfinalpokedex = []
headers = []


url = requests.get('https://pokemondb.net/pokedex/stats/gen1')
data = url.text
soup = BeautifulSoup(data, 'html.parser')
poke = soup.find_all('tr')
headrs = soup.find_all('div' , attrs={'class' : 'sortwrap'})
headers = []
#test = soup.find_all(class_='sortwrap')
for head in headrs:
    headers.append((head.text,[]))


stats2 = []
finstats = []
newlist = []
count = 0
headernum = 0
for cont in poke:
    stats2.append(cont)
for pokemon in stats2:
    raw = pokemon.contents
    for extra in raw:
        if extra == ' ' or extra == '\n':
            pass
        else:
            finstats.append(extra)

for i in finstats[10:]:
    if count < 10:
        headers[headernum][1].append(i.text)
        headernum += 1
        count += 1
    else:
        headernum = 0
        count = 0
        headers[headernum][1].append(i.text)
        headernum += 1
        count += 1

'''
for finistats in finstats:
    newlist.append(finistats.text)
    if len(newlist) % 10 == 0:
        if len(newlist) == 0:
            newlist.append(finistats.text)
            continue
        else:
            myfinalpokedex.append(list(newlist))
            del newlist[:]
#print(myfinalpokedex)
'''
first_result = poke[19]
stats = first_result.contents
upstats = []
finalstats = []
for stat in stats:
    if stat == ' ' or stat == '\n':
        pass
    else:
        upstats.append(stat)
for newstat in upstats:
    finalstats.append(newstat.text)

dict = {}

for c, r in headers:
    dict[c] = r
df = pd.DataFrame(dict)
def cleanup(letters):
    iter = 0
    ls = [p for p in letters]
    for char_ind in range(len(ls)):
        if ls[char_ind].isupper() and char_ind == 0:
            continue
        elif ls[char_ind].isupper() and char_ind > 0:
            ls[char_ind] = ' ' + ls[char_ind]
    finls = ''.join(ls).split(' ')
    length = len(finls)
    if length > 1:
        finls.insert(1, '/')
    return ' '.join(finls)
df['Type']=df['Type'].apply(cleanup)
print(df)
df.to_excel('Pokedex.xlsx')
# Old way of doing it. Does not get data I can use for dataframe but organizes
# nicely into a list.
'''
names = soup.find_all(class_='ent-name')
categories = soup.find_all(class_='sortwrap')
for head in categories:
    headers.append(head.get_text())
#print(headers)
for tags in names:
    for name in tags:
        mypokedex.append(name)
#print(mypokedex)
for val, name in enumerate(mypokedex):
    myfinalpokedex[name] = val + 1
#print(myfinalpokedex)
'''
