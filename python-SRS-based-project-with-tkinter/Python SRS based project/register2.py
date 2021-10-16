# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:49:45 2020

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

root2=Tk()
root2.iconbitmap("C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class Register:
    def __init__(self,root2):
        self.root2=root2
        self.root2.title("SUB-COMPANY'S REGISTRATION WINDOW")
        self.root2.geometry("1350x790+40+40")
        #======Bg Image======
        
        self.bg2=PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/cc.png")
        bg2=Label(self.root2,image=self.bg2).place(x=350,y=0,relwidth=1,relheight=1)
        
        #======Left Image======
        
        #self.left=PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/mp1.png")
        #left=Label(self.root2,image=self.left).place(x=80,y=100,relwidth=400,relheight=500)
        #======Register Frame=======
        frame2=Frame(self.root2,bg="white")
        frame2.place(x=40,y=159,width=650,height=470)
        
        titel=Label(frame2,text="SUB-COMPANY'S REGISTER HERE", font=("times new roman",20,"bold"),bg="white" ,fg="green").place(x=120,y=20)
        
        #---------------------------------------Row1
        c_id=Label(frame2,text="COMPANY-ID", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=220,y=70)
        self.txt_cid=Entry(frame2,font=("times new roman",15),bg="lightgray")
        self.txt_cid.place(x=220,y=100,width=250)
        
        #---------------------------------------Row2
        c_name=Label(frame2,text="SUB-COMPANY NAME", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=220,y=150)
        self.txt_cname=Entry(frame2,font=("times new roman",15),bg="lightgray")
        self.txt_cname.place(x=220,y=180,width=250)
        
        #---------------------------------------Row3
        ccity=Label(frame2,text="SUB-COMPANY CITY", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=220,y=230)
        self.txt_ccity=Entry(frame2,font=("times new roman",15),bg="lightgray")
        self.txt_ccity.place(x=220,y=260,width=250)
        
        #-------------------Terms-----------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame2,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",9,"bold"),bg="white",fg="gray").place(x=220,y=300)
        
        #-------------------buttons--------------------
        #self.btn_img=ImageTk.PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/submit.png")
        #btn=Button(frame2,image=self.btn_img,bd=0,cursor="hand2").place(x=20,y=575)
        btn1_register=Button(frame2, text="Submit Now",cursor="hand2",command=self.register_data2,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=70,y=340,width=150,height=35)
        btn2=Button(frame2, text="Cancel",cursor="hand2",command=self.cancel1,font=("arial",14,"bold"),bg="red",fg="white").place(x=250,y=340,width=150,height=35)
        btn3=Button(frame2, text="back to home>>>",cursor="hand2",command=self.back2,font=("arial",14,"bold"),bg="#DCDCDC",fg="black").place(x=220,y=397,width=200,height=35)
        btn4=Button(frame2, text="update",cursor="hand2",command=self.update2,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=430,y=340,width=150,height=35)
        
        
    def back2(self):
        self.root2.destroy()
        import main
        
    def cancel1(self):
        self.txt_cid.delete(0,END)
        self.txt_cname.delete(0,END)
        self.txt_ccity.delete(0,END)
        #clear checkbox
        self.var_chk.set(0)
        
    def register_data2(self):
        if self.txt_cid.get()=="" or self.txt_cname.get()=="" or self.txt_ccity.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root2)
        elif self.var_chk.get()==0:
            tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root2)
        
        elif(re.search('[a-zA-Z]$',self.txt_cid.get())):
            tm.showerror("Invalidate!" ,"COMPANY ID has to numerical value having length 2!")
        
        elif (len(self.txt_cid.get())<2) or (len(self.txt_cid.get())>2) or all(x.isalpha() or x.isspace() for x in self.txt_cid.get()):
            tm.showerror("Invalidate!" ,"COMPANY ID has to numerical value having length 2!")
        
        elif(re.search('[0-9]$',self.txt_cname.get())):
            tm.showerror("Invalidate!" ,"COMPANY NAME should be of alphabets only!")
        
        elif self.txt_cname.get().isdigit():
            tm.showerror("Invalidate!" ,"COMPANY NAME should be of alphabets only!")
        
        elif(re.search('[0-9]$',self.txt_ccity.get())):
            tm.showerror("Invalidate!" ,"COMPANY CITY should be of alphabets only!")
        
        elif self.txt_ccity.get().isdigit():
            tm.showerror("Invalidate!" ,"COMPANY CITY should be of alphabets only!")
        
        else:
            try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                cur.execute("select * from company where COMPANY_ID=%s",self.txt_cid.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    tm.showerror("Error","COMPANY_ID already exisits please try correct and new COMPANY_ID!",parent=self.root2)
                else:
                    cur.execute("insert into company(COMPANY_ID,COMPANY_NAME,COMPANY_CITY) values(%s,%s,%s)", 
                            (self.txt_cid.get(),
                             self.txt_cname.get(),
                             self.txt_ccity.get()
                             ))
                    con.commit()
                    con.close()
                    tm.showinfo("Success","Registertion successfull!",parent=self.root2)
                    #self.cancel1()
                
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root2)



    def update2(self):
        if self.txt_cid.get()=="" or self.txt_cname.get()=="" or self.txt_ccity.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root2)
        elif self.var_chk.get()==0:
            tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root2)
        
        elif(re.search('[a-zA-Z]$',self.txt_cid.get())):
            tm.showerror("Invalidate!" ,"COMPANY ID has to numerical value having length 2!")
        
        elif (len(self.txt_cid.get())<2) or (len(self.txt_cid.get())>2) or all(x.isalpha() or x.isspace() for x in self.txt_cid.get()):
            tm.showerror("Invalidate!" ,"COMPANY ID has to numerical value having length 2!")
        
        elif(re.search('[0-9]$',self.txt_cname.get())):
            tm.showerror("Invalidate!" ,"COMPANY NAME should be of alphabets only!")
        
        elif self.txt_cname.get().isdigit():
            tm.showerror("Invalidate!" ,"COMPANY NAME should be of alphabets only!")
        
        elif(re.search('[0-9]$',self.txt_ccity.get())):
            tm.showerror("Invalidate!" ,"COMPANY CITY should be of alphabets only!")
        
        elif self.txt_ccity.get().isdigit():
            tm.showerror("Invalidate!" ,"COMPANY CITY should be of alphabets only!")
        
        else:
            try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                 
                cur.execute("update company set COMPANY_NAME=%s,COMPANY_CITY=%s where COMPANY_ID=%s",(
                    self.txt_cname.get(),
                    self.txt_ccity.get(),
                    self.txt_cid.get()
                    ))
            
                con.commit()
                con.close()
                tm.showinfo("Success","COMPANYS DATA IS update2D SUCCESSFULLY!",parent=self.root2)
            
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root2)
   
    
obj=Register(root2)
root2.mainloop()