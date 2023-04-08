import requests
from bs4 import BeautifulSoup
import pandas as pd
l=[]
l1=[]
for a in range(1,6):
    re = requests.get('https://news.ycombinator.com/news'+f'?p={a}')
    soup = BeautifulSoup(re.text,'html.parser')
    titles=list( soup.select(".titleline"))
    scores=list(soup.select(".score"))
    l+=titles
    l1+=scores
title_list=[]
link=[]
score=[]
for i in l:
    title_list.append(i.text)
    link.append(i.find('a').get('href'))
for j in l1:
    score.append(int(j.text.split()[0]))

d= {"title":title_list,"links":link,"scores":score}

print(len(d['scores']))