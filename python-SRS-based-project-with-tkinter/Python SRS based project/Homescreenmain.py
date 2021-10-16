# -*- coding: utf-8 -*-
"""
Created on Sun Oct 4 02:13:46 2020

@author: UPMANYU JHA
"""

from tkinter import*
from PIL import ImageTk, Image # pip install pillow
from tkinter import ttk
import tkinter.messagebox as tm
# For connenction on mysql database in python
import pymysql
import re
# For processing date and time variable
from datetime import datetime
import pandas as pd
from pandastable import Table, TableModel
#image capthca
import random
import webbrowser


text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
      
root123=Tk()
root123.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class Homescreen:
    
    def __init__(self,root123):
        self.root123=root123
        self.root123.title("SUNVILLE PROPERTY HOME")
        self.root123.geometry("1350x790+0+0")
        
        
        #======Bg Image======
        
        self.bggg=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/pngwave.png")
        bggg=Label(self.root123,image=self.bggg).place(x=350,y=0,relwidth=1,relheight=1)
        
        #=========================Handel frame for home==========================
        Hold_Frame=Frame(self.root123,bd=0,relief=GROOVE,bg="#00FF00")
        Hold_Frame.place(x=0,y=0,relwidth=1,height=80)
    
        self.bg111=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/pngwave (1).png")
        bg111=Label(Hold_Frame,image=self.bg111,bg="#00FF00").place(x=-10,y=6,relheight=1, width=135)
        
        self.rrr=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/loginbtn.png")
        btn_lgin=Button(Hold_Frame,image=self.rrr,cursor="hand2",bg="#00FF00",fg="#00FF00",command=self.logingup).place(x=1100, y=23, width=143, height=36)
        
        self.rrr11=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/insights.png")
        btn_compare=Button(Hold_Frame,image=self.rrr11,cursor="hand2",bg="#00FF00",fg="#00FF00", command=self.compare111).place(x=1270, y=15)
        
        
        #=========================Center Handel frame for home==========================
        Center_Frame=Frame(self.root123,bd=0,relief=GROOVE,bg="white")
        Center_Frame.place(x=5,y=85,width=750,height=620)
        
        titel11=Label(Center_Frame,text="Sunville Property", font=("times new roman",20,"bold"),bg="white" ,fg="green").place(x=20,y=15)
        
        
        titeli1=Label(Center_Frame,text="""Sunville Properties is a Colorado based property 
consultants who have appointed their agesnts across Major Cities
 across the globe.They have sub-Coompanies which take carethe 
 buiness in different countries and are placed in  the countries 
 from where they operate from. The Company currently has been using
 multiple forms of data storage and want to streamline their working 
 using an application ,which can help them seamlessly navigate via 
 different forms of storage. Also the company seeks some insights into
 the current data and also going further in future. """, font=("times new roman",17,"bold"),bg="white" ,fg="green").place(x=20,y=65)
        
        self.bg181=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/timeline.png")
        bg181=Label(Center_Frame,image=self.bg181, bg="white").place(x=30,y=300,height=350, width=750)
        
        
        #=========================Bottom Handel frame for home==========================
        Btm_Frame=Frame(self.root123,bd=0,relief=GROOVE,bg="black")
        Btm_Frame.place(x=0,y=710,relwidth=1,height=80)
        
        self.inst=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/insta.png")
        btn_inst=Button(Btm_Frame,image=self.inst,cursor="hand2",bg="black",fg="black", command=self.openinsta).place(x=1260, y=25, height=32, width=32)
        
        self.fb=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/facebook.png")
        btn_fb=Button(Btm_Frame,image=self.fb,cursor="hand2",bg="black",fg="black", command=self.openfb).place(x=1300, y=25, height=32, width=32)
        
        titelu1=Label(Btm_Frame,text="Contact No.: 9435112125", font=("times new roman",15,"bold"),bg="black" ,fg="white").place(x=20,y=25)
        
        titelg1=Label(Btm_Frame,text="E-mail id: sunvilleproperty@gmail.com", font=("times new roman",15,"bold"),bg="black" ,fg="white").place(x=560,y=25)
        
        
    def openinsta(self):
        webbrowser.open("https://www.instagram.com/upmanyujha/")
    
    def openfb(self):
        webbrowser.open("https://www.facebook.com/Upmanyujha0001/")
        
        
    def logingup(self):
        self.root123.destroy()
        import Agentlogin
        
    def compare111(self):
        self.root666=Toplevel()
        self.root666.title("Module4 WINDOW")
        self.root666.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly
        self.root666.geometry("1350x800+80+28")
        self.root666.focus_force()
        self.root666.grab_set()
        
        #=================title frame=====================
        titel=Label(self.root666,text="Country with Maximum Numbers of Registered Customer's", font=("times new roman",30,"bold"),bd=12,relief=GROOVE,bg="#F0FFFF" ,fg="green",pady=2, padx=2).pack(fill=X)
        titel=Label(self.root666,text="Collective Payment Amount and Outstanding Amount for all the Customer's ", font=("times new roman",30,"bold"),bd=12,relief=GROOVE,bg="#F0FFFF" ,fg="green").place(x=0,y=600,relwidth=1)
        
        
        
        
        
        #=================Frame 1=============================
        F1=LabelFrame(self.root666,text="((MAXIMUM))",font=("times new roman",15,"bold"),fg="green",bg="white",bd=14,relief=GROOVE)
        F1.place(x=0,y=76,height=519,relwidth=1)
        
        lab2_type=Label(F1,text="""COUNTRY with MAXIMUM NUMBER of REGISTERED CUSTOMERS""",bg="white",fg="green", font=("times new roman",28,"bold"))
        lab2_type.place(x=0,y=110,height=80, relwidth=1)
        self.lbamp=StringVar()
        lb3_maxv=Label(F1,textvariable=self.lbamp,bg="#F0FFFF",fg="green", font=("times new roman",60,"bold"))
        lb3_maxv.place(x=0,y=200,height=150,relwidth=1)
        
        btn1=Button(F1, text="COMPARE",cursor="hand2",command=self.compare,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=580,y=360,width=150,height=35)
       
        
       
        
       
        #=================Frame 2============================
        F2=LabelFrame(self.root666,text="((Collective and Outstanding Results))",font=("times new roman",15,"bold"),fg="green",bg="white",bd=14,relief=GROOVE)
        F2.place(x=0,y=674,height=122,relwidth=1)
        
        lb1_aamt=Label(F2,bg="white",fg="green",text="COLLECTIVE PAYMENT AMMOUNT", font=("times new roman",15,"bold"))
        lb1_aamt.grid(row=0,column=0,pady=10,padx=10,sticky=W)
        self.payamt=StringVar()
        txt_aamt=Entry(F2,text="self.tpay",textvariable=self.payamt, font=("times new roman",15,"bold"),bd=5,relief=GROOVE,state='readonly')
        txt_aamt.grid(row=0,column=1,pady=10,padx=0,sticky=W)
        Calbalbtn=Button(F2,text="Click",cursor="hand2",bg="#FF8C00",fg="white",width=4,height=1,bd=6,command=self.tpay).grid(row=0,column=2,padx=0,pady=10,sticky=E)
        
        
        lb1_bamt=Label(F2,bg="white",fg="green",text="COLLECTIVE OUTSTANDING AMMOUNT", font=("times new roman",15,"bold"))
        lb1_bamt.grid(row=0,column=4,pady=10,padx=10,sticky=E)
        self.outamt=StringVar()
        txt_bamt=Entry(F2,text="self.tout",textvariable=self.outamt, font=("times new roman",15,"bold"),bd=5,relief=GROOVE,state='readonly')
        txt_bamt.grid(row=0,column=5,pady=10,padx=0,sticky=E)
        Calbalbtn=Button(F2,text="Click",cursor="hand2",bg="#FF8C00",fg="white",width=4,height=1,bd=6,command=self.tout).grid(row=0,column=6,padx=0,pady=10,sticky=E)
        
        
        
        
        
        
        
        
    def tpay(self):
        try:
            # Connecetion for mysql database
            con = pymysql.connect(user="root", password="", host="localhost",database="sales")
            cur = con.cursor()
            cur.execute("select sum(PAYMENT_AMT) as totalsum from customer ")
            result=cur.fetchall()
            #print (result)
            if result==None:
                    tm.showerror("Error","DATABASE ERROR!",parent=self.root666)
            else:
                self.payamt.set(result)
                con.close()
        except Exception as es:
            tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root666)


        
   
        
           
                    
    def tout(self):
        try:
            # Connecetion for mysql database
            con = pymysql.connect(user="root", password="", host="localhost",database="sales")
            cur = con.cursor()
            cur.execute("select sum(OUTSTANDING_AMT) as totalsum from customer ")
            result=cur.fetchall()
            #print (result)
            if result==None:
                    tm.showerror("Error","INVALID INPUT!",parent=self.root666)
            else:
                self.outamt.set(result)
                
                con.close()   
        except Exception as es:
            tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root666)







    def compare(self):
        try:
            # Connecetion for mysql database
            con = pymysql.connect(user="root", password="", host="localhost",database="sales")
            cur = con.cursor()
            cur.execute("select CUST_COUNTRY,count(*) from customer group by CUST_CODE order by count(*) desc",tuple(self.lbamp.get()))
            result=cur.fetchall()
            #print (result)
            if result==None:
                    tm.showerror("Error","INVALID INPUT!",parent=self.root666)
            else:
                for i in result:
                    #print(i[0])
                    self.lbamp.set(str(i[0]))
                con.close()   
        except Exception as es:
            tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root666)

   


        
    
    
    
obj=Homescreen(root123)
root123.mainloop()