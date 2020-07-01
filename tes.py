# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author: surya
"""

import bs4
import requests
import pandas as pd
import json

kabupatenKota=[]
totalPDP=[]
totalPositif=[]
totalMeninggal=[]
totalSembuh=[]
covidSumut=[]


r = requests.get('http://covid19.sumutprov.go.id/')
soup = bs4.BeautifulSoup(r.text, "lxml")

table = soup.find('table', class_ = 'table table-striped table-bordered table-responsive table-custome')
for data in table.find_all('tbody'):
    rows = data.find_all('tr')
    for row in rows:
        kab= row.find_all('td')[1].text
        pdp= row.find_all('td')[2].text
        pos= row.find_all('td')[3].text
        men= row.find_all('td')[4].text
        sem= row.find_all('td')[5].text
        
        sumut={
            'Kabupaten_Kota' : kab,
            'Pdp' : pdp,
            'Positif' : pos,
            'Meninggal' : men,
            'Sembuh' : sem
            }
        
        
        
        #kabupatenKota.append(kab)
        #totalPDP.append(pdp)
        #totalPositif.append(pos)
        #totalMeninggal.append(men)
        #totalSembuh.append(sem)
        covidSumut.append(sumut)
        
#covid = {'CovidSumut':covidSumut}
with open('sumut.json', 'w', encoding='utf-8') as f:
            json.dump(covidSumut, f, ensure_ascii=False, indent=4)
#df = pd.DataFrame(covid)
#df.to_json("coid.json")
        


   
