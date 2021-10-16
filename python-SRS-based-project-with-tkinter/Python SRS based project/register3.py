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


root3=Tk()
root3.iconbitmap("C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class Register:
    def __init__(self,root3):
        self.root3=root3
        self.root3.title("AGENT'S REGISTRATION WINDOW")
        self.root3.geometry("1350x790+40+40")
        #======Bg Image======
        
        self.bg3=PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/hiclipart.com.png")
        bg3=Label(self.root3,image=self.bg3).place(x=350,y=0,relwidth=1,relheight=1)
        
        #======Register Frame=======
        frame3=Frame(self.root3,bg="white")
        frame3.place(x=30,y=10,width=660,height=700)
        
        titel=Label(frame3,text="CUSTOMER'S REGISTER HERE", font=("times new roman",20,"bold"),bg="white" ,fg="green").place(x=10,y=10)
        
        #---------------------------------------Row1
        a_code=Label(frame3,text="AGENT-CODE", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=70)
        self.txt_acode=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_acode.place(x=40,y=100,width=250)
        
        c_code=Label(frame3,text="CUSTOMER-CODE", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=70)
        self.txt_ccode=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_ccode.place(x=370,y=100,width=250)
        
        #---------------------------------------Row2
        c_name=Label(frame3,text="CUSTOMER NAME", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=150)
        self.txt_cname=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_cname.place(x=40,y=180,width=250)
        
        phone=Label(frame3,text="PHONE NO.", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=150)
        self.txt_phone=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_phone.place(x=370,y=180,width=250)
        
        #---------------------------------------Row3
        c_warea=Label(frame3,text="WORKING AREA", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=230)
        self.txt_cwarea=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_cwarea.place(x=40,y=260,width=250)
        
        gdcml=Label(frame3,text="GRADE DECIMAL", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=230)
        self.txt_gdcml=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_gdcml.place(x=370,y=260,width=250)
        
        #---------------------------------------Row4
        gcity=Label(frame3,text="CUSTOMER CITY", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=310)
        self.txt_gcity=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_gcity.place(x=40,y=340,width=250)
        
        ccntry=Label(frame3,text="CUSTOMER COUNTRY", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=310)
        self.txt_ccntry=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_ccntry.place(x=370,y=340,width=250)
        #self.cmb_quest=ttk.Combobox(frame3,font=("times new roman",13),state='readonly' ,justify=CENTER)
        #self.cmb_quest['values']=("Select","ACD","AN","WKG")
        #self.cmb_quest.place(x=40,y=340,width=250)
        #self.cmb_quest.current(0)# to make select as by-default
        
        #---------------------------------------Row5
        oamt=Label(frame3,text="OPENING AMT", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=390)
        self.txt_oamt=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_oamt.place(x=40,y=420,width=250)
        
        ramt=Label(frame3,text="RECEIVE AMT", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=390)
        self.txt_ramt=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_ramt.place(x=370,y=420,width=250)
        
        #---------------------------------------Row6
        pamt=Label(frame3,text="PAYMENT AMT", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=470)
        self.txt_pamt=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_pamt.place(x=40,y=500,width=250)
        
        ostamt=Label(frame3,text="OUTSTANDING AMT", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=470)
        self.txt_ostamt=Entry(frame3,font=("times new roman",15),bg="lightgray")
        self.txt_ostamt.place(x=370,y=500,width=250)
        
        #-------------------Terms-----------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame3,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",9,"bold"),bg="white",fg="gray").place(x=40,y=540)
        
        #-------------------buttons--------------------
        #self.btn_img=ImageTk.PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/submit.png")
        #btn=Button(frame3,image=self.btn_img,bd=0,cursor="hand2").place(x=20,y=575)
        btn1=Button(frame3, text="Submit Now",cursor="hand2",command=self.register_data3,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=78,y=580,width=150,height=35)
        btn2=Button(frame3, text="cancel",cursor="hand2",command=self.cancel3,font=("arial",14,"bold"),bg="red",fg="white").place(x=253,y=580,width=150,height=35)
        #btn3=Button(frame3, text="update3",cursor="hand2",font=("arial",14,"bold"),bg="#FF8C00",fg="black").place(x=460,y=580,width=150,height=35)
        btn3=Button(frame3, text="back to home>>>",cursor="hand2",command=self.back3,font=("arial",14,"bold"),bg="#DCDCDC",fg="black").place(x=228,y=630,width=200,height=35)
        btn4=Button(frame3, text="update",cursor="hand2",command=self.update3,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=430,y=580,width=150,height=35)
        
        
    def back3(self):
        self.root3.destroy()
        import main
    
        
    def cancel3(self):
        self.txt_acode.delete(0,END)
        self.txt_ccode.delete(0,END)
        self.txt_cname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_cwarea.delete(0,END)
        self.txt_gdcml.delete(0,END)
        self.txt_gcity.delete(0,END)
        self.txt_ccntry.delete(0,END)
        self.txt_oamt.delete(0,END)
        self.txt_ramt.delete(0,END)
        self.txt_pamt.delete(0,END)
        self.txt_ostamt.delete(0,END)
        #clear checkbox
        self.var_chk.set(0)
        
    def register_data3(self):
        if self.txt_acode.get()=="" or self.txt_ccode.get()=="" or self.txt_cname.get()=="" or self.txt_phone.get()=="" or self.txt_cwarea.get()=="" or self.txt_gdcml.get()=="" or self.txt_gcity.get()=="" or self.txt_ccntry.get()=="" or self.txt_oamt.get()=="" or self.txt_ramt.get()=="" or self.txt_pamt.get()=="" or self.txt_ostamt.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root3)
        elif self.var_chk.get()==0:
            tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root3)
        #elif(re.search('[a-zA-Z]$',self.txt_acode.get())):
            #tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumeric having length 4!",parent=self.root3)
        #elif (len(self.txt_acode.get())<4) or (len(self.txt_acode.get())>4) or all(x.isalpha() or x.isspace() for x in self.txt_acode.get()):
            #tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumeric having length 4!",parent=self.root3)
        #elif(re.match("(?=.*[*.!#@$%^&(){}[]:;<>,.?/~_+-=|\])",self.txt_acode.get())):
            #tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumeric having length 4!",parent=self.root3)
        elif(re.search('[0-9]$',self.txt_cname.get())):
            tm.showerror("Invalidate!" ,"CUSTOMER_NAME has to alphabets only!",parent=self.root3)
        elif self.txt_cname.get().isdigit():
            tm.showerror("Invalidate!" ,"CUSTOMER_NAME has to alphabets only!",parent=self.root3)
        elif(re.search('[0-9]$',self.txt_cwarea.get())):
            tm.showerror("Invalidate!" ,"CUSTOMER WORKING AREA has to alphanumeric or alphabet values only!",parent=self.root3)
        elif self.txt_cwarea.get().isdigit():
            tm.showerror("Invalidate!" ,"CUSTOMER WORKING AREA has to alphanumeric or alphabet values only!",parent=self.root3)
        elif (len(self.txt_gdcml.get())<0) or (len(self.txt_gdcml.get())>1) or all(x.isalpha() or x.isspace() for x in self.txt_gdcml.get()):
            tm.showerror("Invalidate!" ,"GRADE has to be 1 digit no. only only!",parent=self.root3)
        elif(re.search('[0-9]$',self.txt_gcity.get())):
            tm.showerror("Invalidate!","CUST_CITY field should contain alphabets only!",parent=self.root3)
        elif self.txt_gcity.get().isdigit():
            tm.showerror("Invalidate!","CUST_CITY field should contain alphabets only!",parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_oamt.get())):
            tm.showerror("Invalidate!" ,"OPENING_AMOUNT has to numbers only",parent=self.root3)
        elif all(x.isalpha() or x.isspace() for x in self.txt_oamt.get()):
            tm.showerror("Invalidate!" ,"OPENING_AMOUNT has to numbers only",parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_ramt.get())):
            tm.showerror("Invalidate!" ,"RECEIVE_AMOUNT has to numbers only!",parent=self.root3)
        elif all(x.isalpha() or x.isspace() for x in self.txt_ramt.get()):
            tm.showerror("Invalidate!" ,"RECEIVE_AMOUNT has to numbers only!",parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_pamt.get())):
            tm.showerror("Invalidate!" ,"PAYMENT_AMOUNT has to numbers only!",parent=self.root3)
        elif all(x.isalpha() or x.isspace() for x in self.txt_pamt.get()):
            tm.showerror("Invalidate!" ,"PAYMENT_AMOUNT has to numbers only!",parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_ostamt.get())):
            tm.showerror("Invalidate!" ,"OUTSTANDING_AMOUNT has to numbers only!",parent=self.root3)
        elif all(x.isalpha() or x.isspace() for x in self.txt_ostamt.get()):
            tm.showerror("Invalidate!" ,"OUTSTANDING_AMOUNT has to numbers only!",parent=self.root3)
       # elif(re.search('[a-zA-Z]$',self.txt_phone.get())):
        #    tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
        #elif (len(self.txt_phone.get())<10) or (len(self.txt_phone.get())>10) or all(x.isalpha() or x.isspace() for x in self.txt_phone.get()):
         #   tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_ccode.get())):
            tm.showerror("Invalidate!" ,"CUSTOMER_CODE has to alphanumeric having length 6!",parent=self.root3)
        elif (len(self.txt_ccode.get())<6) or (len(self.txt_ccode.get())>6) or all(x.isalpha() or x.isspace() for x in self.txt_ccode.get()):
            tm.showerror("Invalidate!" ,"CUSTOMER_CODE has to alphanumeric having length 6!",parent=self.root3)
        elif(re.search('[0-9]$',self.txt_ccntry.get())):
            tm.showerror("Invalidate!" ,"CUST_COUNTRY field should contain alphabets only!",parent=self.root3)
        elif self.txt_ccntry.get().isdigit():
            tm.showerror("Invalidate!" ,"CUST_COUNTRY field should contain alphabets only!",parent=self.root3)
        else:
            try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                curs = con.cursor()
                cur.execute("select * from customer where CUST_CODE=%s and PHONE_NO=%s",(self.txt_ccode.get(),self.txt_phone.get()))
                row=cur.fetchone()
                curs.execute("select * from agents where AGENT_CODE=%s",self.txt_acode.get())
                roww=curs.fetchone()
                #print(row)
                if row!=None:
                    tm.showerror("Error","CUSTOMER_CODE/PHONE_NO. already exisits please try correct and new CUSTOMER_CODE!")
                elif roww==None:
                    tm.showerror("Error","Agent Doesn't existes plz check the code again!!!",parent=self.root3)
                elif(re.search(r'\d{3}-\d{3}-\d{4}', self.txt_phone.get())):
                    cur.execute("insert into customer(CUST_CODE,CUST_NAME,CUST_CITY,WORKING_AREA,CUST_COUNTRY,GRADE,OPENING_AMT,RECEIVE_AMT,PAYMENT_AMT,OUTSTANDING_AMT,PHONE_NO,AGENT_CODE) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", 
                            (self.txt_ccode.get(),
                             self.txt_cname.get(),
                             self.txt_gcity.get(),
                             self.txt_cwarea.get(),
                             self.txt_ccntry.get(),
                             self.txt_gdcml.get(),
                             self.txt_oamt.get(),
                             self.txt_ramt.get(),
                             self.txt_pamt.get(),
                             self.txt_ostamt.get(),
                             self.txt_phone.get(),
                             self.txt_acode.get()
                             ))
                    con.commit()
                    con.close()
                    tm.showinfo("Success","Registertion successfull!",parent=self.root3)
                    #self.cancel3()
                else:
                    tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root3)

    def update3(self):
        if self.txt_acode.get()=="" or self.txt_ccode.get()=="" or self.txt_cname.get()=="" or self.txt_phone.get()=="" or self.txt_cwarea.get()=="" or self.txt_gdcml.get()=="" or self.txt_gcity.get()=="" or self.txt_ccntry.get()=="" or self.txt_oamt.get()=="" or self.txt_ramt.get()=="" or self.txt_pamt.get()=="" or self.txt_ostamt.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root3)
        elif self.var_chk.get()==0:
            tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root3)
        #elif(re.search('[a-zA-Z]$',self.txt_acode.get())):
            #tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumeric having length 4!",parent=self.root3)
        #elif (len(self.txt_acode.get())<4) or (len(self.txt_acode.get())>4) or all(x.isalpha() or x.isspace() for x in self.txt_acode.get()):
            #tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumeric having length 4!",parent=self.root3)
        elif(re.search('[0-9]$',self.txt_cname.get())):
            tm.showerror("Invalidate!" ,"CUSTOMER_NAME has to alphabets only!",parent=self.root3)
        elif self.txt_cname.get().isdigit():
            tm.showerror("Invalidate!" ,"CUSTOMER_NAME has to alphabets only!",parent=self.root3)
        elif(re.search('[0-9]$',self.txt_cwarea.get())):
            tm.showerror("Invalidate!" ,"CUSTOMER WORKING AREA has to alphanumeric or alphabet values only!",parent=self.root3)
        elif self.txt_cwarea.get().isdigit():
            tm.showerror("Invalidate!" ,"CUSTOMER WORKING AREA has to alphanumeric or alphabet values only!",parent=self.root3)
        elif (len(self.txt_gdcml.get())<0) or (len(self.txt_gdcml.get())>1) or all(x.isalpha() or x.isspace() for x in self.txt_gdcml.get()):
            tm.showerror("Invalidate!" ,"GRADE has to be 1 digit no. only only!",parent=self.root3)
        elif(re.search('[0-9]$',self.txt_gcity.get())):
            tm.showerror("Invalidate!","CUST_CITY field should contain alphabets only!",parent=self.root3)
        elif self.txt_gcity.get().isdigit():
            tm.showerror("Invalidate!","CUST_CITY field should contain alphabets only!",parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_oamt.get())):
            tm.showerror("Invalidate!" ,"OPENING_AMOUNT has to numbers only",parent=self.root3)
        elif all(x.isalpha() or x.isspace() for x in self.txt_oamt.get()):
            tm.showerror("Invalidate!" ,"OPENING_AMOUNT has to numbers only",parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_ramt.get())):
            tm.showerror("Invalidate!" ,"RECEIVE_AMOUNT has to numbers only!",parent=self.root3)
        elif all(x.isalpha() or x.isspace() for x in self.txt_ramt.get()):
            tm.showerror("Invalidate!" ,"RECEIVE_AMOUNT has to numbers only!",parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_pamt.get())):
            tm.showerror("Invalidate!" ,"PAYMENT_AMOUNT has to numbers only!",parent=self.root3)
        elif all(x.isalpha() or x.isspace() for x in self.txt_pamt.get()):
            tm.showerror("Invalidate!" ,"PAYMENT_AMOUNT has to numbers only!",parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_ostamt.get())):
            tm.showerror("Invalidate!" ,"OUTSTANDING_AMOUNT has to numbers only!",parent=self.root3)
        elif all(x.isalpha() or x.isspace() for x in self.txt_ostamt.get()):
            tm.showerror("Invalidate!" ,"OUTSTANDING_AMOUNT has to numbers only!",parent=self.root3)
     #   elif(re.search('[a-zA-Z]$',self.txt_phone.get())):
      #      tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
       # elif (len(self.txt_phone.get())<10) or (len(self.txt_phone.get())>10) or all(x.isalpha() or x.isspace() for x in self.txt_phone.get()):
        #    tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
        elif(re.search('[a-zA-Z]$', self.txt_ccode.get())):
            tm.showerror("Invalidate!" ,"CUSTOMER_CODE has to alphanumeric having length 6!",parent=self.root3)
        elif (len(self.txt_ccode.get())<6) or (len(self.txt_ccode.get())>6) or all(x.isalpha() or x.isspace() for x in self.txt_ccode.get()):
            tm.showerror("Invalidate!" ,"CUSTOMER_CODE has to alphanumeric having length 6!",parent=self.root3)
        elif(re.search('[0-9]$',self.txt_ccntry.get())):
            tm.showerror("Invalidate!" ,"CUST_COUNTRY field should contain alphabets only!",parent=self.root3)
        elif self.txt_ccntry.get().isdigit():
            tm.showerror("Invalidate!" ,"CUST_COUNTRY field should contain alphabets only!",parent=self.root3)
        else:
            try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                curs = con.cursor()
                cur.execute("select * from customer where CUST_CODE=%s",self.txt_ccode.get())
                row1=cur.fetchone()
                curs.execute("select * from agents where AGENT_CODE=%s",self.txt_acode.get())
                roww1=curs.fetchone()
                #print(row)
                if row1==None:
                    tm.showerror("Error","CUSTOMER_CODE can't be updated as per the laws!",parent=self.root3)
                elif roww1==None:
                    tm.showerror("Error","Agent Doesn't existes plz check the code again!!!",parent=self.root3)
                elif(re.search(r'\d{3}-\d{3}-\d{4}', self.txt_phone.get())):
                    cur.execute("update customer set CUST_NAME=%s,CUST_CITY=%s,WORKING_AREA=%s,CUST_COUNTRY=%s,GRADE=%s,OPENING_AMT=%s,RECEIVE_AMT=%s,PAYMENT_AMT=%s,OUTSTANDING_AMT=%s,PHONE_NO=%s,AGENT_CODE=%s where CUST_CODE=%s",(
                        self.txt_cname.get(),
                        self.txt_gcity.get(),
                        self.txt_cwarea.get(),
                        self.txt_ccntry.get(),
                        self.txt_gdcml.get(),
                        self.txt_oamt.get(),
                        self.txt_ramt.get(),
                        self.txt_pamt.get(),
                        self.txt_ostamt.get(),
                        self.txt_phone.get(),
                        self.txt_acode.get(),
                        self.txt_ccode.get()
                        ))
                    con.commit()
                    con.close()
                    tm.showinfo("Success","REGISTRATION update3D SUCCESSFULLY!",parent=self.root3)
                    self.cancel3()
                else:
                    tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
            
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root3)

                
        




obj=Register(root3)
root3.mainloop()