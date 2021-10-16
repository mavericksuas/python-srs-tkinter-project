# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 05:50:13 2020

@author: UPMANYU JHA
"""

from tkinter import*
from PIL import ImageTk, Image # pip install pillow
from tkinter import ttk
import tkinter.messagebox as tm
# For connenction on mysql database in python
import pymysql
import re


root6=Tk()
root6.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class module4:
    def __init__(self,root6):
        self.root6=root6
        self.root6.title("Module4 WINDOW")
        self.root6.geometry("1350x800+80+28")
        
        
        #=================title frame=====================
        titel=Label(self.root6,text="Country with Maximum Numbers of Registered Customer's", font=("times new roman",30,"bold"),bd=12,relief=GROOVE,bg="#F0FFFF" ,fg="green",pady=2, padx=2).pack(fill=X)
        titel=Label(self.root6,text="Collective Payment Amount and Outstanding Amount for all the Customer's ", font=("times new roman",30,"bold"),bd=12,relief=GROOVE,bg="#F0FFFF" ,fg="green").place(x=0,y=600,relwidth=1)
        
        
        
        
        
        #=================Frame 1=============================
        F1=LabelFrame(self.root6,text="((MAXIMUM))",font=("times new roman",15,"bold"),fg="green",bg="white",bd=14,relief=GROOVE)
        F1.place(x=0,y=76,height=519,relwidth=1)
        
        lab2_type=Label(F1,text="""COUNTRY with MAXIMUM NUMBER of REGISTERED CUSTOMERS""",bg="white",fg="green", font=("times new roman",28,"bold"))
        lab2_type.place(x=0,y=110,height=80, relwidth=1)
        self.lbamp=StringVar()
        lb3_maxv=Label(F1,textvariable=self.lbamp,bg="#F0FFFF",fg="green", font=("times new roman",60,"bold"))
        lb3_maxv.place(x=0,y=200,height=150,relwidth=1)
        
        btn1=Button(F1, text="COMPARE",cursor="hand2",command=self.compare,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=580,y=360,width=150,height=35)
       
        
       
        
       
        #=================Frame 2============================
        F2=LabelFrame(self.root6,text="((Collective and Outstanding Results))",font=("times new roman",15,"bold"),fg="green",bg="white",bd=14,relief=GROOVE)
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
                    tm.showerror("Error","DATABASE ERROR!",parent=self.root6)
            else:
                self.payamt.set(result)
                con.close()
        except Exception as es:
            tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root6)


        
   
        
           
                    
    def tout(self):
        try:
            # Connecetion for mysql database
            con = pymysql.connect(user="root", password="", host="localhost",database="sales")
            cur = con.cursor()
            cur.execute("select sum(OUTSTANDING_AMT) as totalsum from customer ")
            result=cur.fetchall()
            #print (result)
            if result==None:
                    tm.showerror("Error","INVALID INPUT!",parent=self.root6)
            else:
                self.outamt.set(result)
                
                con.close()   
        except Exception as es:
            tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root6)







    def compare(self):
        try:
            # Connecetion for mysql database
            con = pymysql.connect(user="root", password="", host="localhost",database="sales")
            cur = con.cursor()
            cur.execute("select CUST_COUNTRY,count(*) from customer group by CUST_CODE order by count(*) desc",tuple(self.lbamp.get()))
            result=cur.fetchall()
            #print (result)
            if result==None:
                    tm.showerror("Error","INVALID INPUT!",parent=self.root6)
            else:
                for i in result:
                    #print(i[0])
                    self.lbamp.set(str(i[0]))
                con.close()   
        except Exception as es:
            tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root6)

   




     
obj=module4(root6)
root6.mainloop()