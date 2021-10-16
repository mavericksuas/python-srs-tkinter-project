# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 02:54:42 2020

@author: UPMANYU JHA
"""

import pandas as pd

import matplotlib.pyplot as plt

df6_dataset=pd.DataFrame()


for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\data by client\\ccaedfproperty.xlsx"]:
    excel_data_df6 = pd.read_excel(f,"Page1_1",header=8)
    df6 = pd.DataFrame(excel_data_df6, columns= ['Year','Month','UoM','Tenure','Area'])
    products_list = df6.values.tolist()
    #print (products_list[0])
    #print(df6.head(0))
    #print(df6)
    #print(df6.index)
# Prepare data in three parts 2017 2018 2019 2020 for leased and owned
# sqm leased
sqm_2017_leased=[]
sqm_2018_leased=[]
sqm_2019_leased=[]
sqm_2020_leased=[]
# sqm owned
sqm_2017_owned=[]
sqm_2018_owned=[]
sqm_2019_owned=[]
sqm_2020_owned=[]
#ha leased to sqm leased
ha_2017_leased=[]
ha_2018_leased=[]
ha_2019_leased=[]
ha_2020_leased=[]
# ha leased to sqm owned
ha_2017_owned=[]
ha_2018_owned=[]
ha_2019_owned=[]
ha_2020_owned=[]

tarea_in_2017=0
tarea_in_2018=0
tarea_in_2019=0
tarea_in_2020=0


for i in products_list:
    # leased
    if i[0]==2017 and i[1]=="JUL" and i[2]=="SQ-M" and i[3]=="Leased":
        sqm_2017_leased.append(i[4])
    if i[0]==2018 and i[1]=="JUL" and i[2]=="SQ-M" and i[3]=="Leased":
        sqm_2018_leased.append(i[4])
    if i[0]==2019 and i[1]=="JUL" and i[2]=="SQ-M" and i[3]=="Leased":
        sqm_2019_leased.append(i[4])
    if i[0]==2020 and i[1]=="JUL" and i[2]=="SQ-M" and i[3]=="Leased":
        sqm_2020_leased.append(i[4])
    # Owned

    if i[0]==2017 and i[1]=="JUL"  and i[2]=="SQ-M" and i[3]=="Owned":
        sqm_2017_owned.append(i[4])
    if i[0]==2018 and i[1]=="JUL"  and i[2]=="SQ-M" and i[3]=="Owned":
        sqm_2018_owned.append(i[4])
    if i[0]==2019 and i[1]=="JUL"  and i[2]=="SQ-M" and i[3]=="Owned":
        sqm_2019_owned.append(i[4])
    if i[0]==2020 and i[1]=="JUL"  and i[2]=="SQ-M" and i[3]=="Owned":
        sqm_2020_owned.append(i[4])
    
    # leased
    if i[0]==2017 and i[1]=="JUL" and i[2]=="HA" and i[3]=="Leased":
        ha_2017_leased.append(i[4])
    if i[0]==2018 and i[1]=="JUL" and i[2]=="HA" and i[3]=="Leased":
        ha_2018_leased.append(i[4])
    if i[0]==2019 and i[1]=="JUL" and i[2]=="HA" and i[3]=="Leased":
        ha_2019_leased.append(i[4])
    if i[0]==2020 and i[1]=="JUL" and i[2]=="HA" and i[3]=="Leased":
        ha_2020_leased.append(i[4])
    # Owned
    if i[0]==2017 and i[1]=="JUL" and i[2]=="HA" and i[3]=="Owned":
        ha_2017_owned.append(i[4])
    if i[0]==2018 and i[1]=="JUL" and i[2]=="HA" and i[3]=="Owned":
        ha_2018_owned.append(i[4])
    if i[0]==2019 and i[1]=="JUL" and i[2]=="HA" and i[3]=="Owned":
        ha_2019_owned.append(i[4])
    if i[0]==2020 and i[1]=="JUL" and i[2]=="HA" and i[3]=="Owned":
        ha_2020_owned.append(i[4])


# =============================================================================
# print("Sum leased 2017-2020",sum(sqm_2017_leased),
# sum(sqm_2018_leased),
# sum(sqm_2019_leased),
# sum(sqm_2020_leased),"Sum owned 2017-2020",
# sum(sqm_2017_owned),
# sum(sqm_2018_owned),
# sum(sqm_2019_owned),
# sum(sqm_2020_owned))
# 
# 
# print("Sum ha leased 2017-2020",sum(ha_2017_leased)*10000,
# sum(ha_2018_leased)*10000,
# sum(ha_2019_leased)*10000,
# sum(ha_2020_leased)*10000,"Sum owned ha2017-2020",
# sum(ha_2017_owned)*10000,
# sum(ha_2018_owned)*10000,
# sum(ha_2019_owned)*10000,
# sum(ha_2020_owned)*10000)
# 
# =============================================================================



tarea_in_2017=sum(sqm_2017_leased)+sum(ha_2017_leased)*10000+sum(sqm_2017_owned)+sum(ha_2017_owned)*10000
#tarea_in_2017=round(tarea_in_2017)
tarea_in_2018=sum(sqm_2018_leased)+sum(ha_2018_leased)*10000+sum(sqm_2018_owned)+sum(ha_2018_owned)*10000
#tarea_in_2018=round(tarea_in_2018)
tarea_in_2019=sum(sqm_2019_leased)+sum(ha_2019_leased)*10000+sum(sqm_2019_owned)+sum(ha_2019_owned)*10000
#tarea_in_2019=round(tarea_in_2019)
tarea_in_2020=sum(sqm_2020_leased)+sum(ha_2020_leased)*10000+sum(sqm_2020_owned)+sum(ha_2020_owned)*10000
#tarea_in_2020=round(tarea_in_2020)

x=['JULY,2017','JULY,2018','JULY,2019','JULY,2020']

y=[tarea_in_2017,tarea_in_2018,tarea_in_2019,tarea_in_2020]

#print(y)

plt.figure(figsize=(8,6))
plt.titel=('Amount of property area sold for the month of july for all the years')
plt.plot(x,y, color='green')
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
plt.bar(x,y, color='orange',width=0.3)
plt.legend(['Total amount of property area sold'])
plt.xlabel('YEARS \n'+'(with month of July)')
plt.ylabel('AREA')
plt.show()

