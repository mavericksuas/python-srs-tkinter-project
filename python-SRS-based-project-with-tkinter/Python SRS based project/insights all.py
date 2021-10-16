# -*- coding: utf-8 -*-
"""
Created on Sun Oct 2 10:51:50 2020

@author: UPMANYU JHA
"""

from tkinter import*
from tkinter import ttk,ANCHOR
from tkinter.ttk import Combobox
import tkinter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import csv
from pandas import read_csv

root=Tk()
root.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class Insights:
    
    def __init__(self,root):
        def getValue():
            print("Combo : "+str(combobox.get(ANCHOR)))
            print("List Box : "+str(listbox.get(ANCHOR)))
    
        def onChangeValue(object):
            print("Value "+str(combobox.get()))

        self.root=root
        self.root.title("SRS INSIGHT'S WINDOW")
        self.root.geometry("1350x790+40+40")
        
        
        title=Label(self.root,text="INSIGHT'S",bd=12,relief=GROOVE, font=("times new roman",40,"bold"),bg="#00FF00" ,fg="white")
        title.pack(side=TOP,fill=X)
        
        #=========Manage and update Frame================
        Manage_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="#98FB98")
        Manage_Frame.place(x=10,y=95,width=400,height=600)
        
        m_title=Label(Manage_Frame,bg="#98FB98",fg="darkgreen",text="SELECT THE INSIGHT", font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        #combo box
        combobox=Combobox(Manage_Frame,font=("times new roman",11,"bold"), width=14,  state='readonly')
        items=("SELECT YEAR","2020","2019","2018","2017")
        combobox['values']=items
        combobox.current(0)
        combobox.bind("<<ComboboxSelected>>",onChangeValue)
        combobox.grid(row=3,column=0, padx=5)
        
        
        #listbox
        scrollbar = Scrollbar(Manage_Frame, orient=VERTICAL)
        listbox=Listbox(Manage_Frame,font=("times new roman",10,"bold"), height=15, width=27,bd=6)#,yscrollcommand=scrollbar.set
        
        
        listbox.insert(1,"Insights-A")
        
        listbox.insert(2,"Insights-B")
        
        listbox.insert(3,"Insights-C")
        
        listbox.insert(4,"Insights-D")
        
        listbox.insert(5,"Insights-E")
        
        listbox.insert(6,"Insights-F")
        
        listbox.insert(7,"Insights-G")
        
        listbox.insert(8,"Insights-H")
        
        # Attaching Listbox to Scrollbar 
        # Since we need to have a vertical  
        # scroll we use yscrollcommand 
        listbox.config(yscrollcommand = scrollbar.set) 
          
        # setting scrollbar command parameter  
        # to listbox.yview method its yview because 
        # we need to have a vertical view 
        scrollbar.config(command = listbox.yview) 
        
        scrollbar.grid(row=3, column=2, padx=0, pady=20, sticky=N+S+E)
        listbox.grid(row=3,column=1, padx=1, pady=20,sticky=N+S+E+W)
        
# =============================================================================
#         listbox.bind("<<Insights-A>>", self.insighta)
#         listbox.bind("<<Insights-B>>", self.insightb)
#         listbox.bind("<<Insights-C>>", self.insightc)
#         listbox.bind("<<Insights-D>>", self.insightd)
#         listbox.bind("<<Insights-E>>", self.insighte)
#         listbox.bind("<<Insights-F>>", self.insightf)
#         listbox.bind("<<Insights-G>>", self.insightg)
#         listbox.bind("<<Insights-H>>", self.insighth)
#         
# =============================================================================
        
        #button       
        viewbtn=Button(Manage_Frame,text="VIEW GRAPH",command=getValue,font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2",width=15,pady=5).grid(row=4,columnspan=2,padx=5,pady=10)
        
        
        
        #========Details and search Frame=========
        Detail_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="#98FB98")
        Detail_Frame.place(x=420,y=95,width=920,height=600)
        
        
        
        fig = Figure(figsize=(5, 4), dpi=100)
        
        def insighta(self):
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
            
            
            
            # The slice names of a population distribution pie chart
            pieLabels = 'Owned','Leased'
            # Population data
            totalownedvsleased = [total_area_owned,total_area_leased]
            
            fig.add_subplot(111).titel=("The total property area sold\n"+"vs\n"+" total property are leased in Sq-M only\n")
            
            
            # Draw the pie chart
            fig.add_subplot(111).pie(totalownedvsleased,
                    labels=pieLabels,
                    shadow=True,
                    autopct='%1.2f%%',
                    explode = (0.1, 0),
                    startangle=0)
            
            fig.add_subplot(111).legend(title="Tenure")
            
            # Aspect ratio - equal means pie is a circle
            fig.add_subplot(111).axis('equal')
            plt.show()
            
                    
            
            
            
    
            
            
        def insightb(self):
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



            
            
            
    
            
            
        
        def insightc(self):
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












        def insightd(self):
            df4_dataset=pd.DataFrame()
            for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\Visualization\\Book1.xlsx"]:
                excel_data_df4 = pd.read_excel(f)
                df4 = pd.DataFrame(excel_data_df4, columns= ['Agent'])
                products_list = df4.values.tolist()
                #print (products_list[0])
                #print(df4.head(0))
                #print(df4)
                #print(df4.index)
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
                excel_data_df4 = pd.read_excel(f)
                df4 = pd.DataFrame(excel_data_df4, columns= ['Year','City','Tenure','Agent'])
                products_list = df4.values.tolist()
                #print (products_list[0])
                #print(df4.head(0))
                #print(df4)
                #print(df4.index)
                
            for i in products_list:
                # leased
                if i[0]==2017 and i[1]=="Chilliwack" and i[2]=="Leased":
                    x=name.get(i[3])
                    x=x+1
                    name[i[3]]=x
            
                    #agents_2017 = df4.pivot_table(index=i[3], aggfunc='size')
                if i[0]==2018 and i[1]=="Chilliwack" and i[2]=="Leased":
                    x=name.get(i[3])
                    x=x+1
                    name[i[3]]=x
                    #agents_2018 = df4.pivot_table(index=i[3], aggfunc='size')
                if i[0]==2019 and i[1]=="Chilliwack" and i[2]=="Leased":
                    x=name.get(i[3])
                    x=x+1
                    name[i[3]]=x
                if i[0]==2020 and i[1]=="Chilliwack" and i[2]=="Leased":
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
            plt.title(" For chillwalk city, which agent has got the maximum deals in leased form")
            plt.legend(['Agent with maximum no. of deals in leased form'])
            plt.xlabel('Agent name')
            plt.ylabel('Frequency of count')
            # Show graphic
            plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        def insighte(self):
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


        











        def insightf(self):
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


        








        def insightg(self):
            df7_dataset=pd.DataFrame()
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












        def insighth(self):
            df8 = pd.DataFrame()

            #\\
            for f in ["C:\\Users\\Upmanyu\\Desktop\\Python SRS based project(Internship)\\data by client\\ccaedfproperty.xlsx"]:
                excel_data_df8 = pd.read_excel(f,"Page1_1",header=8)
                df8 = pd.DataFrame(excel_data_df8, columns= ['Latitude','Longitude'])
                products_list = df8.values.tolist()
                #print (products_list[0])
                #print(df8.head(0))
                #print(df8)
                #print(df8.index)
            df8.plot()
            plt.show()
        
      ###################################################################################################################################################################################################
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
        
        
        
        # The slice names of a population distribution pie chart
        pieLabels = 'Owned','Leased'
        # Population data
        totalownedvsleased = [total_area_owned,total_area_leased]
        
        fig.add_subplot(111).titel=("The total property area sold\n"+"vs\n"+" total property are leased in Sq-M only\n")
        
        
        # Draw the pie chart
        fig.add_subplot(111).pie(totalownedvsleased,
                labels=pieLabels,
                shadow=True,
                autopct='%1.2f%%',
                explode = (0.1, 0),
                startangle=0)
        
        fig.add_subplot(111).legend(title="Tenure")
        
        # Aspect ratio - equal means pie is a circle
        fig.add_subplot(111).axis('equal')
        plt.show()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        canvas = FigureCanvasTkAgg(fig, Detail_Frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        toolbar = NavigationToolbar2Tk(canvas, Detail_Frame)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        
        def on_key_press(self,event):
            print("you pressed {}".format(event.key))
            key_press_handler(event, canvas, toolbar)
        
        
        canvas.mpl_connect("key_press_event", on_key_press)
        
        
        
        
        #========QUIT Frame=========
        Quitt_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="#98FB98")
        Quitt_Frame.place(x=10,y=700,width=1330,height=85)
        
        
        
        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        
        
        
        #button   
        qquitbtn=Button(Quitt_Frame,text="QUIT",cursor="hand2",command=_quit,font=("times new roman",15,"bold"),bg="red",fg="white",width=10,pady=5).place(x=622,y=15)
        
        
        
        
        
        
        
        
        
        tkinter.mainloop()
        # If you put root.destroy() here, it will cause an error if the window is
        # closed with the window manager.
                
        
        
obj=Insights(root)
root.mainloop()