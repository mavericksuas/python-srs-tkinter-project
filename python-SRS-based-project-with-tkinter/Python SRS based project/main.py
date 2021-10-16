# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:01:54 2020

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
from tkcalendar import Calendar, DateEntry
import csv
import webbrowser
import Agentlogin
global agentcode


root=Tk()
root.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class mainhome:
    def __init__(self,root):
        self.root=root
        self.root.title("SRS HOME WINDOW")
        self.root.geometry("1350x790+40+40")
        
        #======Bg Image======
        
        self.bg=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/bg.png")
        bg=Label(self.root,image=self.bg).place(x=350,y=0,relwidth=1,relheight=1)
        
        
        #=========================Handel frame for home==========================
        Hold1_Frame=Frame(self.root,bd=0,relief=GROOVE,bg="#00FF00")
        Hold1_Frame.place(x=0,y=0,relwidth=1,height=80)
    
        self.bg1wq11=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/pngwave (1).png")
        bg1wq11=Label(Hold1_Frame,image=self.bg1wq11,bg="#00FF00").place(x=-10,y=6,relheight=1, width=135)
        
        self.r23rr=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/homeic.png")
        welcome=Label(Hold1_Frame,text="  Welcome Home Agent!", font=("times new roman",15,"bold"),image=self.r23rr,compound="left",bg="#00FF00" ,fg="black").place(x=1085, y=20)
        
        
         #======Register Frame=======
        frame=Frame(self.root,bg="white")
        frame.place(x=40,y=90,width=670,height=600)
        
       
        titel=Label(frame,text="HOME PAGE", font=("times new roman",20,"bold"),bg="white" ,fg="green").place(x=20,y=20)
        #=========Buttons=============
        btn1=Button(frame, text="AGENTS Registration and Updation",cursor="hand2",command=self.register_window1,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=110,y=75,width=450,height=35)
        btn2=Button(frame, text="COMPANYS Registration and Updation",cursor="hand2",command=self.register_window2,font=("arial",14,"bold"),bg="#FF6347",fg="white").place(x=110,y=153,width=450,height=35)
        btn3=Button(frame, text="CUSTOMERS Registration and Updation",cursor="hand2",command=self.register_window3,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=110,y=231,width=450,height=35)
        btn4=Button(frame, text="ORDER'S Entery and Updation",cursor="hand2",command=self.register_window4,font=("arial",14,"bold"),bg="#FF4500",fg="white").place(x=110,y=309,width=450,height=35)
        btn5=Button(frame, text="COMPARE",cursor="hand2",command=self.compare_window,font=("arial",14,"bold"),bg="#DC143C",fg="white").place(x=110,y=387,width=450,height=35)
        btn6=Button(frame, text="INSIGHTS",cursor="hand2",command=self.insights_window,font=("arial",14,"bold"),bg="#B0C4DE",fg="white").place(x=110,y=465,width=450,height=35)
        
        #=========================Bottom Handel frame for home==========================
        Btm11_Frame=Frame(self.root,bd=0,relief=GROOVE,bg="black")
        Btm11_Frame.place(x=0,y=710,relwidth=1,height=80)
        
        self.inst11=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/insta.png")
        btn_inst11=Button(Btm11_Frame,image=self.inst11,cursor="hand2",bg="black",fg="black", command=self.openinsta12).place(x=1260, y=25, height=32, width=32)
        
        self.fb11=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/facebook.png")
        btn_fb11=Button(Btm11_Frame,image=self.fb11,cursor="hand2",bg="black",fg="black", command=self.openfb12).place(x=1300, y=25, height=32, width=32)
        
        titelu123=Label(Btm11_Frame,text="Contact No.: 9435112125", font=("times new roman",15,"bold"),bg="black" ,fg="white").place(x=20,y=25)
        
        titelg123=Label(Btm11_Frame,text="E-mail id: sunvilleproperty@gmail.com", font=("times new roman",15,"bold"),bg="black" ,fg="white").place(x=560,y=25)
        
    def openinsta12(self):
        webbrowser.open("https://www.instagram.com/hackergod00001/")
    
    def openfb12(self):
        webbrowser.open("https://www.facebook.com/Upmanyujha0001/")
    
        
    def register_window1(self):
        self.root1=Toplevel()
        self.root1.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly
        self.root1.title("AGENT'S REGISTRATION WINDOW")
        self.root1.geometry("1350x790+40+40")
        self.root1.focus_force()
        self.root1.grab_set()
        
        #======Bg Image======
        
        self.bg1=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/brkr.png")
        bg1=Label(self.root1,image=self.bg1).place(x=350,y=0,relwidth=1,relheight=1)
        
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
        
        
        #-------------------Terms-----------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",9,"bold"),bg="white",fg="gray").place(x=40,y=300)
        
        #-------------------buttons--------------------
        #self.btn_img=ImageTk.PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/submit.png")
        #btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2").place(x=20,y=575)
        btn1_register=Button(frame1, text="Submit Now",cursor="hand2",command=self.register_data,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=70,y=347,width=150,height=35)
        btn2=Button(frame1, text="Cancel",cursor="hand2",command=self.cancel,font=("arial",14,"bold"),bg="red",fg="white").place(x=250,y=347,width=150,height=35)
        btn3=Button(frame1, text="Update",cursor="hand2",command=self.update,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=430,y=347,width=150,height=35)
        btn3=Button(frame1, text="Back to home>>>",cursor="hand2",command=self.back,font=("arial",14,"bold"),bg="#DCDCDC",fg="black")
        btn3.place(x=220,y=397,width=200,height=35)
        
        
    def back(self):
        self.root1.destroy()
        
        
    def cancel(self):
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
         #    tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
        #elif (len(self.txt_phone.get())<10) or (len(self.txt_phone.get())>10) or all(x.isalpha() or x.isspace() for x in self.txt_phone.get()):
          #  tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
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
         #    tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
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
                    self.cancel()
                else:
                    tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root1)
                    
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root1)
   
        
        
    def register_window2(self):
        self.root2=Toplevel()
        self.root2.title("SUB-COMPANY'S REGISTRATION WINDOW")
        self.root2.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly
        self.root2.geometry("1350x790+40+40")
        self.root2.focus_force()
        self.root2.grab_set()
        #======Bg Image======
        
        self.bg2=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/cc.png")
        bg2=Label(self.root2,image=self.bg2).place(x=350,y=0,relwidth=1,relheight=1)
        
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
        #self.btn_img=ImageTk.PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/submit.png")
        #btn=Button(frame2,image=self.btn_img,bd=0,cursor="hand2").place(x=20,y=575)
        btn1_register=Button(frame2, text="Submit Now",cursor="hand2",command=self.register_data2,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=70,y=340,width=150,height=35)
        btn2=Button(frame2, text="Cancel",cursor="hand2",command=self.cancel1,font=("arial",14,"bold"),bg="red",fg="white").place(x=250,y=340,width=150,height=35)
        btn3=Button(frame2, text="back to home>>>",cursor="hand2",command=self.back2,font=("arial",14,"bold"),bg="#DCDCDC",fg="black").place(x=220,y=397,width=200,height=35)
        btn4=Button(frame2, text="update",cursor="hand2",command=self.update2,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=430,y=340,width=150,height=35)
        
        
    def back2(self):
        self.root2.destroy()
        
        
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
                self.cancel1()
                
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root2)
   
    
        
    def register_window3(self):
        self.root3=Toplevel()
        self.root3.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly
        self.root3.title("AGENT'S REGISTRATION WINDOW")
        self.root3.geometry("1350x790+40+40")
        self.root3.focus_force()
        self.root3.grab_set()
        #======Bg Image======
        
        self.bg3=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/hiclipart.com.png")
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
        #self.btn_img=ImageTk.PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/submit.png")
        #btn=Button(frame3,image=self.btn_img,bd=0,cursor="hand2").place(x=20,y=575)
        btn1=Button(frame3, text="Submit Now",cursor="hand2",command=self.register_data3,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=78,y=580,width=150,height=35)
        btn2=Button(frame3, text="cancel",cursor="hand2",command=self.cancel3,font=("arial",14,"bold"),bg="red",fg="white").place(x=253,y=580,width=150,height=35)
        #btn3=Button(frame3, text="update3",cursor="hand2",font=("arial",14,"bold"),bg="#FF8C00",fg="black").place(x=460,y=580,width=150,height=35)
        btn3=Button(frame3, text="back to home>>>",cursor="hand2",command=self.back3,font=("arial",14,"bold"),bg="#DCDCDC",fg="black").place(x=228,y=630,width=200,height=35)
        btn4=Button(frame3, text="update",cursor="hand2",command=self.update3,font=("arial",14,"bold"),bg="#FF8C00",fg="white").place(x=430,y=580,width=150,height=35)
        
        
    def back3(self):
        self.root3.destroy()
  
        
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
        #elif(re.search('[a-zA-Z]$',self.txt_phone.get())):
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
        #elif(re.search('[a-zA-Z]$',self.txt_phone.get())):
         #   tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
        #elif (len(self.txt_phone.get())<10) or (len(self.txt_phone.get())>10) or all(x.isalpha() or x.isspace() for x in self.txt_phone.get()):
         #   tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
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


    def register_window4(self):
        self.root4=Toplevel()
        self.root4.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly
        self.root4.title("SUB-COMPANY'S REGISTRATION WINDOW")
        self.root4.geometry("1350x790+40+40")
        self.root4.focus_force()
        self.root4.grab_set()
        #======Bg Image======
    
        self.bg4=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/orders.png")
        bg4=Label(self.root4,image=self.bg4).place(x=350,y=0,relwidth=1,relheight=1)
        
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
        #btn_img=ImageTk.PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/submit.png")
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
        self.root5=Toplevel()
        self.root5.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly
        self.root5.title("SRS Search and update WINDOW")
        self.root5.geometry("1350x790+40+40")
        self.root5.focus_force()
        self.root5.grab_set()
        
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
        
        
        
        
    def write_to_csv(self,df):
        df.to_csv(r'SRS REPORT HIGHLIGHTS.csv')
           
            
    def read_data(self):
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

                
 
        
    def insights_window(self):
        self.root.destroy()
        import insights
        
    def compare_window(self):
        self.root6=Toplevel()
        self.root6.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly
        self.root6.title("Module4 WINDOW")
        self.root6.geometry("1350x800+80+28")
        self.root6.focus_force()
        self.root6.grab_set()
        
        
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
        
        lb1_aamt=Label(F2,bg="white",fg="green",text="COLLECTIVE PAYMENT AMOUNT  Rs.", font=("times new roman",15,"bold"))
        lb1_aamt.grid(row=0,column=0,pady=15,padx=1,sticky=W)
        self.payamt=StringVar()
        txt_aamt=Entry(F2,text="self.tpay",textvariable=self.payamt, font=("times new roman",15,"bold"),bd=5,relief=GROOVE,state='readonly')
        txt_aamt.grid(row=0,column=1,pady=15,padx=0,sticky=W)
        Calbalbtn=Button(F2,text="Click",cursor="hand2",bg="#FF8C00",fg="white",width=4,height=1,bd=6,command=self.tpay).grid(row=0,column=2,padx=0,pady=15,sticky=E)
        
        
        lb1_bamt=Label(F2,bg="white",fg="green",text="  COLLECTIVE OUTSTANDING AMOUNT  Rs.", font=("times new roman",15,"bold"))
        lb1_bamt.grid(row=0,column=4,pady=15,padx=1,sticky=E)
        self.outamt=StringVar()
        txt_bamt=Entry(F2,text="self.tout",textvariable=self.outamt, font=("times new roman",15,"bold"),bd=5,relief=GROOVE,state='readonly')
        txt_bamt.grid(row=0,column=5,pady=15,padx=0,sticky=E)
        Calbalbtn=Button(F2,text="Click",cursor="hand2",bg="#FF8C00",fg="white",width=4,height=1,bd=6,command=self.tout).grid(row=0,column=6,padx=0,pady=15,sticky=E)
        
        
        
        
        
        
        
        
    def tpay(self):
        try:
            # Connecetion for mysql database
            con = pymysql.connect(user="root", password="", host="localhost",database="sales")
            cur = con.cursor()
            cur.execute("select sum(PAYMENT_AMT) as total from customer ")
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
            cur.execute("select sum(OUTSTANDING_AMT) as total from customer ")
            result=cur.fetchone()
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

   



        
        
obj=mainhome(root)
root.mainloop()

