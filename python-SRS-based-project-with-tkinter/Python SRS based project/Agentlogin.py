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
#image capthca
import random


text="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
      
root=Tk()
root.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly

class agentlogin:
    def __init__(self,root):
        self.root=root
        self.root.title("AGENT'S LOGIN WINDOW")
        self.root.geometry("1350x790+40+40")
        
        #======Bg Image======
        
        self.bg=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/login-avatar.png")
        bg=Label(self.root,image=self.bg).place(x=350,y=0,relwidth=1,relheight=1)
        #=======Frame=======
        
        login_frame=Frame(self.root,bg="white",bd=10)
        login_frame.place(x=40,y=120,width=665,height=550)
        
        titel=Label(login_frame,text="LOGIN HERE", font=("times new roman",20,"bold"),bg="white" ,fg="green").place(x=20,y=20)
        
        
        
        acode=Label(login_frame,text="AGENT_CODE", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=150,y=95)
        self.txt_acode=Entry(login_frame, font=("times new roman",15),bg="lightgray" ,fg="black", selectbackground="lightgray")
        self.txt_acode.place(x=150,y=125,width=350,height=35)
        #self.txt_acode.insert(END,'AGENT_CODE')
        
        
        paswd=Label(login_frame,text="PASSWORD", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=150,y=185)
        self.txt_paswd=Entry(login_frame, font=("times new roman",15),bg="lightgray" ,fg="black", show='*')
        self.txt_paswd.place(x=150,y=215,width=331,height=35)
        
        self.captcha = StringVar()
        self.user_input = StringVar()
        
        
        self.bg1=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/1.png")
        captchaaa=Label(login_frame,textvariable= self.captcha, font=("times new roman",30,"bold"),image=self.bg1,compound="center",bg="lightgray" ,fg="#A9A9A9").place(x=180,y=320,width=230, height=50)
        txt_captcha=Entry(login_frame,textvariable= self.user_input, font=("times new roman",15),bg="lightgray" ,fg="black")
        txt_captcha.place(x=150,y=390,width=350,height=35)
        
        self.var_ck=IntVar()
        chk=Checkbutton(login_frame,variable=self.var_ck,command = self.mark,onvalue=0,offvalue=1,bg="white",fg="green").place(x=480,y=219)
        
        self.var_cchk=IntVar()
        chk=Checkbutton(login_frame,text="I agree the Terms and Conditions.",command=self.check_status,variable=self.var_cchk,onvalue=1,offvalue=0,font=("times new roman",9),bg="white",fg="#DC143C", highlightcolor="green").place(x=146,y=252)
        
        
        self.var_chk=IntVar()
        chk=Checkbutton(login_frame,text="Keep me logged in",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",9),bg="white",fg="green").place(x=386,y=252)
        
        
        btn_reg=Button(login_frame,text="New Agent Account?",command=self.register_window,cursor="hand2",font=("times new roman",12),bg="white",bd=0,fg="#DC143C").place(x=146,y=274)
        btn_frpa=Button(login_frame,text="Forgot Password?",command=self.forget_password_window,cursor="hand2",font=("times new roman",12),bg="white",bd=0,fg="#228B22").place(x=292,y=274)
        self.rl=PhotoImage(file="C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/rl.png")
        btn_reload=Button(login_frame,image=self.rl,cursor="hand2",command=self.set_captcha).place(x=410,y=320)
        self.btn_login=Button(login_frame,text="LOGIN",cursor="hand2",command=self.login,font=("times new roman",15,"bold"),bg="green",fg="white",state=DISABLED)
        self.btn_login.place(x=250,y=450,width=150,height=35)
    
    
    def check_status(self):
        #print(self.var_cchk.get())
        if self.var_cchk.get() == 1:
            self.btn_login.configure(state=NORMAL)
        elif self.var_cchk.get() == 0:
            self.btn_login.configure(state=DISABLED)    
    
    
    def set_captcha(self):
        s=random.choices(text)
        s1=random.choices(text)
        s2=random.choices(text)
        s3=random.choices(text)
        self.captcha.set(" ".join(s)+" ".join(s1)+" ".join(s2)+" ".join(s3))
        
     
    def cancel(self):
        self.txt_acode.delete(0,END)
        self.txt_paswd.delete(0,END)
        #clear checkbox
        self.var_chk.set(0)
        
    def reset(self):
        self.txt_acode.delete(0,END)
        self.txt_aname.delete(0,END)
        self.txt_new_pswd.delete(0,END)
        self.txt_paswd.delete(0,END)
        #clear checkbox
        self.var_chk.set(0)
        
    def forget_password(self):
        if self.txt_aname.get()=="" or self.txt_new_pswd.get()=="" or self.var_chk.get()==0:
            tm.showerror("Error","Please enter all the valid Details with the Tick!",parent=self.root2)
        elif self.txt_new_pswd.get()!="12345":
            tm.showerror("Error","Invalid AGENT_CODE or PASSWORD!",parent=self.root2)
        else:
            try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                cur.execute("select * from agents where AGENT_CODE=%s and AGENT_NAME=%s",(self.txt_acode.get(),self.txt_aname.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    tm.showerror("Error","Please enter the valid Agent Name to reset your password!",parent=self.root2)
                else:
                    cur.execute("update agents set AGENT_NAME=%s where AGENT_CODE=%s",(self.txt_aname.get(),self.txt_acode.get()))
                    con.commit()
                    con.close()
                    tm.showinfo("Success","New Password Updated Successfull!",parent=self.root2)
                    #self.root2.destory()
                    self.reset()
                    #self.root.destory()
                    
                    
                
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

                
            
    def forget_password_window(self):
        if self.txt_acode.get()=="":
            tm.showerror("Error","Please enter the valid Agent Code to reset your password!",parent=self.root)
       
        # elif self.var_chk.get()==0:
           # tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root)
        else:
             try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                cur.execute("select * from agents where AGENT_CODE=%s",self.txt_acode.get())
                row=cur.fetchone()
                #print(row)
                if (row==None):
                    tm.showerror("Error","Please enter the valid Agent Code to reset your password!",parent=self.root)
                else:
                    con.close()
                    #self.root2=Tk()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.iconbitmap("C:/Users/Upmanyu/Desktop/Python SRS based project(Internship)/images/ag47f-whoaa-001.ico") #where ever any saves this folder plz make a not to change its addres accordingly
                    self.root2.geometry("400x380+450+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=40,relwidth=1)
                    
                    #===================Forget Password==============
                     
                    a_name=Label(self.root2,text="AGENT-NAME", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=76,y=98)
                    self.txt_aname=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_aname.place(x=76,y=126,width=250)
                    
                    new_pswd=Label(self.root2,text="NEW PASSWORD", font=("times new roman",15,"bold"),bg="white" ,fg="gray").place(x=76,y=170)
                    self.txt_new_pswd=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pswd.place(x=76,y=198,width=250)
                    
            
            
                    self.var_chk=IntVar()
                    chk=Checkbutton(self.root2,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",9,"bold"),bg="white",fg="gray").place(x=76,y=236)
                    
                    
                    btn1_change_pswd=Button(self.root2, text="Reset Password",cursor="hand2",command=self.forget_password,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=101,y=274,width=200,height=35)
                    exitButton = Button(self.root2, text = 'CLOSE AND LOGIN AGAIN',cursor="hand2",font=("arial",14,"bold"),bg="#C0C0C0",fg="white", command = self.root2.destroy).place(x=65,y=314,width=270,height=35)
                    
            
             except Exception as es:
                 tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

            
        
        
        
        
        
        
        
        
        
    def register_window(self):
        self.root3=Toplevel()
        self.root3.focus_force()
        self.root3.grab_set()
        self.root3.title("AGENT'S REGISTRATION WINDOW")
        self.root3.geometry("655x465+445+150")
        
        #======Register Frame=======
        frame1=Frame(self.root3,bg="white")
        frame1.place(x=0,y=0,width=655,height=465)
        
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
        
        
        #-------------------Terms-----------------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",9,"bold"),bg="white",fg="gray").place(x=40,y=300)
        
        #-------------------buttons--------------------
        btn1_register=Button(frame1, text="Submit Now",cursor="hand2",command=self.register_data,font=("arial",14,"bold"),bg="#32CD32",fg="white").place(x=45,y=347,width=150,height=35)
        btn2=Button(frame1, text="Cancel",cursor="hand2",command=self.cancel1,font=("arial",14,"bold"),bg="red",fg="white").place(x=225,y=347,width=150,height=35)
        #btn3=Button(frame1, text="Exit",cursor="hand2",font=("arial",14,"bold"),bg="grey",fg="white",command=self.root3.destory).place(x=403,y=347,width=150,height=35)
    
        
    
    def cancel1(self):
        self.txt_acode.delete(0,END)
        self.txt_aname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_warea.delete(0,END)
        self.txt_comsion.delete(0,END)
        self.txt_cntry.delete(0,END)
        #clear checkbox
        self.var_chk.set(0)
        
        
    def register_data(self):
        if self.txt_acode.get()=="" or self.txt_aname.get()=="" or self.txt_comsion.get()=="" or self.txt_cntry.get()=="" or self.var_chk.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root3)
        elif self.var_chk.get()==0:
            tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root3)
        elif(re.search('[a-zA-Z]$', self.txt_acode.get())):
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumerical value having length 4!")
        elif (len(self.txt_acode.get())<4) or (len(self.txt_acode.get())>4) or all(x.isalpha() or x.isspace() for x in self.txt_acode.get()) or self.txt_acode.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENT_CODE has to alphanumerical value having length 4!",parent=self.root3)
        elif(re.search('[a-z0-9]$', self.txt_aname.get())):  
            tm.showerror("Invalidate!" ,"AGENTS_NAME has to alphabets only!",parent=self.root3)   
        elif self.txt_aname.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENTS_NAME has to alphabets only!",parent=self.root3)
        elif(re.search('[a-zA-Z]$', self.txt_phone.get())):
             tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
        elif (len(self.txt_phone.get())<10) or (len(self.txt_phone.get())>10) or all(x.isalpha() or x.isspace() for x in self.txt_phone.get()):
            tm.showerror("Invalidate!","Phone no. stritly has to be 10 digit no. only!" ,parent=self.root3)
        elif(re.search('[0-9]$', self.txt_warea.get())):
            tm.showerror("Invalidate!" ,"AGENTS WORKING AREA has to be alphabet only!",parent=self.root3)
        elif self.txt_warea.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENTS WORKING AREA has to be alphabet only!",parent=self.root3)
        elif(re.search('[a-zA-Z]$',self.txt_comsion.get())):
             tm.showerror("Invalidate!" ,"COMMISSION should be in digits format only!",parent=self.root3)
        elif all(x.isalpha() or x.isspace() for x in self.txt_comsion.get()):
            tm.showerror("Invalidate!" ,"COMMISSION should be in digits format only!",parent=self.root3)
        elif(re.search('[0-9]$',self.txt_cntry.get())):
            tm.showerror("Invalidate!" ,"AGENTS COUNTRY should be in alphabets format only!",parent=self.root3) 
        elif self.txt_cntry.get().isdigit():
            tm.showerror("Invalidate!" ,"AGENTS COUNTRY should be in alphabets format only!",parent=self.root3)
        
        else:
            try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                cur.execute("select * from agents where AGENT_CODE=%s and PHONE_NO=%s",(self.txt_acode.get(),self.txt_phone.get()))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    tm.showerror("Error","AGENT_CODE/PHONE NO. already exisits please try correct and new AGENT_CODE!",parent=self.root3)
                else:
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
                    tm.showinfo("Success","Registertion successfull!",parent=self.root3)
                    self.cancel1()
                    
                    
                
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root3)
    
    
    
    
    def mark(self) :
        if self.var_ck.get() == 1 :
            self.txt_paswd.configure(show = "")
        elif self.var_ck.get() == 0 :
            self.txt_paswd.configure(show = "*")
        
    def login(self):
        #print(self.txt_acode.get(),self.txt_paswd.get())
        if self.txt_acode.get()=="" or self.txt_paswd.get()=="" or self.var_cchk.get()=="":
            tm.showerror("Error","All Fields Are Required!",parent=self.root)
        elif self.var_cchk.get()==0:
            tm.showerror("Error","Please Tick and agree the terms & conditions field which is mandatory!",parent=self.root)
        elif (len(self.txt_acode.get())<4) or (len(self.txt_acode.get())>4) or all(x.isalpha() or x.isspace() for x in self.txt_acode.get()):
            tm.showerror("Invalidate!" ,"AGENT_CODE has to numerical value having length 4!",parent=self.root)
        elif self.txt_paswd.get()!="12345":
            tm.showerror("Error","Invalid AGENT_CODE or PASSWORD!",parent=self.root)
        elif self.captcha.get()!= self.user_input.get() or self.captcha.get()=="": 
            tm.showerror("Error","Captcha entered is not correct",parent=self.root)
        else:
            try:
                # Connecetion for mysql database
                con = pymysql.connect(user="root", password="", host="localhost",database="sales")
                cur = con.cursor()
                cur.execute("select * from agents where AGENT_CODE=%s",self.txt_acode.get())
                row=cur.fetchone()
                #print(row)
                if (row==None):
                    tm.showerror("Error","Invalid AGENT_CODE and PASSWORD!",parent=self.root)
                else:
                    tm.showinfo("Success","WELCOME, you have Logged-In successfuly!",parent=self.root)
                    self.cancel()
                    self.root.destroy()
                    import main
                    #self.cancel()
                con.close()
            except Exception as es:
                tm.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

        
        
        
obj=agentlogin(root)
root.mainloop()