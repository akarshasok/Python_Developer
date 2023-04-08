import requests
from bs4 import BeautifulSoup
import pandas as pd
l=[]
l1=[]
for a in range(1,2):
    re = requests.get('https://news.ycombinator.com/news'+f'?p={a}')
    soup = BeautifulSoup(re.text,'html.parser')
    titles=list(soup.select(".titleline"))

    scores=list(soup.select(".score"))
    l+=titles
    l1+=scores
d=[]
for i,j in enumerate(l):
    title = j.text
    links = j.find('a').get('href')
    if i<len(l1) and i is not None:
        score = int(l1[i].text.split()[0])
    elif i is None:
        score = 0
    d.append({'title':title,'links':links,'score':score})

df =pd.DataFrame(d)
print(df)



