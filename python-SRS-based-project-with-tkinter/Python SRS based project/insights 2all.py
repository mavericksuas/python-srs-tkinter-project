# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 12:37:24 2020

@author: UPMANYU JHA
"""


import pandas as pd

import matplotlib.pyplot as plt


df2_dataset=pd.DataFrame()


for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\data by client\\ccaedfproperty.xlsx"]:
    excel_data_df2 = pd.read_excel(f,"Page1_1",header=8)
    df2 = pd.DataFrame(excel_data_df2, columns= ['Year','UoM','Tenure','Area','Country'])
    products_list = df2.values.tolist()
    #print (products_list[0])
    #print(df2.head(0))
    #print(df2)
    #print(df2.index)
# Prepare data in three parts 2017 2018 2019 2020 for leased and owned
# sqm leased
sqm_2017_leased=[]
sqm_2018_leased=[]
sqm_2019_leased=[]

# sqm owned
sqm1_2017_leased=[]
sqm1_2018_leased=[]
sqm1_2019_leased=[]

#ha leased to sqm leased
ha_2017_leased=[]
ha_2018_leased=[]
ha_2019_leased=[]

# ha leased to sqm owned
ha1_2017_leased=[]
ha1_2018_leased=[]
ha1_2019_leased=[]


area_in_2019=0
area_in_2018=0
area_in_2017=0

area1_in_2019=0
area1_in_2018=0
area1_in_2017=0

for i in products_list:
    # leased
    if i[0]==2017 and i[1]=="SQ-M" and i[2]=="Leased" and i[4]=="CA":
        sqm_2017_leased.append(i[3])
    if i[0]==2018 and i[1]=="SQ-M" and i[2]=="Leased" and i[4]=="CA":
        sqm_2018_leased.append(i[3])
    if i[0]==2019 and i[1]=="SQ-M" and i[2]=="Leased" and i[4]=="CA":
        sqm_2019_leased.append(i[3])
    
    
    # leased
    if i[0]==2017 and i[1]=="HA" and i[2]=="Leased" and i[4]=="CA":
        ha_2017_leased.append(i[3])
    if i[0]==2018 and i[1]=="HA" and i[2]=="Leased" and i[4]=="CA":
        ha_2018_leased.append(i[3])
    if i[0]==2019 and i[1]=="HA" and i[2]=="Leased" and i[4]=="CA":
        ha_2019_leased.append(i[3])
    
    
    # leased
    if i[0]==2017 and i[1]=="SQ-M" and i[2]=="Leased" and i[4]=="WS":
        sqm1_2017_leased.append(i[3])
    if i[0]==2018 and i[1]=="SQ-M" and i[2]=="Leased" and i[4]=="WS":
        sqm1_2018_leased.append(i[3])
    if i[0]==2019 and i[1]=="SQ-M" and i[2]=="Leased" and i[4]=="WS":
        sqm1_2019_leased.append(i[3])
    
    # leased
    if i[0]==2017 and i[1]=="HA" and i[2]=="Leased" and i[4]=="WS":
        ha1_2017_leased.append(i[3])
    if i[0]==2018 and i[1]=="HA" and i[2]=="Leased" and i[4]=="ES":
        ha1_2018_leased.append(i[3])
    if i[0]==2019 and i[1]=="HA" and i[2]=="Leased" and i[4]=="WS":
        ha1_2019_leased.append(i[3])
    



# =============================================================================
# print("Sum leased 2017-2019 for CA",
#       sum(sqm_2017_leased),
#       sum(sqm_2018_leased),
#       sum(sqm_2019_leased),
#       "Sum leased 2017-2019 for WS",
#       sum(sqm1_2017_leased),
#       sum(sqm1_2018_leased),
#       sum(sqm1_2019_leased))
# 
# 
# print("Sum ha leased 2017-2019 for CA",
#       sum(ha_2017_leased)*10000,
#       sum(ha_2018_leased)*10000,
#       sum(ha_2019_leased)*10000,
#       "Sum ha  leased 2017-2019 for WS",
#       sum(ha1_2017_leased)*10000,
#       sum(ha1_2018_leased)*10000,
#       sum(ha1_2019_leased)*10000)
# =============================================================================

area_in_2019=sum(sqm_2019_leased)+sum(ha_2019_leased)*10000
#area_in_2019=round(area_in_2019)
area_in_2018=sum(sqm_2018_leased)+sum(ha_2018_leased)*10000
#area_in_2018=round(area_in_2018)
area_in_2017=sum(sqm_2017_leased)+sum(ha_2017_leased)*10000
#area_in_2017=round(area_in_2017)

area1_in_2019=sum(sqm1_2019_leased)+sum(ha1_2019_leased)*10000
#area1_in_2019=round(area1_in_2019)
area1_in_2018=sum(sqm1_2018_leased)+sum(ha1_2018_leased)*10000
#area1_in_2018=round(area1_in_2018)
area1_in_2017=sum(sqm1_2017_leased)+sum(ha1_2017_leased)*10000
#area1_in_2017=round(area1_in_2017)


x=['2017','2018','2019']
y=[area_in_2017,area_in_2018,area_in_2019]
y1=[area1_in_2017,area1_in_2018,area1_in_2019]



plt.figure(figsize=(5,4))
plt.titel=("Year which got max leased area in CA and WS")
plt.plot(x,y)
plt.plot(x,y1)
plt.grid(True)
plt.legend(['CA','WS'])
plt.xlabel('YEARS')
plt.ylabel('AREA')
plt.show()

