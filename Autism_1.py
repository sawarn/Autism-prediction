#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:15:55 2021

@author: ga1ileo
"""

import pandas as pd

df=pd.read_csv("/home/ga1ileo/Desktop/Autism/Autism_Dataset.csv")
df.dropna(inplace=True)

#print(a)
num_values = {
   "jaundice":{"yes":1,"no":0},
   "autism":{"yes":1,"no":0},
   "country_of_res":{"Jordan":1,"United States":2,"Egypt":3,"United Kingdom":4,"Bahrain":5,"Austria":6,
                     "Kuwait":7,"United Arab Emirates":8,"Europe":9,"Malta":10,"Bulgaria":11,
                     "South Africa":12,"India":13,"Afghanistan":14,"Georgia":15,"New Zealand":16,"Syria":17,
                     "Iraq":18,"Australia":19,"Saudi Arabia":20,"Armenia":21,"Turkey":22,"Pakistan":23,"Canada":24,
                     "Oman":25,"Brazil":26,"South Korea":27,"Costa Rica":28,"Sweden":29,"Philippines":30,
                     "Malaysia":31,"Argentina":32,"Japan":33,"Bangladesh":34,"Qatar":35,"Ireland":36,"Romania":37,
                     "Netherlands":38,"Lebanon":39,"Germany":40,"Latvia":41,"Russia":42,"Italy":43,"China":44,
                     "Nigeria":45,"U.S. Outlying Islands":46,"Nepal":47,"Mexico":48,"Isle of Man":49,"Libya":50,
                     "Ghana":51,"Bhutan":52,"Spain":53,"Bahamas":54,"Burundi":55,"Chile":56,"France":57,"Tonga":58,
                      "Sri Lanka":59,"Sierra Leone":60,"Ethiopia":61,"Viet Nam":62,"Iran":63,"Iceland":64,"Nicaragua":65,
                      "Hong Kong":66,"Ukraine":67,"Kazakhstan":68,"AmericanSamoa":69,"Uruguay":70,"Serbia":71,"Portugal":72,
                      "Ecuador":73,"Niger":74,"Belgium":75,"Bolivia":76,"Aruba":77,"Finland":78,"Indonesia":79,"Angola":80,
                      "Azerbaijan":81,"Czech Republic":82,"Cyprus":83},
   "gender":{"f":1,"m":0},
   "ethnicity":{"Middle Eastern":1,"White-European":2,"Black":3,"South Asian":4,"Asian":5,
                "Pasifika":6,"Hispanic":7,"Turkish":8,"Latino":9,"Others":10},
    }


df.replace(num_values,inplace=True)
conv={
    'ethnicity':int,
    'age':int
}
df=df.astype(conv)
#print(df.info())

#print(df.head())


