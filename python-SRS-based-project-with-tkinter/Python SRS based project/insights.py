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

root=Tk()
root.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class Insights:
    
    def __init__(self,root):
        def getValue():
            print("Combo : "+str(combobox.get()))
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
        
        
        #button       
        viewbtn=Button(Manage_Frame,text="VIEW GRAPH",command=getValue,font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2",width=15,pady=5).grid(row=4,columnspan=2,padx=5,pady=10)
        
        
        
        #========Details and search Frame=========
        Detail_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="#98FB98")
        Detail_Frame.place(x=420,y=95,width=920,height=600)
        
        
        
        fig = Figure(figsize=(5, 4), dpi=100)
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