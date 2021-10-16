# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 02:13:46 2020

@author: UPMANYU JHA
"""

import pandas as pd

import matplotlib.pyplot as plt

df3_dataset=pd.DataFrame()


for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\Visualization\\Book1.xlsx"]:
    excel_data_df3 = pd.read_excel(f)
    df3 = pd.DataFrame(excel_data_df3, columns= ['Agent'])
    products_list = df3.values.tolist()
    #print (products_list[0])
    #print(df3.head(0))
    #print(df3)
    #print(df3.index)
# Prepare data in three parts 2017 2018 2019 2020 for Owned and owned
agentname=[]

for i in products_list:
    if i not in agentname:
        agentname.append(i)

agentname.pop(0)
agentname.pop(0)
agentname.pop(len(agentname)-1)

#print(agentname)

name ={}

for i in agentname:
    #print(i[0])
    name.update({i[0]:0})

#print(name)
for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\Visualization\\Book1.xlsx"]:
    excel_data_df3 = pd.read_excel(f)
    df3 = pd.DataFrame(excel_data_df3, columns= ['Year','City','Tenure','Agent'])
    products_list = df3.values.tolist()
    #print (products_list[0])
    #print(df3.head(0))
    #print(df3)
    #print(df3.index)
    
for i in products_list:
    # Owned
    if i[0]==2017 and i[2]=="Owned":
        x=name.get(i[3])
        x=x+1
        name[i[3]]=x

    if i[0]==2018 and i[2]=="Owned":
        x=name.get(i[3])
        x=x+1
        name[i[3]]=x
        
# =============================================================================
#     if i[0]==2019 and i[2]=="Owned":
#         x=name.get(i[3])
#         x=x+1
#         name[i[3]]=x
# =============================================================================
        
    if i[0]==2020 and i[2]=="Owned":
        x=name.get(i[3])
        x=x+1
        name[i[3]]=x

#print(name)
name1=list(name.values())
import numpy as np

 
# Make a fake dataset:
height = name1

#print(agentname)

bars = (agentname[0],agentname[1],agentname[2],agentname[3],agentname[4],agentname[5],agentname[6],agentname[7],agentname[8])
y_pos = np.arange(len(bars))
plt.figure(figsize=(15,8))
# Create bars
plt.bar(y_pos, height, color='orange', width=0.3)
 
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.title(" Agent codes of all the agents who have got deals in ‘OWNED’ categories across the years")
plt.legend(['Agent with maximum no. of deals in Owned form'])
plt.xlabel('Agent name')
plt.ylabel('Frequency of count')
# Show graphic
plt.show()

