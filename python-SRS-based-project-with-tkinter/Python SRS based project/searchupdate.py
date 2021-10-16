# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:39:13 2020

@author: UPMANYU JHA
"""

from tkinter import*
from PIL import ImageTk, Image # pip install pillow
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import tkinter.messagebox as tm
# For connenction on mysql database in python
import pymysql
import re
# For processing date and time variable
from datetime import datetime
import pandas as pd
from pandastable import Table, TableModel
import csv

root5=Tk()
root5.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class Searchedit:
    def __init__(self,root5):
        self.root5=root5
        self.root5.title("SRS Search and update5 WINDOW")
        self.root5.geometry("1350x790+40+40")
        
        title=Label(self.root5,text="Search or update order's",bd=10,relief=GROOVE, font=("times new roman",40,"bold"),bg="#FF4500" ,fg="white")
        title.pack(side=TOP,fill=X)
        
        
        #===========All Variables=================
        self.ORD_NUM_var=StringVar()
        self.ORD_AMOUNT_var=IntVar()#StringVar()
        self.ADVANCE_AMOUNT_var=IntVar()#StringVar()
        self.BALANCE_AMOUNT_var=StringVar()
        self.CUST_CODE_var=StringVar()
        self.AGENT_CODE_var=StringVar()
        self.AGENT_NAME_var=StringVar()
        self.ORD_DESCRIPTION_var=StringVar()
        
        
        self.search_by=StringVar()
        self.search_txt=StringVar()
        
        #=========Manage and update Frame================
        Manage_Frame=Frame(self.root5,bd=4,relief=RIDGE,bg="#FFA07A")
        Manage_Frame.place(x=10,y=100,width=480,height=650)
        
        m_title=Label(Manage_Frame,bg="#FFA07A",fg="white",text="update and Manage Orders", font=("times new roman",21,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        lb1_onumbr=Label(Manage_Frame,bg="#FFA07A",fg="white",text="ORDER NO.", font=("times new roman",15,"bold"))
        lb1_onumbr.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_onumbr=Entry(Manage_Frame,textvariable=self.ORD_NUM_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_onumbr.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lb1_oamt=Label(Manage_Frame,bg="#FFA07A",fg="white",text="ORDER_AMT", font=("times new roman",15,"bold"))
        lb1_oamt.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_oamt=Entry(Manage_Frame,textvariable=self.ORD_AMOUNT_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_oamt.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lb1_aamt=Label(Manage_Frame,bg="#FFA07A",fg="white",text="ADVANCE_AMT", font=("times new roman",15,"bold"))
        lb1_aamt.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_aamt=Entry(Manage_Frame,textvariable=self.ADVANCE_AMOUNT_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_aamt.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lb1_odate=Label(Manage_Frame,bg="#FFA07A",fg="white",text="ORDER_DATE", font=("times new roman",15,"bold"))
        lb1_odate.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        ORD_DATE = StringVar()
        self.txt_odate=DateEntry(Manage_Frame,textvariable=ORD_DATE, date_pattern="y-mm-dd",font=("times new roman",22,"bold"),bg="#FFA07A",fg="white",bd=5,relief=GROOVE)
        self.txt_odate.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        
        lb1_ccode=Label(Manage_Frame,bg="#FFA07A",fg="white",text="CUST_CODE", font=("times new roman",15,"bold"))
        lb1_ccode.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_ccode=Entry(Manage_Frame,textvariable=self.CUST_CODE_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_ccode.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        lb1_ods=Label(Manage_Frame,bg="#FFA07A",fg="white",text="ORD_DESCRIPTION", font=("times new roman",15,"bold"))
        lb1_ods.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_ods=Entry(Manage_Frame,textvariable=self.ORD_DESCRIPTION_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_ods.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        lb1_bamt=Label(Manage_Frame,bg="#FFA07A",fg="white",text="BALANCE_AMT", font=("times new roman",15,"bold"))
        lb1_bamt.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        txt_bamt=Entry(Manage_Frame,textvariable=self.BALANCE_AMOUNT_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE,state='readonly')
        txt_bamt.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        Calbalbtn=Button(Manage_Frame,text="Cal",cursor="hand2",width=4,height=1,bd=6,command=self.bal).grid(row=7,column=1,padx=20,pady=10,sticky=E)
        
        
        lb1_aname=Label(Manage_Frame,bg="#FFA07A",fg="white",text="AGENT_NAME", font=("times new roman",15,"bold"))
        lb1_aname.grid(row=8,column=0,pady=10,padx=20,sticky="w")
        txt_aname=Entry(Manage_Frame,textvariable=self.AGENT_NAME_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_aname.grid(row=8,column=1,pady=10,padx=20,sticky="w")
        
        lb1_acode=Label(Manage_Frame,bg="#FFA07A",fg="white",text="AGENT_CODE", font=("times new roman",15,"bold"))
        lb1_acode.grid(row=9,column=0,pady=10,padx=20,sticky="w")
        txt_acode=Entry(Manage_Frame,textvariable=self.AGENT_CODE_var, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_acode.grid(row=9,column=1,pady=10,padx=20,sticky="w")
        
        #========Button Frame=====================
        
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#FFA07A")
        btn_Frame.place(x=33,y=580,width=408)
        
        Addbtn=Button(btn_Frame,text="Add",cursor="hand2",width=10,command=self.add).grid(row=0,column=0,padx=10,pady=10)
        update5btn=Button(btn_Frame,text="update",cursor="hand2",width=10,command=self.update5).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",cursor="hand2",width=10,command=self.delete).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",cursor="hand2",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        
        #========Details and search Frame=========
        Detail_Frame=Frame(self.root5,bd=4,relief=RIDGE,bg="#FFA07A")
        Detail_Frame.place(x=536,y=100,width=804,height=650)
        
        #lb1_search=Label(Detail_Frame,bg="#FFA07A",fg="white",text="Search by", font=("times new roman",15,"bold"))
        #lb1_search.grid(row=0,column=0,pady=10,padx=10,sticky="w")
        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=13,font=("times new roman",15,"bold"),state='readonly')
        combo_search['values']=("Search By >>>","ORD_NUM","ORD_DATE","CUST_CODE")
        combo_search.grid(row=0,column=1,padx=5,pady=10)
        combo_search.current(0)
        
        txt_search=Entry(Detail_Frame,textvariable=self.search_txt, font=("times new roman",14,"bold"),width=32,bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=10,sticky="w")
       
        #search_img=ImageTk.PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/sc.png")
        #searchbtn=Button(Detail_Frame,image=search_img,bd=0,cursor="hand2").grid(row=0,column=3,padx=5,pady=10)
        searchbtn=Button(Detail_Frame,command=self.searchdt,text="Search",cursor="hand2",width=10,pady=5).grid(row=0,column=3,padx=5,pady=10)
        showallbtn=Button(Detail_Frame,command=self.fetch,text="Show All",cursor="hand2",width=10,pady=5).grid(row=0,column=4,padx=5,pady=10)
        btn3_read=Button(Detail_Frame, text="RD&P",cursor="hand2",command=self.read_data1,width=10,pady=5).grid(row=0,column=5,padx=5,pady=10)
        
        #=================Table Frame===================
        Table_Frame=Frame(Detail_Frame,bg="#FFA07A",bd=4,relief=RIDGE)
        Table_Frame.place(x=9,y=70,width=780,height=560)
        
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Searchedit_table=ttk.Treeview(Table_Frame,columns=("ORD_NUM","ORD_AMOUNT","ADVANCE_AMOUNT","BALANCE_AMOUNT","ORD_DATE","CUST_CODE","AGENT_CODE","AGENT_NAME","ORD_DESCRIPTION"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Searchedit_table.xview)
        scroll_y.config(command=self.Searchedit_table.yview)
        self.Searchedit_table.heading("ORD_NUM",text="ORD_NUM")
        self.Searchedit_table.heading("ORD_AMOUNT",text="ORD_AMOUNT")
        self.Searchedit_table.heading("ADVANCE_AMOUNT",text="ADVANCE_AMOUNT")
        self.Searchedit_table.heading("BALANCE_AMOUNT",text="BALANCE_AMOUNT")
        self.Searchedit_table.heading("ORD_DATE",text="ORD_DATE")
        self.Searchedit_table.heading("CUST_CODE",text="CUST_CODE")
        self.Searchedit_table.heading("AGENT_CODE",text="AGENT_CODE")
        self.Searchedit_table.heading("AGENT_NAME",text="AGENT_NAME")
        self.Searchedit_table.heading("ORD_DESCRIPTION",text="ORD_DESCRIPTION")
        self.Searchedit_table['show']='headings'
        self.Searchedit_table.column("ORD_NUM",width=100)
        self.Searchedit_table.column("ORD_AMOUNT",width=100)
        self.Searchedit_table.column("ADVANCE_AMOUNT",width=150)
        self.Searchedit_table.column("BALANCE_AMOUNT",width=150)
        self.Searchedit_table.column("ORD_DATE",width=100)
        self.Searchedit_table.column("CUST_CODE",width=100)
        self.Searchedit_table.column("AGENT_CODE",width=100)
        self.Searchedit_table.column("AGENT_NAME",width=120)
        self.Searchedit_table.column("ORD_DESCRIPTION",width=160)
        self.Searchedit_table.pack(fill=BOTH,expand=1)
        self.Searchedit_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch()
    def add(self):
        if self.AGENT_CODE_var.get()=="" or self.ORD_NUM_var.get()=="" or self.CUST_CODE_var.get()=="" or self.txt_odate.get()=="" or self.ORD_AMOUNT_var.get()=="" or self.ADVANCE_AMOUNT_var.get()=="" or self.ORD_DESCRIPTION_var.get()=="" or self.BALANCE_AMOUNT_var.get()=="" or self.AGENT_NAME_var.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root5)
        elif(re.search('[a-zA-Z]$',self.ORD_NUM_var.get())):
            tm.showerror("Invalidate!" ,"ORD_NUMBER Are Required to be of 6 digits only!",parent=self.root5)
        elif (len(self.ORD_NUM_var.get())<6) or (len(self.ORD_NUM_var.get())>6) or all(x.isalpha() or x.isspace() for x in self.ORD_NUM_var.get()):
            tm.showerror("Invalidate!" ,"ORD_NUMBER Are Required to be of 6 digits only!",parent=self.root5)
        #elif all(x.isalpha() or x.isspace() for x in self.ADVANCE_AMOUNT_var.get()):
            #tm.showerror("Invalidate!" ,"ADVANCE_AMOUNT has to numbers only!",parent=self.root5)
        elif(re.search('[a-zA-Z]$',self.BALANCE_AMOUNT_var.get())):
            tm.showerror("Invalidate!" ,"BALANCE_AMOUNT has to numbers only!",parent=self.root5)
        elif all(x.isalpha() or x.isspace() for x in self.BALANCE_AMOUNT_var.get()):
            tm.showerror("Invalidate!" ,"BALANCE_AMOUNT has to numbers only!",parent=self.root5)
        #elif all(x.isalpha() or x.isspace() for x in self.ORD_AMOUNT_var.get()):
           # tm.showerror("Invalidate!" ,"ORD_AMOUNT has to numbers only",parent=self.root5)
        elif(re.search('[a-zA-Z]$',self.txt_odate.get())):
            tm.showerror("Invalidate!" ,"ORD_DATE stritly has to be in yyyy-mm-dd format only!",parent=self.root5)
        elif all(x.isalpha() or x.isspace() for x in self.txt_odate.get()):
            tm.showerror("Invalidate!" ,"ORD_DATE stritly has to be in yyyy-mm-dd format only!",parent=self.root5)
        elif (len(self.CUST_CODE_var.get())<6) or (len(self.CUST_CODE_var.get())>6) or all(x.isalpha() or x.isspace() for x in self.CUST_CODE_var.get()):
            tm.showerror("Invalidate!" ,"CUSTOMER_CODE has to alphanumeric having length 6!",parent=self.root5)
        elif(re.search('[0-9a-z0-9]$',self.ORD_DESCRIPTION_var.get())):
            tm.showerror("Invalidate!" ,"ORD_DESCRIPTION has to be CAPITAL alphabets only!",parent=self.root5)
        elif self.ORD_DESCRIPTION_var.get().isdigit():
            tm.showerror("Invalidate!" ,"ORD_DESCRIPTION has to be CAPITAL alphabets only!",parent=self.root5)
        elif (len(self.AGENT_CODE_var.get())<4) or (len(self.AGENT_CODE_var.get())>4) or all(x.isalpha() or x.isspace() for x in self.AGENT_CODE_var.get()):
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumeric having length 4!",parent=self.root5)    
        elif self.AGENT_NAME_var.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENT_NAME Are Required to be of alphabets only!",parent=self.root5)
        else:
            try:
                ORD_DATE = datetime.strptime(self.txt_odate.get(), '%Y-%m-%d')
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                curr = con.cursor()
                curs = con.cursor()
                curss = con.cursor()
                cur.execute("insert into orders1 (ORD_NUM,ORD_AMOUNT,ADVANCE_AMOUNT,ORD_DATE,CUST_CODE,AGENT_CODE,AGENT_NAME,ORD_DESCRIPTION) select orders.ORD_NUM,orders.ORD_AMOUNT,orders.ADVANCE_AMOUNT,orders.ORD_DATE,orders.CUST_CODE,orders.AGENT_CODE,agents.AGENT_NAME,orders.ORD_DESCRIPTION from orders inner join agents on orders.AGENT_CODE=agents.AGENT_CODE ")
                curs.execute("select * from agents where AGENT_CODE=%s and AGENT_NAME=%s",(self.AGENT_CODE_var.get(),self.AGENT_NAME_var.get()))
                curr.execute("select * from orders where ORD_NUM=%s",self.ORD_NUM_var.get())
                curss.execute("select * from customer where CUST_CODE=%s ",self.CUST_CODE_var.get())
                row=cur.fetchone()
                roww=curr.fetchone()
                rowww=curs.fetchone()
                roow= curss.fetchone()
                #print(row)
                
                if row!=None:
                    tm.showerror("Error","Order no. already exisits please try correct and new order no.!",parent=self.root5)
                elif roww!=None:
                    tm.showerror("Error","Order no. already exisits please try correct and new order no.!!!",parent=self.root5)
                elif rowww==None:
                    tm.showerror("Error","AGENT_CODE/AGENT_NAME Doesn't existes plz check the code again!!!",parent=self.root5)
                elif roow==None:
                    tm.showerror("Error","CUSTOMER_CODE doesn't exits plz enter the vaild code!!!",parent=self.root5)
                else:
                    cur.execute("insert into orders1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.ORD_NUM_var.get(),
                                                                                          self.ORD_AMOUNT_var.get(),
                                                                                          self.ADVANCE_AMOUNT_var.get(),
                                                                                          self.BALANCE_AMOUNT_var.get(),
                                                                                          ORD_DATE.strftime("%Y-%m-%d"),
                                                                                          self.CUST_CODE_var.get(),
                                                                                          self.AGENT_CODE_var.get(),
                                                                                          self.AGENT_NAME_var.get(),
                                                                                          self.ORD_DESCRIPTION_var.get()
                                                                                          ))
                    con.commit()
                    self.fetch()
                    self.clear()
                    con.close()
                    tm.showinfo("Success","Registertion successfull!",parent=self.root5)
                
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root5)


    # This fetch fun. is used to fetch data from db and diplay on the Table_Frame          
    def fetch(self):
        con = pymysql.connect(user="root", password="", host="localhost",database="sales")
        cur = con.cursor()
        cur.execute("select * from orders1 order by BALANCE_AMOUNT desc")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Searchedit_table.delete(*self.Searchedit_table.get_children())
            for row in rows:
                self.Searchedit_table.insert('',END,values=row)
            con.commit()
        con.close()
                
    def clear(self):
        self.ORD_NUM_var.set("")
        self.ORD_AMOUNT_var.set("")
        self.ADVANCE_AMOUNT_var.set("")
        self.BALANCE_AMOUNT_var.set("")
        self.CUST_CODE_var.set("")
        self.AGENT_CODE_var.set("")
        self.AGENT_NAME_var.set("")
        self.ORD_DESCRIPTION_var.set("")
        self.txt_odate.delete('0',END)
        
    def get_cursor(self,evt):
        cursor_row=self.Searchedit_table.focus()
        contents=self.Searchedit_table.item(cursor_row)
        row=contents['values']
        #print(row)
        self.ORD_NUM_var.set(row[0])
        self.ORD_AMOUNT_var.set(row[1])
        self.ADVANCE_AMOUNT_var.set(row[2])
        self.BALANCE_AMOUNT_var.set(row[3])
        self.CUST_CODE_var.set(row[5])
        self.AGENT_CODE_var.set(row[6])
        self.AGENT_NAME_var.set(row[7])
        self.ORD_DESCRIPTION_var.set(row[8])
        self.txt_odate.delete(0,END)
        self.txt_odate.insert(END,row[4])
    
    def update5(self):
        if self.AGENT_CODE_var.get()=="" or self.ORD_NUM_var.get()=="" or self.CUST_CODE_var.get()=="" or self.txt_odate.get()=="" or self.ORD_AMOUNT_var.get()=="" or self.ADVANCE_AMOUNT_var.get()=="" or self.ORD_DESCRIPTION_var.get()=="" or self.BALANCE_AMOUNT_var.get()=="" or self.AGENT_NAME_var.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root5)
        elif(re.search('[a-zA-Z]$',self.ORD_NUM_var.get())):
            tm.showerror("Invalidate!" ,"ORD_NUMBER Are Required to be of 6 digits only!",parent=self.root5)
        elif (len(self.ORD_NUM_var.get())<6) or (len(self.ORD_NUM_var.get())>6) or all(x.isalpha() or x.isspace() for x in self.ORD_NUM_var.get()):
            tm.showerror("Invalidate!" ,"ORD_NUMBER Are Required to be of 6 digits only!",parent=self.root5)
       # elif all(x.isalpha() or x.isspace() for x in self.ADVANCE_AMOUNT_var.get()):
         #   tm.showerror("Invalidate!" ,"ADVANCE_AMOUNT has to numbers only!",parent=self.root5)
        elif(re.search('[a-zA-Z]$',self.BALANCE_AMOUNT_var.get())):
            tm.showerror("Invalidate!" ,"BALANCE_AMOUNT has to numbers only!",parent=self.root5)
        elif all(x.isalpha() or x.isspace() for x in self.BALANCE_AMOUNT_var.get()):
            tm.showerror("Invalidate!" ,"BALANCE_AMOUNT has to numbers only!",parent=self.root5)
        #elif all(x.isalpha() or x.isspace() for x in self.ORD_AMOUNT_var.get()):
         #   tm.showerror("Invalidate!" ,"ORD_AMOUNT has to numbers only",parent=self.root5)
        elif(re.search('[a-zA-Z]$',self.txt_odate.get())):
            tm.showerror("Invalidate!" ,"ORD_DATE stritly has to be in yyyy-mm-dd format only!",parent=self.root5)
        elif all(x.isalpha() or x.isspace() for x in self.txt_odate.get()):
            tm.showerror("Invalidate!" ,"ORD_DATE stritly has to be in yyyy-mm-dd format only!",parent=self.root5)
        elif (len(self.CUST_CODE_var.get())<6) or (len(self.CUST_CODE_var.get())>6) or all(x.isalpha() or x.isspace() for x in self.CUST_CODE_var.get()):
            tm.showerror("Invalidate!" ,"CUSTOMER_CODE has to alphanumeric having length 6!",parent=self.root5)
        elif(re.search('[0-9a-z0-9]$',self.ORD_DESCRIPTION_var.get())):
            tm.showerror("Invalidate!" ,"ORD_DESCRIPTION has to be CAPITAL alphabets only!",parent=self.root5)
        elif self.ORD_DESCRIPTION_var.get().isdigit():
            tm.showerror("Invalidate!" ,"ORD_DESCRIPTION has to be CAPITAL alphabets only!",parent=self.root5)
        elif (len(self.AGENT_CODE_var.get())<4) or (len(self.AGENT_CODE_var.get())>4) or all(x.isalpha() or x.isspace() for x in self.AGENT_CODE_var.get()):
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumeric having length 4!",parent=self.root5)
        elif self.AGENT_NAME_var.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENT_NAME Are Required to be of alphabets only!",parent=self.root5)
        else:
            try:
                
                ORD_DATE = datetime.strptime(self.txt_odate.get(), '%Y-%m-%d')
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                curr = con.cursor()
                curs = con.cursor()
                curss = con.cursor()
                cur.execute("insert into orders1 (ORD_NUM,ORD_AMOUNT,ADVANCE_AMOUNT,ORD_DATE,CUST_CODE,AGENT_CODE,AGENT_NAME,ORD_DESCRIPTION) select orders.ORD_NUM,orders.ORD_AMOUNT,orders.ADVANCE_AMOUNT,orders.ORD_DATE,orders.CUST_CODE,orders.AGENT_CODE,agents.AGENT_NAME,orders.ORD_DESCRIPTION from orders inner join agents on orders.AGENT_CODE=agents.AGENT_CODE ")
                curs.execute("select * from agents where AGENT_CODE=%s and AGENT_NAME=%s",(self.AGENT_CODE_var.get(),self.AGENT_NAME_var.get()))
                curr.execute("select * from orders where ORD_NUM=%s",self.ORD_NUM_var.get())
                curss.execute("select * from customer where CUST_CODE=%s ",self.CUST_CODE_var.get())
                row=cur.fetchone()
                roww=curr.fetchone()
                rowww=curs.fetchone()
                roow= curss.fetchone()
                #print(row)
                
                if row!=None:
                    tm.showerror("Error","Order no. already exisits please try correct and new order no.!",parent=self.root5)
                elif roww==None:
                    tm.showerror("Error","Order no. doesn't exisits please try correct and valid order no.!!!",parent=self.root5)
                elif rowww==None:
                    tm.showerror("Error","AGENT_CODE/AGENT_NAME Doesn't existes plz check the code again!!!",parent=self.root5)
                elif roow==None:
                    tm.showerror("Error","CUSTOMER_CODE doesn't exits plz enter the vaild code!!!",parent=self.root5)
                else:
                    cur.execute("update orders1 set ORD_AMOUNT=%s,ADVANCE_AMOUNT=%s,BALANCE_AMOUNT=%s,ORD_DATE=%s,CUST_CODE=%s,AGENT_CODE=%s,AGENT_NAME=%s,ORD_DESCRIPTION=%s where ORD_NUM=%s",(
                        self.ORD_AMOUNT_var.get(),
                        self.ADVANCE_AMOUNT_var.get(),
                        self.BALANCE_AMOUNT_var.get(),
                        ORD_DATE.strftime("%Y-%m-%d"),
                        self.CUST_CODE_var.get(),
                        self.AGENT_CODE_var.get(),
                        self.AGENT_NAME_var.get(),
                        self.ORD_DESCRIPTION_var.get(),
                        self.ORD_NUM_var.get()
                        ))
                    con.commit()
                    self.fetch()
                    self.clear()
                    con.close()
                    tm.showinfo("Success","ODRDER update5D Successfull!",parent=self.root5)
            
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root5)

    def delete(self):
        con = pymysql.connect(user="root", password="", host="localhost",database="sales")
        cur = con.cursor()
        cur.execute("delete from orders1 where ORD_NUM=%s",self.ORD_NUM_var.get())
        con.commit()
        con.close()
        tm.showinfo("Success","Data Deletd successfull!",parent=self.root5)
        self.fetch()
        self.clear()
        
    def searchdt(self):
        con = pymysql.connect(user="root", password="", host="localhost",database="sales")
        cur = con.cursor()
        #cur.execute("select * from orders1 where " +str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        cur.execute("select * from orders1 where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Searchedit_table.delete(*self.Searchedit_table.get_children())
            for row in rows:
                self.Searchedit_table.insert('',END,values=row)
            con.commit()
        con.close()
        
    def bal(self):
        self.total_bal=(
            (self.ORD_AMOUNT_var.get())-
            (self.ADVANCE_AMOUNT_var.get())
            )
        self.BALANCE_AMOUNT_var.set(str(self.total_bal))
    
        
    def write_to_csv1(self,df):
        df.to_csv(r'SRS REPORT HIGHLIGHTS1.csv')
     
    
    def read_data1(self):
        readwindow = Tk()
        readwindow.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever anyone saves this folder plz make a not to change its addres accordingly
        readwindow.title("Report Highlights")
        readwindow.geometry("800x600+40+40")
        
        frame2 = Frame(readwindow)
        l = Label(readwindow,text='Here are the Report Highlights',font=("times new roman",15,"bold"),bg="#154360",fg="#FDFEFE")
        l.place(x=270,y=10)
        #print(df)
        df = pd.DataFrame()
        df = TableModel.getSampleData()
        
        pt = Table(frame2)
        
        con = pymysql.connect(user="root", password="", host="localhost", database="sales")
        cur = con.cursor()
        # Excuting insert query
        query = "select ORD_NUM,ORD_AMOUNT,ADVANCE_AMOUNT,BALANCE_AMOUNT,ORD_DATE,CUST_CODE,AGENT_CODE,AGENT_NAME,ORD_DESCRIPTION from orders1 order by BALANCE_AMOUNT desc"
        cur.execute(query)
        #print(cur.fetchall())
        #print(df)
        df = pd.DataFrame(list(cur.fetchall()),columns =['ORD_NUM','ORD_AMOUNT','ADVANCE_AMOUNT','BALANCE_AMOUNT','ORD_DATE','CUST_CODE','AGENT_CODE','AGENT_NAME','ORD_DESCRIPTION'])
        #print (df)
        csv_button = Button(readwindow, text="Print to Excel",cursor="hand2",command=self.write_to_csv1(df),font=("arial",14,"bold"),bg="#32CD32",fg="white")
        csv_button.place(x=270,y=490,width=250,height=35)
        
        table =Table(frame2, dataframe=df,showtoolbar=True,showstatusbar=True)
        table.currwidth=700
        table.currheight=500
        frame2.place(x=110,y=70)
        table.show()

        con.close()
        
obj=Searchedit(root5)
root5.mainloop()