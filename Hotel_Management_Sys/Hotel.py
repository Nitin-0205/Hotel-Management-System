import random
import time
from tkinter import *
from tkinter import ttk,messagebox
from tkinter.ttk import Treeview
import pymysql

Grand_total = 0
BillPrintLine = 7.0

root = Tk()
root.geometry("474x660+500+20")
root.title("Hotel Management System")

Mframe = Frame(root,bg='#9AD2A1',relief="ridge",bd="4")
Mframe.place(x=0,y=0,relheight=1,width=474)

bg = PhotoImage(file="MainBg.png")

bgImgLab = Label(Mframe,image=bg)
bgImgLab.place(x=0,y=0,relwidth=1,relheight=1)

ChefImg = PhotoImage(file="chef.png")
ChefImg = ChefImg.subsample(2,2)

TitleImg = PhotoImage(file="Ng_TitleImg.png")
TitleImg = TitleImg.subsample(1,1)

StarterButImg = PhotoImage(file="StarterBut.png")
StarterButImg = StarterButImg.subsample(1,1)

PizzaButImg = PhotoImage(file="PizzaBut.png")
PizzaButImg = PizzaButImg.subsample(1,1)

DeserButImg = PhotoImage(file="DsertBut.png")
DeserButImg = DeserButImg.subsample(1,1)

BeverButImg = PhotoImage(file="BeverBut.png")
BeverButImg = BeverButImg.subsample(1,1)

NoodButImg = PhotoImage(file="NoodBut.png")
NoodButImg = NoodButImg.subsample(1,1)

SandwitButImg = PhotoImage(file="SandBut.png")
SandwitButImg = SandwitButImg.subsample(1,1)

SaladButImg = PhotoImage(file="SaladBut.png")
SaladButImg = SaladButImg.subsample(1,1)

MainCoButImg = PhotoImage(file="MainCoBut.png")
MainCoButImg = MainCoButImg.subsample(1,1)

PayButImg = PhotoImage(file="pay-button.png")
PayButImg = PayButImg.subsample(9,9)

AddDishButImg = PhotoImage(file="Add_Dish.png")
AddDishButImg = AddDishButImg.subsample(9,9)

DeleteDishButImg = PhotoImage(file="Delete_Dish.png")
DeleteDishButImg = DeleteDishButImg.subsample(9,9)

tilt_Lab = Label(Mframe,image=TitleImg,text="Nitin's Kitchen",bg='#9AD2A1',fg='red',font=('Chiller',32,'bold'),
                 compound='left')
tilt_Lab.place(x=100,y=50)

chef_Lab = Label(Mframe,image=ChefImg,bg='#9AD2A1')
chef_Lab.place(x=100,y=210)


def FrameRaise_ButFun(framNam):
    root.geometry("948x660+220+20")
    framNam.tkraise()


def BillFrameRaiseFun():
    root.geometry("474x660+500+20")
    M3frame.tkraise()

def addMoreDishies():
    addDishroot = Toplevel()
    addDishroot.title("Add More Dishes")
    addDishroot.geometry("500x500")

    Label(addDishroot,text='Menu').place(x=30,y=50)
    menuval = StringVar()
    menuList = ttk.Combobox(addDishroot,width=20,textvariable =menuval)
    menuList['values'] = ('starter','sandwiches','pizzas','noodles','main_course','dessert','beveages')
    menuList.place(x=100,y=50)

    lab = Label(addDishroot,text = menuList.get(),bg = 'red')
    lab.place(x=100,y=100)
    addDishroot.mainloop()

def deleteMoreDishies():
    pass


