# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:49:21 2020

@author: UPMANYU JHA
"""

from tkinter import*
from PIL import ImageTk, Image # pip install pillow
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import tkinter.messagebox as tm
import re
# For connenction on mysql database in python
import pymysql
# For processing date and time variable
from datetime import datetime
import pandas as pd
from pandastable import Table, TableModel
import csv

root4=Tk()
root4.iconbitmap("C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly
class Register:
    def __init__(self,root4):
        self.root4=root4
        self.root4.title("SUB-COMPANY'S REGISTRATION WINDOW")
        self.root4.geometry("1350x790+40+40")
        #======Bg Image======
    
        self.bg4=PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/orders.png")
        bg4=Label(self.root4,image=self.bg4).place(x=350,y=0,relwidth=1,relheight=1)
        
        #======Left Image======
        
        #self.left=PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/mp1.png")
        #left=Label(self.root4,image=self.left).place(x=80,y=100,relwidth=400,relheight=500)
        #======Register Frame=======
        frame4=Frame(self.root4,bg="white")
        frame4.place(x=30,y=120,width=660,height=575)
        titel=Label(frame4,text="CUSTOMER'S ORDER DETAILS HERE", font=("times new roman",20,"bold"),bg="white" ,fg="green").place(x=10,y=10)
            
        #---------------------------------------Row1
    
        a_code=Label(frame4,text="AGENT-CODE", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=70)
        self.txt_acode=Entry(frame4,font=("times new roman",15),bg="lightgray")
        self.txt_acode.place(x=40,y=100,width=250)
        #self.txt_acode.bind("<Tab>", lambda event: register_data4(event, "AGENT-CODE"))

        orderno=Label(frame4,text="ORD_NUM", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=70)
        self.txt_orderno=Entry(frame4,font=("times new roman",15),bg="lightgray")
        self.txt_orderno.place(x=370,y=100,width=250)
        #---------------------------------------Row2
        c_code=Label(frame4,text="CUST_CODE", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=150)
        self.txt_ccode=Entry(frame4,font=("times new roman",15),bg="lightgray")
        self.txt_ccode.place(x=40,y=180,width=250)
        
        ORD_DATE = StringVar()
        odate=Label(frame4,text="ORD_DATE", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=150)
        self.txt_odate=DateEntry(frame4,textvariable=ORD_DATE, date_pattern="y-mm-dd",font=("times new roman",15,"bold"),bg="gray",fg="balck",bd="gray" )
        self.txt_odate.place(x=370,y=180,width=250)
        
        #---------------------------------------Row3
        orderamt=Label(frame4,text="ORD_AMOUNT", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=230)
        self.txt_orderamt=Entry(frame4,font=("times new roman",15),bg="lightgray")
        self.txt_orderamt.place(x=40,y=260,width=250)
        
        advamt=Label(frame4,text="ADVANCE_AMOUNT", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=230)
        self.txt_advamt=Entry(frame4,font=("times new roman",15),bg="lightgray")
        self.txt_advamt.place(x=370,y=260,width=250)
        
        #---------------------------------------Row4
        odrdtion=Label(frame4,text="ORDER DESCRIPTION", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=200,y=310)
        self.txt_odrdtion=Entry(frame4,font=("times new roman",15),bg="lightgray")
        self.txt_odrdtion.place(x=200,y=340,width=250)
        #-------------------Terms-----------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame4,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",9,"bold"),bg="white",fg="gray").place(x=200,y=380)
                    
        #-------------------buttons--------------------
        #btn_img=ImageTk.PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/submit.png")
        #btn=Button(frame4,image=btn_img,bd=0,cursor="hand2").place(x=20,y=575)
        btn1_register=Button(frame4, text="Submit Now",cursor="hand2",command=self.register_data4,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=70,y=420,width=150,height=35)
        btn2_cancel4=Button(frame4, text="Cancel",cursor="hand2",command=self.cancel4,font=("arial",14,"bold"),bg="red",fg="white").place(x=250,y=420,width=150,height=35)
        btn3_read=Button(frame4, text="Read Data",cursor="hand2",command=self.read_data,font=("arial",14,"bold"),bg="gray",fg="black").place(x=250,y=470,width=150,height=35)
        btn4=Button(frame4, text="search",cursor="hand2",command=self.search4,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=430,y=420,width=150,height=35)
        btn5=Button(frame4, text="back to home>>>",cursor="hand2",command=self.back4,font=("arial",14,"bold"),bg="#DCDCDC",fg="black").place(x=220,y=520,width=200,height=35)
        
        
    def back4(self):
        self.root4.destroy()
        #import main
        
        
    def search4(self):
        self.root4.destroy()
        import searchupdate
        
        
        
    def write_to_csv(self,df):
        df.to_csv(r'SRS REPORT HIGHLIGHTS.csv')
           
            
    def read_data(self):
        readwindow = Tk()
        readwindow.iconbitmap("C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever anyone saves this folder plz make a not to change its addres accordingly
        readwindow.title("Report Highlights")
        readwindow.geometry("800x600+40+40")
        
        frame2 = Frame(readwindow)
        l = Label(readwindow,text='Here are the Report Highlights',font=("times new roman",15,"bold"),bg="#154360",fg="#FDFEFE")
        l.place(x=270,y=10)
        #print(df)
        df = pd.DataFrame()
        df = TableModel.getSampleData()
        
        pt = Table(frame2)
        
        con = pymysql.connect(user="root4", password="", host="localhost", database="sales")
        cur = con.cursor()
        # Excuting insert query
        query = "select orders.AGENT_CODE,agents.AGENT_NAME,orders.ORD_NUM,orders.ORD_AMOUNT,orders.ADVANCE_AMOUNT,orders.ORD_DATE,orders.CUST_CODE,orders.ORD_DESCRIPTION from orders inner join agents on orders.AGENT_CODE=agents.AGENT_CODE"
        cur.execute(query)
        #print(cur.fetchall())
        #print(df)
        df = pd.DataFrame(list(cur.fetchall()),columns =['AGENT_CODE','AGENT_NAME','ORD_NUM','ORD_AMOUNT','ADVANCE_AMOUNT','ORD_DATE','CUST_CODE','ORD_DESCRIPTION']) #,'AGENT_NAME'
        #print (df)
        csv_button = Button(readwindow, text="Print to Excel",cursor="hand2",command=self.write_to_csv(df),font=("arial",14,"bold"),bg="#32CD32",fg="white")
        csv_button.place(x=270,y=490,width=250,height=35)
        
        table =Table(frame2, dataframe=df,showtoolbar=True,showstatusbar=True)
        table.currwidth=700
        table.currheight=500
        frame2.place(x=110,y=70)
        table.show()

        con.close()
    
    def cancel4(self):
        self.txt_orderno.delete(0,END)
        self.txt_orderamt.delete(0,END)
        self.txt_advamt.delete(0,END)
        self.txt_odate.delete(0,END)
        self.txt_ccode.delete(0,END)
        self.txt_acode.delete(0,END)
        self.txt_odrdtion.delete(0,END)
        #clear checkbox
        self.var_chk.set(0)
        
    def register_data4(self):
        if self.txt_acode.get()=="" or self.txt_orderno.get()=="" or self.txt_ccode.get()=="" or self.txt_odate.get()=="" or self.txt_orderamt.get()=="" or self.txt_advamt.get()=="" or self.txt_odrdtion.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root4)
        elif self.var_chk.get()==0:
            tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root4)
        elif(re.search4('[a-zA-Z]$',self.txt_acode.get())):
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumeric having length 4!",parent=self.root4)
        elif (len(self.txt_acode.get())<4) or (len(self.txt_acode.get())>4) or all(x.isalpha() or x.isspace() for x in self.txt_acode.get()):
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumeric having length 4!",parent=self.root4)
        elif(re.search4('[a-zA-Z]$',self.txt_orderno.get())):
            tm.showerror("Invalidate!" ,"ORD_NUMBER Are Required to be of 6 digits only!",parent=self.root4)
        elif (len(self.txt_orderno.get())<6) or (len(self.txt_orderno.get())>6) or all(x.isalpha() or x.isspace() for x in self.txt_orderno.get()):
            tm.showerror("Invalidate!" ,"ORD_NUMBER Are Required to be of 6 digits only!",parent=self.root4)
        elif (len(self.txt_ccode.get())<6) or (len(self.txt_ccode.get())>6) or all(x.isalpha() or x.isspace() for x in self.txt_ccode.get()):
            tm.showerror("Invalidate!" ,"CUSTOMER_CODE has to alphanumeric having length 6!",parent=self.root4)
        elif(re.search4('[0-9a-z0-9]$',self.txt_odrdtion.get())):
            tm.showerror("Invalidate!" ,"ORD_DESCRIPTION has to be CAPITAL alphabets only!",parent=self.root4)
        elif self.txt_odrdtion.get().isdigit():
            tm.showerror("Invalidate!" ,"ORD_DESCRIPTION has to be CAPITAL alphabets only!",parent=self.root4)
        elif(re.search4('[a-zA-Z]$',self.txt_orderamt.get())):
            tm.showerror("Invalidate!" ,"ORD_AMOUNT has to numbers only",parent=self.root4)
        elif all(x.isalpha() or x.isspace() for x in self.txt_orderamt.get()):
            tm.showerror("Invalidate!" ,"ORD_AMOUNT has to numbers only",parent=self.root4)
        elif(re.search4('[a-zA-Z]$',self.txt_advamt.get())):
            tm.showerror("Invalidate!" ,"ADVANCE_AMOUNT has to numbers only!",parent=self.root4)
        elif all(x.isalpha() or x.isspace() for x in self.txt_advamt.get()):
            tm.showerror("Invalidate!" ,"ADVANCE_AMOUNT has to numbers only!",parent=self.root4)
        elif(re.search4('[a-zA-Z]$',self.txt_odate.get())):
            tm.showerror("Invalidate!" ,"ORD_DATE stritly has to be in yyyy/mm/dd format only!",parent=self.root4)
        elif all(x.isalpha() or x.isspace() for x in self.txt_odate.get()):
            tm.showerror("Invalidate!" ,"ORD_DATE stritly has to be in yyyy/mm/dd format only!",parent=self.root4)
        else:
            try:
                ORD_DATE = datetime.strptime(self.txt_odate.get(), '%Y-%m-%d')
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                curr = con.cursor()
                curs = con.cursor()
                cur.execute("select * from customer where CUST_CODE=%s",self.txt_ccode.get())
                curs.execute("select * from agents where AGENT_CODE=%s",self.txt_acode.get())
                curr.execute("select * from orders where ORD_NUM=%s",self.txt_orderno.get())
                row=cur.fetchone()
                roww=curr.fetchone()
                rowww=curs.fetchone()
                #print(row)
                if row==None:
                    tm.showerror("Error","CUSTOMER_CODE Doesn't existes plz check the code again!!!",parent=self.root4)
                elif rowww==None:
                    tm.showerror("Error","Agent Doesn't existes plz check the code again!!!",parent=self.root4)
                elif roww!=None:
                    tm.showerror("Error","Order no. already exisits please try correct and new order no.!",parent=self.root4)
                else:
                    cur.execute("insert into orders(ORD_NUM,ORD_AMOUNT,ADVANCE_AMOUNT,ORD_DATE,CUST_CODE,AGENT_CODE,ORD_DESCRIPTION) values(%s,%s,%s,%s,%s,%s,%s)", 
                            (self.txt_orderno.get(),
                             self.txt_orderamt.get(),
                             self.txt_advamt.get(),
                             ORD_DATE.strftime("%Y-%m-%d"),
                             self.txt_ccode.get(),
                             self.txt_acode.get(),
                             self.txt_odrdtion.get()
                             ))
                    con.commit()
                    con.close()
                    tm.showinfo("Success","Registertion successfull!",parent=self.root4)
                    self.cancel4()
                
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root4)

                
        
        
obj=Register(root4)
root4.mainloop()  
