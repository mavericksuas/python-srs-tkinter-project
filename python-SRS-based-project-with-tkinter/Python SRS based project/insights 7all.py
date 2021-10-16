# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 15:02:58 2020

@author: UPMANYU JHA
"""

import pandas as pd

import matplotlib.pyplot as plt

df7_dataset=pd.DataFrame()

import csv
from pandas import read_csv

for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\data by client\\ccaedfproperty.xlsx"]:
    excel_data_df7 = pd.read_excel(f,"Page1_1",header=8)
    df7 = pd.DataFrame(excel_data_df7, columns= ['Year','UoM','Tenure','Area'])
    products_list = df7.values.tolist()
    #print (products_list[0])
    #print(df7.head(0))
    #print(df7)
    #print(df7.index)
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


total_area_2017=0
total_area_2018=0
total_area_2019=0
total_area_2020=0


for i in products_list:
    # leased
    if i[0]==2017 and i[1]=="SQ-M" and i[2]=="Leased":
        sqm_2017_leased.append(i[3])
    if i[0]==2018 and i[1]=="SQ-M" and i[2]=="Leased":
        sqm_2018_leased.append(i[3])
    if i[0]==2019 and i[1]=="SQ-M" and i[2]=="Leased":
        sqm_2019_leased.append(i[3])
    if i[0]==2020 and i[1]=="SQ-M" and i[2]=="Leased":
        sqm_2020_leased.append(i[3])
    # Owned

    if i[0]==2017 and i[1]=="SQ-M" and i[2]=="Owned":
        sqm_2017_owned.append(i[3])
    if i[0]==2018 and i[1]=="SQ-M" and i[2]=="Owned":
        sqm_2018_owned.append(i[3])
    if i[0]==2019 and i[1]=="SQ-M" and i[2]=="Owned":
        sqm_2019_owned.append(i[3])
    if i[0]==2020 and i[1]=="SQ-M" and i[2]=="Owned":
        sqm_2020_owned.append(i[3])
    
    # leased
    if i[0]==2017 and i[1]=="HA" and i[2]=="Leased":
        ha_2017_leased.append(i[3])
    if i[0]==2018 and i[1]=="HA" and i[2]=="Leased":
        ha_2018_leased.append(i[3])
    if i[0]==2019 and i[1]=="HA" and i[2]=="Leased":
        ha_2019_leased.append(i[3])
    if i[0]==2020 and i[1]=="HA" and i[2]=="Leased":
        ha_2020_leased.append(i[3])
    # Owned
    if i[0]==2017 and i[1]=="HA" and i[2]=="Owned":
        ha_2017_owned.append(i[3])
    if i[0]==2018 and i[1]=="HA" and i[2]=="Owned":
        ha_2018_owned.append(i[3])
    if i[0]==2019 and i[1]=="HA" and i[2]=="Owned":
        ha_2019_owned.append(i[3])
    if i[0]==2020 and i[1]=="HA" and i[2]=="Owned":
        ha_2020_owned.append(i[3])

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
# =============================================================================

# =============================================================================
# total_area=sum(sqm_2017_leased+sqm_2018_leased+sqm_2019_leased+sqm_2020_leased)+sum(ha_2017_leased)*10000+sum(ha_2018_leased)*10000+sum(ha_2019_leased)*10000+sum(ha_2020_leased)*10000+sum(sqm_2017_owned+sqm_2018_owned+sqm_2019_owned+sqm_2020_owned)+sum(ha_2017_owned)*10000+sum(ha_2018_owned)*10000+sum(ha_2019_owned)*10000+sum(ha_2020_owned)*10000
# #print(total_area)
# =============================================================================
total_area_2017=sum(sqm_2017_leased)+sum(ha_2017_leased)*10000+sum(sqm_2017_owned)+sum(ha_2017_owned)*10000
#print(total_area_2017)
total_area_2018=sum(sqm_2018_leased)+sum(ha_2018_leased)*10000+sum(sqm_2018_owned)+sum(ha_2018_owned)*10000
#print(total_area_2018)
total_area_2019=sum(sqm_2019_leased)+sum(ha_2019_leased)*10000+sum(sqm_2019_owned)+sum(ha_2019_owned)*10000
#print(total_area_2019)
total_area_2020=sum(sqm_2020_leased)+sum(ha_2020_leased)*10000+sum(sqm_2020_owned)+sum(ha_2020_owned)*10000
#print(total_area_2020)

with open('C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\Visualization\\timeseries.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Year","Total Area"])
    writer.writerow([2017,total_area_2017])
    writer.writerow([2018, total_area_2018])
    writer.writerow([2019,total_area_2019])
    writer.writerow([2020, total_area_2020])



plt.figure(figsize=(8,6))
series = read_csv('C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\Visualization\\timeseries.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
series.plot()
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, alpha=0.7)
plt.legend(['Time series analysis report of the orders received'])
plt.xlabel('YEARS')
plt.ylabel('AREA')
plt.show()
