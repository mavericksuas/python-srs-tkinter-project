# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 15:02:58 2020

@author: UPMANYU JHA
"""

import pandas as pd

import matplotlib.pyplot as plt

df_dataset=pd.DataFrame()


for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\data by client\\ccaedfproperty.xlsx"]:
    excel_data_df = pd.read_excel(f,"Page1_1",header=8)
    df = pd.DataFrame(excel_data_df, columns= ['Year','UoM','Tenure','Area'])
    products_list = df.values.tolist()
    #print (products_list[0])
    #print(df.head(0))
    #print(df)
    #print(df.index)
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


total_area_owned=0
total_area_leased=0

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
# 
# =============================================================================
total_area_leased=sum(sqm_2017_leased+sqm_2018_leased+sqm_2019_leased+sqm_2020_leased)+sum(ha_2017_leased)*10000+sum(ha_2018_leased)*10000+sum(ha_2019_leased)*10000+sum(ha_2020_leased)*10000
#total_area_leased=round(total_area_leased)
total_area_owned=sum(sqm_2017_owned+sqm_2018_owned+sqm_2019_owned+sqm_2020_owned)+sum(ha_2017_owned)*10000+sum(ha_2018_owned)*10000+sum(ha_2019_owned)*10000+sum(ha_2020_owned)*10000
#total_area_owned=round(total_area_owned)
#print(total_area_leased)
#print(total_area_owned)
list_area_owned=[total_area_owned,"Owned"]
list_area_leased=[total_area_leased,"Leased"]
list_area=[list_area_owned,list_area_leased]
df_count =pd.DataFrame(list_area,columns=['Area','Tenure'])   
#print(df_count)


plt.figure(figsize=(6, 4))
# The slice names of a population distribution pie chart
pieLabels = 'Owned','Leased'
# Population data
totalownedvsleased = [total_area_owned,total_area_leased]

plt.titel=("The total property area sold\n"+"vs\n"+" total property are leased in Sq-M only")


# Draw the pie chart
plt.pie(totalownedvsleased,
        labels=pieLabels,
        shadow=True,
        autopct='%1.2f%%',
        explode = (0.1, 0),
        startangle=0)

plt.legend(title="Tenure")

# Aspect ratio - equal means pie is a circle
plt.axis('equal')
plt.show()