Str_Button = Button(Mframe,image=StarterButImg,command=lambda:FrameRaise_ButFun(Startframe),height=38,width=160,
                    text=" Starter's",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Str_Button.place(x=60,y=170)

piz_Button = Button(Mframe,image=PizzaButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(Pizzaframe),
                    text="  PIZZA",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
piz_Button.place(x=270,y=170)

Des_Button = Button(Mframe,image=DeserButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(Dessframe),
                    text="  Dessert",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Des_Button.place(x=60,y=260)

Brev_Button = Button(Mframe,image=BeverButImg,height=38,command=lambda:FrameRaise_ButFun(Breveframe),width=160,
                     text="   Beverages",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Brev_Button.place(x=270,y=260)

Nod_Button = Button(Mframe,image=NoodButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(Noodframe),
                    text=" Noodle's",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Nod_Button.place(x=60,y=350)

SAND_Button = Button(Mframe,image=SandwitButImg,height=38,command=lambda:FrameRaise_ButFun(SandWframe),width=160,
                     text="Sandwich's",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
SAND_Button.place(x=270,y=350)

Salad_Button = Button(Mframe,image=SaladButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(Saladframe),
                      text="  Salad",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
Salad_Button.place(x=60,y=440)

MAN_Button = Button(Mframe,image=MainCoButImg,height=38,width=160,command=lambda:FrameRaise_ButFun(MainCoframe),
                    text="Main Course",bg='#DDBA51',font=('Times',14,'bold'),bd="4",compound='left')
MAN_Button.place(x=270,y=440)

Pay_Button = Button(Mframe,image=PayButImg,bg="#9AD2A1",font=('Times',14,'bold'),command=BillFrameRaiseFun,
                    borderwidth=0)
Pay_Button.place_forget()

AddDish_Button = Button(Mframe,image=AddDishButImg,bg="#9AD2A1",font=('Times',14,'bold'),command=addMoreDishies,
                        borderwidth=0)
AddDish_Button.place(x=120,y=500)

DeleteDish_Button = Button(Mframe,image=DeleteDishButImg,bg="#9AD2A1",font=('Times',14,'bold'),command=deleteMoreDishies,
                        borderwidth=0)
DeleteDish_Button.place(x=220,y=500)


def BillingFun(Item,ItmPrice,itmAmount,TotalAmt):
    global BillPrintLine
    BillArea.insert(BillPrintLine,f'  {Item}\t\t\t\t{ItmPrice}\t {itmAmount}\t {TotalAmt}\n')
    global Grand_total
    Grand_total += TotalAmt
    BillPrintLine += 1
    Pay_Button.place(x=320,y=505)


def SelectedFrameFun(itm,price):
    Selectroot = Toplevel()
    Selectroot.geometry("500x340+500+200")
    Selectroot.title("Selected Item")
    Selectroot.resizable(False,False)

    Selectbg = PhotoImage(file="SelectItemBg1.png")
    Selectbg = Selectbg.subsample(1,2)

    SelectCan = Canvas(Selectroot,relief="ridge",bg='#E4B388',bd=4)
    SelectCan.place(x=0,y=0,relwidth=1,relheight=1)

    SelectCan.create_image((0,0),image=Selectbg,anchor=NW)
    SelectCan.create_text((73,107),text='Item :',anchor=NW,font=('Georgia',13,'italic bold'),fill='black')
    SelectCan.create_text((160,107),text=itm,anchor=NW,font=('Courier New',15,'italic bold'),fill='red')
    SelectCan.create_text((70,160),text='Amount :',anchor=NW,font=('Georgia',13,'italic bold'),fill='black')
    SelectCan.create_text((160,158),text=price,anchor=NW,font=('Georgia',14,'bold'),fill='red')
    SelectCan.create_text((70,220),text="Quantity : ",anchor=NW,font=('Georgia',13,'italic bold'),fill='black')

    Quant = StringVar()
    QuantVal = Entry(SelectCan,textvariable=Quant,width=5,fg='red',relief='groove',bd=4,font=('Georgia',15,'bold'))
    QuantVal.place(x=170,y=215)
    QuantVal.focus()
    Quant.set('')

    def addToBill():
        if Quant.get() == '':
            messagebox.showerror('ERROR',"Amount Cannot Be Empty !!!",parent=Selectroot)
        else:
            try:
                x = int(Quant.get())
                total = x * int(price)
                BillingFun(itm,price,Quant.get(),total)
                QuantVal.delete(0,END)
                Selectroot.destroy()

            except ValueError:
                messagebox.showerror('ERROR',"Amount Must be Number !!!",parent=Selectroot)
                QuantVal.delete(0,END)

    SelSubmitBut = Button(SelectCan,text="Select",bg='#B97B3F',fg='white',bd=5,font=('Georgia',12,'bold'),
                          command=addToBill)
    SelSubmitBut.place(x=130,y=270)

    def SelCancelButFun():
        Selectroot.destroy()

    SelCancelBut = Button(SelectCan,text="Cancel",bg='#B97B3F',fg='white',bd=5,font=('Georgia',12,'bold'),
                          command=SelCancelButFun)
    SelCancelBut.place(x=230,y=270)

    Selectroot.mainloop()


##Starter Frame
Startframe = Frame(root,bg='#232731',relief="ridge",bd="3")
Startframe.place(x=474,y=0,relheight=1,width=474)

starbg = PhotoImage(file="StarterBg.png")
starbg = starbg.subsample(2,2)

starTitlImg = PhotoImage(file="StarterTitleImg.png")
starTitlImg = starTitlImg.subsample(7,7)

StarCan = Canvas(Startframe)
StarCan.place(x=0,y=0,relwidth=1,relheight=1)

StarCan.create_image((0,0),image=starbg,anchor=NW)
StarCan.create_image((80,70),image=starTitlImg,anchor=NW)
StarCan.create_text((160,70),text="STARTER",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Startminiframe = Frame(Startframe,bg='#232731',relief="ridge",bd="4")
Startminiframe.place(x=20,y=200,height=300)

# Startilt_Lab = Label(Startframe,image = TitleImg,text = "STARTER",bg = '#232731',fg= 'red',font = ('Chiller', 50,'bold'),compound ='left')
# Startilt_Lab.place(x=90,y=50)

Scrolly = Scrollbar(Startminiframe,orient="vertical")

style = ttk.Style()
style.theme_use('clam')
style.configure('Start.Treeview',font=('times',15,'italic'),fieldbackground='#394051',foreground='white',
                background='#394051',rowheight=50)
style.configure('Start.Treeview.Heading',font=('Chiller',18,'bold'),foreground='red',background='#232731')
style.map('Start.Treeview',background=[('selected','#232731')],foreground=[('selected','white')])

starttab = Treeview(Startminiframe,columns=('Menu','Price'),style="Start.Treeview",yscrollcommand=Scrolly.set)

Scrolly.pack(side='right',fill='y',anchor=N)

Scrolly.configure(command=starttab.yview)

starttab.column("#0",width=0,stretch=NO)
starttab.column("Menu",width=300)
starttab.column("Price",width=100,anchor=CENTER)

starttab.heading('#0',text="")
starttab.heading('Menu',text="MENU")
starttab.heading('Price',text="PRICE")

starttab.pack(fill='both')

con = pymysql.connect(host="localhost",user='root',password='')
mycursor = con.cursor()
query = "use Hotel;"
mycursor.execute(query)

# dict1 = {}
# for key in dict1:
#     q = 'insert into Starter values(%s ,%s);'
#     mycursor.execute(q,(key,dict1[key]))

mycursor.execute("select * from Starter;")
data = mycursor.fetchall()
for i in data:
    starttab.insert('',END,values=(i[0],i[1]))


def on_select(event):
    a = starttab.focus()
    value = starttab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


starttab.bind('<Double-1>',on_select)

# ## PIZZA Frame
Pizzaframe = Frame(root,bg='#DC8480',relief="ridge",bd="4")
Pizzaframe.place(x=474,y=0,relheight=1,width=474)

Pizzabg = PhotoImage(file="PizzaFrameBg.png")
Pizzabg = Pizzabg.subsample(1,1)

PizzCan = Canvas(Pizzaframe)
PizzCan.place(x=0,y=0,relwidth=1,relheight=1)

PizzCan.create_image((0,0),image=Pizzabg,anchor=NW)
PizzCan.create_text((160,70),text="Pizza's",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Pizzminiframe = Frame(Pizzaframe,bg='#C64E1D',relief="ridge",bd="4")
Pizzminiframe.place(x=50,y=190,height=300)

PizzScrolly = Scrollbar(Pizzminiframe,orient="vertical")

style.configure('Pizz.Treeview',font=('times',15,'italic'),fieldbackground='#C64E1D',foreground='white',
                background='#C64E1D',rowheight=50)
style.configure('Pizz.Treeview.Heading',font=('Chiller',18,'bold'),foreground='red',background='#E7B237')
style.map('Pizz.Treeview',background=[('selected','#7A3218')],foreground=[('selected','white')])

Pizztab = Treeview(Pizzminiframe,columns=('Menu','Price'),style='Pizz.Treeview',yscrollcommand=PizzScrolly.set)

PizzScrolly.pack(side='right',fill='y',anchor=N)
PizzScrolly.configure(command=Pizztab.yview)

Pizztab.column("#0",width=0,stretch=NO)
Pizztab.column("Menu",width=248)
Pizztab.column("Price",width=100,anchor=CENTER)

Pizztab.heading('#0',text="")
Pizztab.heading('Menu',text="MENU")
Pizztab.heading('Price',text="PRICE")

Pizztab.pack(fill='both')

mycursor.execute("select * from Pizzas;")
data = mycursor.fetchall()
for i in data:
    Pizztab.insert('',END,values=(i[0],i[1]))


def on_piz_select(event):
    a = Pizztab.focus()
    value = Pizztab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Pizztab.bind('<Double-1>',on_piz_select)

## Dessert Frame
Dessframe = Frame(root,bg='#DC8480',relief="ridge",bd="4")
Dessframe.place(x=474,y=0,relheight=1,width=474)

Dessbg = PhotoImage(file="DessBackGImg.png")
Dessbg = Dessbg.subsample(1,1)

# DessTitlImg = PhotoImage(file = "IceCreame.png")
# DessTitlImg = DessTitlImg.subsample(8,8)

DessCan = Canvas(Dessframe)
DessCan.place(x=0,y=0,relwidth=1,relheight=1)

DessCan.create_image((0,0),image=Dessbg,anchor=NW)
DessCan.create_text((160,70),text="Dessert",font=('Chiller',50,'bold'),fill='red',anchor=NW)
# DessCan.create_image((80,150),image = DessTitlImg ,anchor =NW)

Dessminiframe = Frame(Dessframe,bg='#232731',relief="ridge",bd="4")
Dessminiframe.place(x=20,y=200,height=300)

DessScrolly = Scrollbar(Dessminiframe,orient="vertical")

style.configure('Dess.Treeview',font=('times',15,'italic'),fieldbackground='#F4D0DC',foreground='black',
                background='#F4D0DC',rowheight=50)
style.configure('Dess.Treeview.Heading',font=('Chiller',18,'bold'),foreground='red',background='pink')
style.map('Dess.Treeview',background=[('selected','#FF537B')],foreground=[('selected','white')])

Desstab = Treeview(Dessminiframe,columns=('Menu','Price'),style='Dess.Treeview',yscrollcommand=DessScrolly.set)

DessScrolly.pack(side='right',fill='y',anchor=N)

DessScrolly.configure(command=Desstab.yview)

Desstab.column("#0",width=0,stretch=NO)
Desstab.column("Menu",width=300)
Desstab.column("Price",width=100,anchor=CENTER)

Desstab.heading('#0',text="")
Desstab.heading('Menu',text="MENU")
Desstab.heading('Price',text="PRICE")

Desstab.pack(fill='both')

mycursor.execute("select * from Dessert;")
data = mycursor.fetchall()
for i in data:
    Desstab.insert('',END,values=(i[0],i[1]))


def on_des_select(event):
    a = Desstab.focus()
    value = Desstab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Desstab.bind('<Double-1>',on_des_select)

# ## Breverages Frame
Breveframe = Frame(root,bg='#DC8480',relief="ridge",bd="4")
Breveframe.place(x=474,y=0,relheight=1,width=474)

Brevebg = PhotoImage(file="BreverageFrameBg.png")
Brevebg = Brevebg.subsample(1,1)

BreveCan = Canvas(Breveframe)
BreveCan.place(x=0,y=0,relwidth=1,relheight=1)

BreveCan.create_image((0,0),image=Brevebg,anchor=NW)
BreveCan.create_text((130,70),text="Breverage's",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Breveminiframe = Frame(Breveframe,bg='#C64E1D',relief="ridge",bd="4")
Breveminiframe.place(x=45,y=200,height=300)

BreveScrolly = Scrollbar(Breveminiframe,orient="vertical")

style.configure('Breve.Treeview',font=('times',15,'italic'),fieldbackground='#FDD768',foreground='black',
                background='#FDD768',rowheight=50)
style.configure('Breve.Treeview.Heading',font=('Chiller',18,'bold'),foreground='red',background='#E7B237')
style.map('Breve.Treeview',background=[('selected','#FF992B')],foreground=[('selected','white')])

Brevetab = Treeview(Breveminiframe,columns=('Menu','Price'),style='Breve.Treeview',yscrollcommand=BreveScrolly.set)

BreveScrolly.pack(side='right',fill='y',anchor=N)
BreveScrolly.configure(command=Brevetab.yview)

Brevetab.column("#0",width=0,stretch=NO)
Brevetab.column("Menu",width=260)
Brevetab.column("Price",width=100,anchor=CENTER)

Brevetab.heading('#0',text="")
Brevetab.heading('Menu',text="MENU")
Brevetab.heading('Price',text="PRICE")

Brevetab.pack(fill='both')

mycursor.execute("select * from Breveges;")
data = mycursor.fetchall()
for i in data:
    Brevetab.insert('',END,values=(i[0],i[1]))


def on_brev_select(event):
    a = Brevetab.focus()
    value = Brevetab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Brevetab.bind('<Double-1>',on_brev_select)

## Noodles Frame
Noodframe = Frame(root,bg='#2EAC63',relief="ridge",bd="4")
Noodframe.place(x=474,y=0,relheight=1,width=474)

Noodbg = PhotoImage(file="NoodleFrameBg.png")
Noodbg = Noodbg.subsample(1,1)

Noodtitlebg = PhotoImage(file="ChineseFrameTitlBg.png")
Noodtitlebg = Noodtitlebg.subsample(1,1)

NoodCan = Canvas(Noodframe)
NoodCan.place(x=0,y=0,relwidth=1,relheight=1)

NoodCan.create_image((0,0),image=Noodbg,anchor=NW)
NoodCan.create_image((20,40),image=Noodtitlebg,anchor=NW)
NoodCan.create_text((140,65),text="NOODLES",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Noodminiframe = Frame(Noodframe,bg='#DBD6CE',relief="ridge",bd="4")
Noodminiframe.place(x=25,y=200,height=300)

NoodleScrolly = Scrollbar(Noodminiframe,orient="vertical")

style.configure('Nood.Treeview',font=('times',15,'italic'),fieldbackground='#B6FFB0',foreground='black',
                background='#B6FFB0',rowheight=50)
style.configure('Nood.Treeview.Heading',font=('Chiller',18,'bold'),foreground='white',background='#15B90A')
style.map('Nood.Treeview',background=[('selected','#2EAC63')],foreground=[('selected','white')])

Noodletab = Treeview(Noodminiframe,columns=('Menu','Price'),style='Nood.Treeview',yscrollcommand=NoodleScrolly.set)

NoodleScrolly.pack(side='right',fill='y',anchor=N)

NoodleScrolly.configure(command=Noodletab.yview)

Noodletab.column("#0",width=0,stretch=NO)
Noodletab.column("Menu",width=300)
Noodletab.column("Price",width=100,anchor=CENTER)

Noodletab.heading('#0',text="")
Noodletab.heading('Menu',text="MENU")
Noodletab.heading('Price',text="PRICE")

Noodletab.pack(fill='both')

mycursor.execute("select * from Noodles;")
data = mycursor.fetchall()
for i in data:
    Noodletab.insert('',END,values=(i[0],i[1]))


def on_Nod_select(event):
    a = Noodletab.focus()
    value = Noodletab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Noodletab.bind('<Double-1>',on_Nod_select)

## Sandwich's  Frame
SandWframe = Frame(root,bg='#E6D1A4',relief="ridge",bd="4")
SandWframe.place(x=474,y=0,relheight=1,width=474)

Sandbg = PhotoImage(file="SandBackGImg.png")
Sandbg = Sandbg.subsample(1,1)

SandCan = Canvas(SandWframe)
SandCan.place(x=0,y=0,relwidth=1,relheight=1)

SandCan.create_image((0,0),image=Sandbg,anchor=NW)
SandCan.create_text((100,80),text="SANDWICH'S",font=('Chiller',50,'bold'),fill='red',anchor=NW)

Sandminiframe = Frame(SandWframe,bg='#E6D1A4',relief="ridge",bd="4")
Sandminiframe.place(x=20,y=200,height=300)

SandWScrolly = Scrollbar(Sandminiframe,orient="vertical")

style.configure('Sand.Treeview',font=('times',15,'italic'),fieldbackground='#E6D1A4',foreground='black',
                background='#E6D1A4',rowheight=50)
style.configure('Sand.Treeview.Heading',font=('Chiller',18,'bold'),foreground='white',background='#CB8A4D')
style.map('Sand.Treeview',background=[('selected','#9E3D12')],foreground=[('selected','white')])

SandWtab = Treeview(Sandminiframe,columns=('Menu','Price'),style='Sand.Treeview',yscrollcommand=SandWScrolly.set)

SandWScrolly.pack(side='right',fill='y',anchor=N)

SandWScrolly.configure(command=Noodletab.yview)

SandWtab.column("#0",width=0,stretch=NO)
SandWtab.column("Menu",width=300)
SandWtab.column("Price",width=100,anchor=CENTER)

SandWtab.heading('#0',text="")
SandWtab.heading('Menu',text="MENU")
SandWtab.heading('Price',text="PRICE")

SandWtab.pack(fill='both')

mycursor.execute("select * from Sandwiches;")
data = mycursor.fetchall()
for i in data:
    SandWtab.insert('',END,values=(i[0],i[1]))


def on_Sand_select(event):
    a = SandWtab.focus()
    value = SandWtab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


SandWtab.bind('<Double-1>',on_Sand_select)

## Salad's  Frame
Saladframe = Frame(root,bg='#E6D1A4',relief="ridge",bd="4")
Saladframe.place(x=474,y=0,relheight=1,width=474)

Saladbg = PhotoImage(file="saladFrameBg.png")
Saladbg = Saladbg.subsample(1,1)

SaladCan = Canvas(Saladframe)
SaladCan.place(x=0,y=0,relwidth=1,relheight=1)

SaladCan.create_image((0,0),image=Saladbg,anchor=NW)
SaladCan.create_text((160,80),text="Salad'S",font=('Chiller',50,'bold'),fill='white',anchor=NW)

Saladminiframe = Frame(Saladframe,bg='#E6D1A4',relief="ridge",bd="4")
Saladminiframe.place(x=20,y=200,height=300)

SaladScrolly = Scrollbar(Saladminiframe,orient="vertical")

style.configure('Salad.Treeview',font=('times',15,'italic'),fieldbackground='#C3D7BB',foreground='black',
                background='#C3D7BB',rowheight=50)
style.configure('Salad.Treeview.Heading',font=('Chiller',18,'bold'),foreground='white',background='#586E1B')
style.map('Salad.Treeview',background=[('selected','#78E8B7')],foreground=[('selected','blue')])

Saladtab = Treeview(Saladminiframe,columns=('Menu','Price'),style='Salad.Treeview',yscrollcommand=SaladScrolly.set)

SaladScrolly.pack(side='right',fill='y',anchor=N)

SaladScrolly.configure(command=Noodletab.yview)

Saladtab.column("#0",width=0,stretch=NO)
Saladtab.column("Menu",width=300)
Saladtab.column("Price",width=100,anchor=CENTER)

Saladtab.heading('#0',text="")
Saladtab.heading('Menu',text="MENU")
Saladtab.heading('Price',text="PRICE")

Saladtab.pack(fill='both')

mycursor.execute("select * from Salad;")
data = mycursor.fetchall()
for i in data:
    Saladtab.insert('',END,values=(i[0],i[1]))


def on_Salad_select(event):
    a = Saladtab.focus()
    value = Saladtab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


Saladtab.bind('<Double-1>',on_Salad_select)

## Main Course  Frame
MainCoframe = Frame(root,bg='#810322',relief="ridge",bd="4")
MainCoframe.place(x=474,y=0,relheight=1,width=474)

Mainbg = PhotoImage(file="MainCorseFrameBg.png")
Mainbg = Mainbg.subsample(1,1)

MainCan = Canvas(MainCoframe)
MainCan.place(x=0,y=0,relwidth=1,relheight=1)

MainCan.create_image((0,0),image=Mainbg,anchor=NW)
MainCan.create_text((100,80),text="Main Course",font=('Chiller',50,'bold'),fill='white',anchor=NW)

MainCominiframe = Frame(MainCoframe,bg='#810322',relief="ridge",bd="4")
MainCominiframe.place(x=20,y=200,height=300)

MainCoScrolly = Scrollbar(MainCominiframe,orient="vertical")

style.configure('Main.Treeview',font=('times',15,'italic'),fieldbackground='#FF8173',foreground='black',
                background='#FF8173',rowheight=50)
style.configure('Main.Treeview.Heading',font=('Chiller',18,'bold'),foreground='white',background='#C72319')
style.map('Main.Treeview',background=[('selected','#C72319')],foreground=[('selected','white')])

MainCotab = Treeview(MainCominiframe,columns=('Menu','Price'),style='Main.Treeview',yscrollcommand=MainCoScrolly.set)

MainCoScrolly.pack(side='right',fill='y',anchor=N)

MainCoScrolly.configure(command=MainCotab.yview)

MainCotab.column("#0",width=0,stretch=NO)
MainCotab.column("Menu",width=300)
MainCotab.column("Price",width=100,anchor=CENTER)

MainCotab.heading('#0',text="")
MainCotab.heading('Menu',text="MENU")
MainCotab.heading('Price',text="PRICE")

MainCotab.pack(fill='both')

mycursor.execute("select * from Main_Course;")
data = mycursor.fetchall()
for i in data:
    MainCotab.insert('',END,values=(i[0],i[1]))


def on_Sand_select(event):
    a = MainCotab.focus()
    value = MainCotab.item(a,'values')
    menu = value[0]
    MenuPrice = value[1]
    SelectedFrameFun(menu,MenuPrice)


MainCotab.bind('<Double-1>',on_Sand_select)

## BILL FRAME

M3frame = Frame(root,bg='#A47E52',relief="ridge",bd="4")
M3frame.place(x=0,y=0,relheight=1,width=474)

Billbg = PhotoImage(file="BillBackImg.png")
Billbg = Billbg.subsample(1,1)

BillTitlImg = PhotoImage(file="Bill.png")
BillTitlImg = BillTitlImg.subsample(4,4)

BillCan = Canvas(M3frame)
BillCan.place(x=0,y=0,relwidth=1,relheight=1)

BillCan.create_image((0,0),image=Billbg,anchor=NW)

BillCan.create_image((50,60),image=BillTitlImg,anchor=NW)
BillCan.create_text((100,70),text="Bill Board",font=('Courier New',30,'italic bold'),fill='brown',anchor=NW)

BillBominiframe = Frame(M3frame,bg='#D3B27F',relief="ridge",bd="2")
BillBominiframe.place(x=35,y=150,height=400,width=400)

Bill_Lab = Label(BillBominiframe,text='Nitin\'s Kitchen',bg='white',font=('Chiller',15,'bold underline'),fg='red')
Bill_Lab.place(x=0,y=0,relwidth=1)

BillArea = Text(BillBominiframe,font=('Courier New',9,'italic bold'),relief="flat")
BillArea.place(x=0,y=30,height=365,relwidth=1)
BillArea.insert(1.0,'\t\t\tCash Bill')

bill_no = random.randint(1000,9999)
BillArea.insert(END,'\n\n   Bill No:' + str(bill_no))
date = time.strftime("%d/%m/%y")
BillArea.insert(END,'\t\t\t\t\t Date:' + date)
BillArea.insert(END,'\n  ____________________________________________________')
BillArea.insert(END,'\n   ITEM\t\t\t\tPRICE\tQTY\t TOTAL')
BillArea.insert(END,'\n  ____________________________________________________ \n')


def Generate_billFun():
    BillArea.insert(END,'\n  ____________________________________________________')
    BillArea.insert(END,f'\n   Grand Total\t\t\t\t\t\t{Grand_total}\n')
    BillArea.insert(END,'  ____________________________________________________ ')
    BillArea.insert(END,'\n\n\t  THANK YOU... VISIT AGAIN !!!')


BillBut = Button(M3frame,text="Generate Bill",font=('Georgia',12,'bold'),fg='white',bg='#A47E52',bd=4,
                 command=Generate_billFun)
BillBut.place(x=85,y=570)


def Addmoreitem():
    BillArea.delete(BillPrintLine + 1,END)
    Mframe.tkraise()


BillAddMorBut = Button(M3frame,text="Add More",font=('Georgia',12,'bold'),fg='white',bg='#A47E52',bd=4,
                       command=Addmoreitem)
BillAddMorBut.place(x=300,y=570)

Mframe.tkraise()
root.mainloop()
