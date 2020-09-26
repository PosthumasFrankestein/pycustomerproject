from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import mysql.connector

class Customer(Tk):
    tpant=20
    tshirt=20
    that=20
    cpant=7000
    cshirt=5000
    chat=2500
    ppant=0
    pshirt=0
    phat=0

    def __init__(self):
        super().__init__()
        self.geometry("760x480")
        self.configure(background="White")
        self.title("Form")

    def value(self):
        l1=Label(self,text="Add Customer",fg="white",bg="blue",bd=4,relief=RIDGE,font=("times new roman",20,"bold"))
        l1.place(x=280,y=2)
    
    def submit(self):
        if c_iname.get()=="" or c_iage.get()=="" or c_icountry.get()=="" or combo_gender.get()=="" or c_iphone.get()=="":
             messagebox.showinfo("Please","Fillup the form") 
        else:      
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="business")
            mycursor=mydb.cursor()            
            s="INSERT INTO customer(name,age,gender,phone,country) VALUES(%s,%s,%s,%s,%s)"
            b1=(c_iname.get(),c_iage.get(),combo_gender.get(),c_iphone.get(),c_icountry.get())
            mycursor.execute(s,b1)
            mydb.commit()
            messagebox.showinfo("Wow","Sucessfully submited")      

    def custinfo(self):
        global c_iname,c_iage,c_icountry,combo_gender,c_iphone
        c_name=Label(self,text="Customer name",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        c_name.place(x=55,y=105)
        c_iname=Entry(self,textvariable=c_name,fg="black",bg="silver",font=("times new roman",15,"bold"))
        c_iname.place(x=225,y=105)
      
        c_age=Label(self,text="Custome Age",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        c_age.place(x=55,y=155)
        c_iage=Entry(self,textvariable=c_age,fg="black",bg="silver",font=("times new roman",15,"bold"))
        c_iage.place(x=225,y=155)

        c_gender=Label(self,text="Custome Gender",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        c_gender.place(x=55,y=200)
        
        v=["male","female","other"]
        combo_gender=Combobox(self,values=v,font=("times new roman",15,"bold"),state='readonly')
        combo_gender.place(x=225,y=200)

        c_phone=Label(self,text="Custome number",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        c_phone.place(x=55,y=255)
        c_iphone=Entry(self,textvariable=c_phone,fg="black",bg="silver",font=("times new roman",15,"bold"))
        c_iphone.place(x=225,y=255)
  
        c_country=Label(self,text="Customercountry",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        c_country.place(x=55,y=300)
        c_icountry=Entry(self,textvariable=c_country,fg="black",bg="silver",font=("times new roman",15,"bold"))
        c_icountry.place(x=225,y=300)
          
        btn=Button(self,text="Submit",bg="red",fg="white",font=("times new roman",15,"bold"),bd=4,relief=RIDGE,command=self.submit)
        btn.place(x=90,y=355)
  
class product(Customer):
    def prod(self):
        btnn=Button(self,text="Add Product",bg="red",fg="white",font=("times new roman",15,"bold"),bd=4,relief=RIDGE,command=self.screen)
        btnn.place(x=280,y=355)

    def gift(self):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="business")
        mycursor=mydb.cursor()            
        s="INSERT INTO product(product_name,no_product,cost_product) VALUES(%s,%s,%s)"
        b1=("Pant",self.tpant,self.cpant)
        b2=("Shirt",self.tshirt,self.cshirt)
        b3=("Hat",self.that,self.chat)
        mycursor.execute(s,b1)
        mycursor.execute(s,b2)
        mycursor.execute(s,b3)
        mydb.commit()
        messagebox.showinfo("Wow","Thanks for buying the products")   

    def hit(self):
        global btn1
        if ipant.get()=="" or ihat.get()=="" or ishirt.get()=="" or ipno=="" or isno.get()=="" or ihno.get()=="":
            messagebox.showinfo("Please","Please buy the  products")
        else:
            #Pant
            if int(ipno.get())<self.tpant:
                self.tpant-=int(ipno.get())
            
            elif int(ipno.get())==self.tpant:
                 self.tpant-=int(ipno.get())
                 messagebox.showinfo("Empty","buyed and No pant left")

            elif int(ipno.get())>self.tpant:
                 messagebox.showinfo("Please","we dont't have pant")

            if int(ipant.get())==self.cpant:
                  self.ppant+=7000*int(ipno.get())
                  if self.ppant>=50000:
                        messagebox.showinfo("Wow","Congratulation you are a silver/gold customer and  got 30 percent discount")
                        self.cpant=int(self.cpant-30/100*self.cpant)
                        messagebox.showinfo("Wow",f"Pant cost after discount is {self.cpant}")
                
                  elif self.ppant>=30000:
                        messagebox.showinfo("Wow","Congratulation you are a bronze and have got 20 percent discount")
                        self.cpant=int(self.cpant-20/100*self.cpant)
                        messagebox.showinfo("Wow",f"Pant cost after discount is {self.cpant}")   

                  elif self.ppant>=10000:
                        messagebox.showinfo("Wow","Congratulation you are normal customer and have got 10 percent discount")
                        self.cpant=int(self.cpant-10/100*self.cpant)
                        messagebox.showinfo("Wow",f"Pant cost after discount is {self.cpant}")     
                  else:
                       messagebox.showinfo("Wow","buyed ")

            elif int(ipant.get())<self.cpant:
                  messagebox.showinfo("Sorry","Amount not enough")

            elif int(ipant.get())>self.cpant:
                  messagebox.showinfo("Sorry","Amount is more than required amount")     

            #Shirt
            if int(isno.get())<self.tshirt:
                self.tshirt-=int(isno.get())
            
            elif int(isno.get())==self.tshirt:
                 self.tshirt-=int(isno.get())
                 messagebox.showinfo("Empty","buyed and No pant left")

            elif int(isno.get())>self.tshirt:
                 messagebox.showinfo("Please","we dont't have pant")

            if int(ishirt.get())==self.cshirt:
                  self.pshirt+=7000*int(isno.get())
                  if self.pshirt>=50000:
                        messagebox.showinfo("Wow","Congratulation you are a silver/gold customer and  got 30 percent discount")
                        self.cshirt=int(self.cshirt-30/100*self.cshirt)
                        messagebox.showinfo("Wow",f"Pant cost after discount is {self.cshirt}")
                
                  elif self.pshirt>=30000:
                        messagebox.showinfo("Wow","Congratulation you are a bronze and have got 20 percent discount")
                        self.cshirt=int(self.cshirt-20/100*self.cshirt)
                        messagebox.showinfo("Wow",f"Pant cost after discount is {self.cshirt}")   

                  elif self.pshirt>=10000:
                        messagebox.showinfo("Wow","Congratulation you are normal customer and have got 10 percent discount")
                        self.cshirt=int(self.cshirt-10/100*self.cshirt)
                        messagebox.showinfo("Wow",f"Pant cost after discount is {self.cshirt}")     
                  else:
                       messagebox.showinfo("Wow","buyed ")

            elif int(ishirt.get())<self.cshirt:
                  messagebox.showinfo("Sorry","Amount not enough")

            elif int(ishirt.get())>self.cshirt:
                  messagebox.showinfo("Sorry","Amount is more than required amount")         

          
            # #Hat
            if int(ihno.get())<self.that:
                self.that-=int(ihno.get())
            
            elif int(ihno.get())==self.that:
                 self.that-=int(ihno.get())
                 messagebox.showinfo("Empty","buyed and No hat left")

            elif int(ihno.get())>self.that:
                 messagebox.showinfo("Please","we dont't have hat")


            if int(ihat.get())==self.chat:
                  self.pshirt+=7000*int(ihno.get())
                  if self.pshirt>=50000:
                        messagebox.showinfo("Wow","Congratulation you are a silver/gold customer and  got 30 percent discount")
                        self.chat=int(self.chat-30/100*self.chat)
                        messagebox.showinfo("Wow",f"Hat cost after discount is {self.chat}")
                
                  elif self.pshirt>=30000:
                        messagebox.showinfo("Wow","Congratulation you are a bronze and have got 20 percent discount")
                        self.chat=int(self.chat-20/100*self.chat)
                        messagebox.showinfo("Wow",f"Hat cost after discount is {self.chat}")   

                  elif self.pshirt>=10000:
                        messagebox.showinfo("Wow","Congratulation you are normal customer and have got 10 percent discount")
                        self.chat=int(self.chat-10/100*self.chat)
                        messagebox.showinfo("Wow",f"Hat cost after discount is {self.chat}")     
                  else:
                       messagebox.showinfo("Wow","buyed ")
            elif int(ihat.get())<self.chat:
                  messagebox.showinfo("Sorry","Amount not enough")

            elif int(ihat.get())>self.chat:
                  messagebox.showinfo("Sorry","Amount is more than required amount")  

        btn1=Button(s,text="Finish",bg="red",fg="white",font=("times new roman",15,"bold"),bd=4,relief=RIDGE,command=self.gift)
        btn1.place(x=350,y=355)                      



    def screen(self):
        global s,btn,ipno,isno,ihno,ishirt,ihat,ipant
        s=Toplevel(self)
        s.title("Product")
        s.configure(background="white")   
        s.geometry("800x480")
        l=Label(s,text="Suren clothes",fg="white",bg="blue",bd=4,relief=RIDGE,font=("times new roman",20,"bold"))
        l.place(x=280,y=2)
        l2=Label(s,text="1 pant cost 7000,1 shirts cost 5000,1 hats costs 2500",fg="white",bg="blue",bd=4,relief=RIDGE,font=("times new roman",20,"bold"))
        l2.place(x=120,y=50)
        pno=Label(s,text="No of pants",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        pno.place(x=70,y=170)
        v=["1","2","3","4","5","6","7","8","9","10"]
        ipno=Combobox(s,values=v,font=("times new roman",10,"bold"),state='readonly')
        ipno.place(x=200,y=170)

        pant=Label(s,text="Cost of pant",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        pant.place(x=400,y=170)
        ipant=Entry(s,textvariable=pant,fg="black",bg="silver",font=("times new roman",15,"bold"))
        ipant.place(x=550,y=170)

        sno=Label(s,text="No of Shirt",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        sno.place(x=70,y=230)
        v=["1","2","3","4","5","6","7","8","9","10"]
        isno=Combobox(s,values=v,font=("times new roman",10,"bold"),state='readonly')
        isno.place(x=200,y=230)

        shirt=Label(s,text="Cost of Shirt",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        shirt.place(x=400,y=230)
        ishirt=Entry(s,textvariable=shirt,fg="black",bg="silver",font=("times new roman",15,"bold"))
        ishirt.place(x=550,y=230)

        hno=Label(s,text="No of Hats",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        hno.place(x=70,y=290)
        v=["1","2","3","4","5","6","7","8","9","10"]
        ihno=Combobox(s,values=v,font=("times new roman",10,"bold"),state='readonly')
        ihno.place(x=200,y=290)

        hat=Label(s,text="Cost of Hat",fg="white",bd=4,relief=RIDGE,bg="crimson",font=("times new roman",15,"bold"))
        hat.place(x=400,y=290)
        ihat=Entry(s,textvariable=hat,fg="black",bg="silver",font=("times new roman",15,"bold"))
        ihat.place(x=550,y=290)

        btn=Button(s,text="Submit",bg="red",fg="white",font=("times new roman",15,"bold"),bd=4,relief=RIDGE,command=self.hit)
        btn.place(x=90,y=355)

        s.mainloop()


     
if __name__ == "__main__":

    window=product()
    window.value()
    window.custinfo()
    window.prod()
    window.mainloop()       