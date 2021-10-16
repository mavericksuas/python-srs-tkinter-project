# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 01:37:21 2020

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


root1=Tk()
root1.iconbitmap("C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class Register:
    def __init__(self,root1):
        self.root1=root1
        self.root1.title("AGENT'S REGISTRATION WINDOW")
        self.root1.geometry("1350x790+40+40")
        #======Bg Image======
        
        self.bg1=PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/brkr.png")
        bg1=Label(self.root1,image=self.bg1).place(x=350,y=0,relwidth=1,relheight=1)
        
        #======Left Image======
        
        #self.left=PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/mp1.png")
        #left=Label(self.root1,image=self.left).place(x=80,y=100,relwidth=400,relheight=500)
        #======Register Frame=======
        frame1=Frame(self.root1,bg="white")
        frame1.place(x=40,y=155,width=650,height=465)
        
        titel=Label(frame1,text="AGENT'S REGISTER HERE", font=("times new roman",20,"bold"),bg="white" ,fg="green").place(x=20,y=20)
        
        #---------------------------------------Row1
        a_code=Label(frame1,text="AGENT-CODE", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=70)
        self.txt_acode=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_acode.place(x=40,y=100,width=250)
        
        a_name=Label(frame1,text="AGENT-NAME", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=70)
        self.txt_aname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_aname.place(x=370,y=100,width=250)
        
        #---------------------------------------Row2
        phone=Label(frame1,text="PHONE NO.", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=150)
        self.txt_phone=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_phone.place(x=40,y=180,width=250)
        
        w_area=Label(frame1,text="WORKING AREA", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=150)
        self.txt_warea=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_warea.place(x=370,y=180,width=250)
        
        #---------------------------------------Row3
        comsion=Label(frame1,text="COMMISSION", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=230)
        self.txt_comsion=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_comsion.place(x=40,y=260,width=250)
        
        cntry=Label(frame1,text="COUNTRY", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=230)
        self.txt_cntry=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cntry.place(x=370,y=260,width=250)
        #cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly' ,justify=CENTER)
        #cmb_quest['values']=("Select","ACD","AN","WKG")
        #cmb_quest.place(x=370,y=260,width=250)
        #cmb_quest.current(0)# to make select as by-default
        
        
        #---------------------------------------Row4
        #question=Label(frame1,text="SECURITY QUESTION", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=40,y=310)
        #cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly' ,justify=CENTER)
        #cmb_quest['values']=("Select","ACD","AN","WKG")
        #cmb_quest.place(x=40,y=340,width=250)
        #cmb_quest.current(0)# to make select as by-default
        
        #answer=Label(frame1,text="ANSWER", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=310)
        #txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=340,width=250)
        
        #---------------------------------------Row5
        #pswrd=Label(frame1,text="PASSWORD", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=40,y=390)
        #txt_pswrd=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=40,y=420,width=250)
        
        #cpswrd=Label(frame1,text="CONFIRM PASSWORD", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=370,y=390)
        #txt_cpswrd=Entry(frame1,font=("times new roman",15),bg="lightgray").place(x=370,y=420,width=250)
        
        #-------------------Terms-----------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",9,"bold"),bg="white",fg="gray").place(x=40,y=300)
        
        #-------------------buttons--------------------
        #self.btn_img=ImageTk.PhotoImage(file="C:/Users/UPMANYU JHA/Desktop/Python SRS based project(Internship)/images/submit.png")
        #btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2").place(x=20,y=575)
        btn1_register=Button(frame1, text="Submit Now",cursor="hand2",command=self.register_data,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=70,y=347,width=150,height=35)
        btn2=Button(frame1, text="Cancel",cursor="hand2",command=self.cancle,font=("arial",14,"bold"),bg="red",fg="white").place(x=250,y=347,width=150,height=35)
        btn3=Button(frame1, text="Update",cursor="hand2",command=self.update,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=430,y=347,width=150,height=35)
        btn3=Button(frame1, text="Back to home>>>",cursor="hand2",command=self.back,font=("arial",14,"bold"),bg="#DCDCDC",fg="black")
        btn3.place(x=220,y=397,width=200,height=35)
        
        
    def back(self):
        self.root1.destroy()
        import main
        
    def cancle(self):
        self.txt_acode.delete(0,END)
        self.txt_aname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_warea.delete(0,END)
        self.txt_comsion.delete(0,END)
        self.txt_cntry.delete(0,END)
        #clear checkbox
        self.var_chk.set(0)
        
    def register_data(self):
        if self.txt_acode.get()=="" or self.txt_aname.get()=="" or self.txt_comsion.get()=="" or self.txt_cntry.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root1)
        elif self.var_chk.get()==0:
            tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root1)
        elif(re.search('[a-zA-Z]$', self.txt_acode.get())):
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumerical value having length 4!")
        elif (len(self.txt_acode.get())<4) or (len(self.txt_acode.get())>4) or all(x.isalpha() or x.isspace() for x in self.txt_acode.get()) or self.txt_acode.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphnumerical value having length 4!")
        elif(re.search('[a-z0-9]$', self.txt_aname.get())):  
            tm.showerror("Invalidate!" ,"AGENTS_NAME has to alphabets only!",parent=self.root1)   
        elif self.txt_aname.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENTS_NAME has to alphabets only!",parent=self.root1)
        #elif(re.search('[a-zA-Z]$', self.txt_phone.get())):
            # tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
       # elif (len(self.txt_phone.get())<10) or (len(self.txt_phone.get())>10) or all(x.isalpha() or x.isspace() for x in self.txt_phone.get()):
           # tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
        elif(re.search('[0-9]$', self.txt_warea.get())):
            tm.showerror("Invalidate!" ,"AGENTS WORKING AREA has to be alphabet only!",parent=self.root1)
        elif self.txt_warea.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENTS WORKING AREA has to alphanumeric or alphabet values only!",parent=self.root1)
        elif(re.search('[a-zA-Z]$',self.txt_comsion.get())):
             tm.showerror("Invalidate!" ,"COMMISSION should be in digits format only!",parent=self.root1)
        elif all(x.isalpha() or x.isspace() for x in self.txt_comsion.get()):
            tm.showerror("Invalidate!" ,"COMMISSION should be in digits format only!")
        elif(re.search('[0-9]$',self.txt_cntry.get())):
            tm.showerror("Invalidate!" ,"AGENTS COUNTRY should be in alphabets format only!",parent=self.root1) 
        elif self.txt_cntry.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENTS COUNTRY should be in alphabets format only!")
        
        else:
            try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                cur.execute("select * from agents where AGENT_CODE=%s and PHONE_NO=%s",(self.txt_acode.get(),self.txt_phone.get()))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    tm.showerror("Error","AGENT_CODE/PHONE NO. already exisits please try correct and new AGENT_CODE!",parent=self.root1)
                elif(re.search(r'\d{3}-\d{3}-\d{4}', self.txt_phone.get())):
                    cur.execute("insert into agents(AGENT_CODE,AGENT_NAME,WORKING_AREA,COMMISSION,PHONE_NO,COUNTRY) values(%s,%s,%s,%s,%s,%s)", 
                            (self.txt_acode.get(),
                             self.txt_aname.get(),
                             self.txt_warea.get(),
                             self.txt_comsion.get(),
                             self.txt_phone.get(),
                             self.txt_cntry.get()
                             ))
                    con.commit()
                    con.close()
                    tm.showinfo("Success","Registertion successfull!",parent=self.root1)
                else:
                    tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
                
                
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root1)

    def update(self):
        if self.txt_acode.get()=="" or self.txt_aname.get()=="" or self.txt_comsion.get()=="" or self.txt_cntry.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root1)
        elif self.var_chk.get()==0:
            tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root1)
        elif(re.search('[a-zA-Z]$', self.txt_acode.get())):
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumerical value having length 4!")
        elif (len(self.txt_acode.get())<4) or (len(self.txt_acode.get())>4) or all(x.isalpha() or x.isspace() for x in self.txt_acode.get() or self.txt_acode.get().isdigit()):
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphnumerical value having length 4!")
        elif(re.search('[a-z0-9]$', self.txt_aname.get())):  
            tm.showerror("Invalidate!" ,"AGENTS_NAME has to alphabets only!",parent=self.root1)   
        elif self.txt_aname.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENTS_NAME has to alphabets only!",parent=self.root1)
        #elif(re.search('[a-zA-Z]$', self.txt_phone.get())):
          #   tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
        #elif (len(self.txt_phone.get())<10) or (len(self.txt_phone.get())>10) or all(x.isalpha() or x.isspace() for x in self.txt_phone.get()):
         #   tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
        elif(re.search('[0-9]$', self.txt_warea.get())):
            tm.showerror("Invalidate!" ,"AGENTS WORKING AREA has to be alphabet only!",parent=self.root1)
        elif self.txt_warea.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENTS WORKING AREA has to alphanumeric or alphabet values only!",parent=self.root1)
        elif(re.search('[a-zA-Z]$',self.txt_comsion.get())):
             tm.showerror("Invalidate!" ,"COMMISSION should be in digits format only!",parent=self.root1)
        elif all(x.isalpha() or x.isspace() for x in self.txt_comsion.get()):
            tm.showerror("Invalidate!" ,"COMMISSION should be in digits format only!")
        elif(re.search('[0-9]$',self.txt_cntry.get())):
            tm.showerror("Invalidate!" ,"AGENTS COUNTRY should be in alphabets format only!",parent=self.root1) 
        elif self.txt_cntry.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENTS COUNTRY should be in alphabets format only!")
        
        else:
            try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                if(re.search(r'\d{3}-\d{3}-\d{4}', self.txt_phone.get())):
                    cur.execute("update agents set AGENT_NAME=%s,WORKING_AREA=%s,COMMISSION=%s,PHONE_NO=%s,COUNTRY=%s where AGENT_CODE=%s",(
                        self.txt_aname.get(),
                        self.txt_warea.get(),
                        self.txt_comsion.get(),
                        self.txt_phone.get(),
                        self.txt_cntry.get(),
                        self.txt_acode.get()
                        ))
                    con.commit()
                    con.close()
                    tm.showinfo("Success","AGENTS DATA IS UPDATED SUCCESSFULLY!",parent=self.root1)
                else:
                    tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root1)
   
    
obj=Register(root1)
root1.mainloop()