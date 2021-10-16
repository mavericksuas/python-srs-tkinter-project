# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 02:13:46 2020

@author: UPMANYU JHA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df5_dataset=pd.DataFrame()


for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\Visualization\\Book1.xlsx"]:
    excel_data_df5 = pd.read_excel(f)
    df5 = pd.DataFrame(excel_data_df5, columns= ['Agent'])
    products_list = df5.values.tolist()
    #print (products_list[0])
    #print(df5.head(0))
    #print(df5)
    #print(df5.index)
# Prepare data in three parts 2017 2018 2019 2020 for leased and owned
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
    excel_data_df5 = pd.read_excel(f)
    df5 = pd.DataFrame(excel_data_df5, columns= ['Year','Tenure','Agent'])
    products_list = df5.values.tolist()
    #print (products_list[0])
    #print(df5.head(0))
    #print(df5)
    #print(df5.index)
    
for i in products_list:
    
    if i[0]==2017 and i[1]=="Leased":
        x=name.get(i[2])
        x=x+1
        name[i[2]]=x

    if i[0]==2018 and i[1]=="Leased":
        x=name.get(i[2])
        x=x+1
        name[i[2]]=x
        
    if i[0]==2019 and i[1]=="Leased":
        x=name.get(i[2])
        x=x+1
        name[i[2]]=x


agentname1=[]

for j in products_list:
    if j not in agentname1:
        agentname1.append(j)

agentname1.pop(0)
agentname1.pop(0)
agentname1.pop(len(agentname1)-1)

#print(agentname1)

name11 ={}

for j in agentname1:
    #print(j[0])
    name11.update({j[0]:0})
        


#print(name11)

    

for j in products_list:
    
    if j[0]==2017 and j[1]=="Owned":
        x=name11.get(j[2])
        x=x+1
        name11[j[2]]=x

    if j[0]==2018 and j[1]=="Owned":
        x=name11.get(j[2])
        x=x+1
        name11[j[2]]=x
        
    if j[0]==2019 and j[1]=="Owned":
        x=name11.get(j[2])
        x=x+1
        name11[j[2]]=x
        
#print(name)
name1=list(name.values())
name2=list(name11.values())


# Make a fake dataset:
height = name1
height1 = name2

#print(agentname)
#print(agentname1)

bars = (agentname[0],agentname[1],agentname[2],agentname[3],agentname[4],agentname[5],agentname[6],agentname[7],agentname[8])
y_pos = np.arange(len(bars))
bars1 = (agentname1[0],agentname1[1],agentname1[2],agentname1[3],agentname1[4],agentname1[5],agentname1[6],agentname1[7],agentname1[8])
y_pos1 = np.arange(len(bars1))
plt.figure(figsize=(15,8))
# Create bars
plt.bar(y_pos, height, color='orange', width=0.6)
plt.bar(y_pos1, height1, color='green', width=0.2)
 
# Create names on the x-axis
plt.xticks(y_pos, bars)
plt.xticks(y_pos1, bars)
plt.title(" performance of all agents based on the area leased and owned for the years 2017,2018 and 2019")
plt.legend(['performance of all agents on the area Leased', 'performance of all agents on the area Owned'])
plt.xlabel('Agent name')
plt.ylabel('Frequency of count')
# Show graphic
plt.show()

