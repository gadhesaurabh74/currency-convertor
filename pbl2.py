from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tmsg
from tkinter import filedialog
from PIL import Image,ImageTk
import requests
import json



#initializing window
windows = Tk()
windows.title('Currency Converter')
windows.geometry("845x460")
windows.configure(background="MediumPurple1")


#defining function
def conversion():
    global converted
    statusvar.set("your amount is converting...")
    sbar.update()
    import time
    time.sleep(2)
    # main code for currency conversion
    statusvar.set("your amount is converted")
    currency_1 = from_currency_combobox.get()
    currency_2 = to_currency_combobox.get()
    amount_1 = float(amount_entry.get())
    result_1 = requests.get(f'https://v6.exchangerate-api.com/v6/ab50ff14aaf8efda83f456d1/pair/{currency_1}/{currency_2}/{amount_1}').json()
    converted = result_1['conversion_result']
    
    formatted_result = f'{amount_1} {currency_1} = {converted} {currency_2}'
    result.config(text = formatted_result)
    
    statusvar.set("your amount is converted")
    f=open('data.txt','a')
    import datetime
    timestamp=datetime.datetime.now()
    f.write(f" date and time={timestamp}\n")
    f.write(f"from currency:{currency_1} , to currency:{currency_2} , Amount:{amount_1} , converted amount:{converted}\n")
    f.write(f"Exchange rate: 1 {currency_1}={float(converted)/float(amount_1)} {currency_2}\n")

    
    def clear_fields(): 
        amount_entry.delete(0,END) 
    #clear button
    f10= Frame(f9, width = 50, height = 5,bg="dark salmon",borderwidth=4,relief=SUNKEN)
    f10.grid(row = 5, column = 2,padx=5,pady=5)
    Button(f10,text="Clear",font='times 20 bold',command=clear_fields,bg='dark blue').grid()

    def exit():
        menubar.destroy()
        sbar.destroy()
        
        for item in Frame_list:
            item.destroy()
        windows.geometry("845x610")
        #end statement
        end_label=Label(windows,text="Thanks for using our Convertor!",font="comicsansn 30 bold",fg="light blue",anchor="nw",justify=LEFT,bg="green")
        end_label.grid(column=0,row=0,padx=100)
        #end image
        global newimage
        image=Image.open("photo.jpg")
        resized=image.resize((600,400),Image.ANTIALIAS)
        newimage=ImageTk.PhotoImage(resized)
        newimage_label=Label(windows,image=newimage)
        newimage_label.grid(column=0,row=1,pady=20,padx=20)

        end_label=Label(windows,text="Have a nice Day!!",font="comicsansn 30 bold",fg="light blue",anchor="nw",justify=LEFT,bg="green")
        end_label.grid(column=0,row=2,pady=10)
        def ok():
            quit()
        Button(windows,text="OK",command=ok).grid(column=0,row=3,padx=10,ipadx=10,ipady=3)
        
        

    #exit button
    f12= Frame(f9, width = 50, height = 5,bg="dark salmon",borderwidth=4,relief=SUNKEN)
    f12.grid(row = 5,column = 3,padx=5,pady=5)
    Button(f12,text = "Exit",font='times 20 bold',command=exit,bg='dark blue').grid()
    

def login():
    import loginpage

def feedback():
    child_windows_1=Toplevel(windows)
    child_windows_1.geometry("900x630")
    child_windows_1.configure(background="peach puff")
    def submit():
        add=open("data.txt","a")
        add.write(textarea.get(1.0,END))
        add.write("\n")
        add.close()
        child_windows_1.destroy()
        tmsg.showinfo("THANKS","Thanks for your feedback.Have a nice day!!!")
    #feedback tab 
    review=Label(child_windows_1,text="Please enter your feedback",font="comicsansn 20 bold")
    review.grid(row=2,column=0)
    textarea=Text(child_windows_1,font="lucida 14 bold")
    textarea.grid(row=3)
    f0= Frame(child_windows_1, width = 50, height = 5,bg="peach puff",borderwidth=4,relief=SUNKEN)
    f0.grid(row = 4,column = 0,padx=5,pady=5)
    Button(f0,text='submit',command=submit,bg="dark blue",fg="white").grid(row=4,ipadx=10)
    
def delete():
    result.delete(0,'end')
    currency_1.delete(0,'end')
    currency_2.delete(0,'end')
    amount_1.delete(0,'end')
    result_1 .delete(0,'end')
    
def rating():
    child_windows_2=Toplevel(windows)
    child_windows_2.geometry("300x150")
    child_windows_2.configure(background="peach puff")
    def Submit():
        tmsg.showinfo("THANKS",f"Thanks for giving us {r.get()} scale rating!!!")
        child_windows_2.destroy()
    l=Label(child_windows_2,text="Give us rating",bg="white")
    l.grid()
    r=Scale (child_windows_2, from_=1 ,to =5, length=300,width=60,orient=HORIZONTAL,bg="grey")
    r.grid()
    store=open("data.txt","a")
    store.write(f" rating={r.get()}")
    store.write("\n")
    store.close()
    f_10= Frame(child_windows_2, width = 50, height = 5,bg="dark salmon",borderwidth=4,relief=SUNKEN)
    f_10.grid(row = 3, column = 0,padx=5,pady=5)
    #submit button
    Button(f_10,text="submit",command=Submit,bg="dark blue",fg="white").grid(row=3)

def History():
    child_windows_3=Toplevel(windows)
    child_windows_3.geometry("300x150")
    child_windows_3.configure(background="peach puff")
    text_widget = tk.Text(child_windows_3)
    text_widget.pack(fill='both', expand=True)
    
    with open('C:\\Users\\DELL\\OneDrive\\Desktop\\python pbl\\data.txt', 'r') as file:
        contents = file.read()
        text_widget.insert(tk.INSERT, contents)

    





#creating frames
f1 = Frame(windows, width = 5, height = 5,bg="MediumPurple1",borderwidth=2,relief=SUNKEN)
f1.grid(row = 0, column = 0,padx=5,pady=0)
f2= Frame(windows, width = 50, height = 5,bg="dark green",borderwidth=8,relief=SUNKEN)
f2.grid(row=1, column = 0,padx=5,pady=0)
#f3= Frame(windows, width = 50, height = 5,bg="dark salmon",borderwidth=1,relief=SUNKEN)
#f3.grid(row=2, column = 0,padx=10,pady=10)
f4= Frame(windows, width = 100, height = 5,bg="dark salmon",borderwidth=4,relief=SUNKEN)
f4.grid(row = 3, column = 0,padx=10,pady=10)
f5= Frame(f4, width = 100, height = 5,bg="dark salmon",borderwidth=4,relief=SUNKEN)
f5.grid(row = 3, column = 0,padx=10,pady=10)
f6= Frame(f4, width = 100, height = 5,bg="dark salmon",borderwidth=4,relief=SUNKEN)
f6.grid(row = 3, column = 1,padx=10,pady=10)
f7= Frame(f4, width = 50, height = 5,bg="dark salmon",borderwidth=4,relief=SUNKEN)
f7.grid(row = 3, column = 2,padx=5,pady=5)
f8= Frame(windows, width = 50, height = 5,bg="dark salmon",borderwidth=2,relief=SUNKEN)
f8.grid(row = 4, column = 0,padx=5,pady=5)
f9= Frame(windows, width = 50, height = 5,bg="MediumPurple1",borderwidth=2,relief=SUNKEN)
f9.grid(row = 5,column = 0,padx=5,pady=5)
f11= Frame(f9, width = 50, height = 5,bg="dark salmon",borderwidth=4,relief=SUNKEN)
f11.grid(row = 5,column = 0,padx=5,pady=5)
Frame_list=[f1,f2,f4,f5,f6,f7,f8,f9,f11]

#Title
name_label = Label(f2, text = 'WELCOME TO SMART CURRENCY CONVERTER', bg = 'green', font = ('TimesRoman 20 bold'),fg='red',anchor="w",justify=LEFT) 
name_label.grid(pady=4,padx=5,ipadx=23)


#API KEY
API_KEY = "ab50ff14aaf8efda83f456d1"
url = f'https://v6.exchangerate-api.com/v6/ab50ff14aaf8efda83f456d1/latest/USD'
response = requests.get(f'{url}').json()
currencies = dict(response['conversion_rates'])


#from currency
from_currency = Label(f5, text = 'From Currency:', font = ('Times 20 bold'),bg='dark salmon') 
from_currency.grid(pady=10,padx=5)
#from_currency_combobox['values'] = ('US Dollar', 'Indian Rupees', 'EU Euro', 'Chinese Yuan', 'Japanese Yen', 'UK Pound', 'UAE Dirham')
from_currency_combobox = ttk.Combobox(f5, values = list(currencies.keys()), width = 14, font = ('Times 10 bold'))
from_currency_combobox.grid(pady=10,padx=5,ipady=10)

#to currency
to_currency = Label(f6, text = 'To Currency :', font = ('Times 20 bold'),bg='dark salmon') 
to_currency.grid(pady=10,padx=10,ipadx=5)
#to_currency_combobox['values'] = ('US Dollar', 'Indian Rupees', 'EU Euro', 'Chinese Yuan', 'Japanese Yen', 'UK Pound', 'UAE Dirham')
to_currency_combobox = ttk.Combobox(f6, values = list(currencies.keys()) , width = 14, font = ('Times 10 bold'))
to_currency_combobox.grid(pady=10,padx=10,ipady=10)

#amount
amount = Label(f7, text = 'Amount :', font = ('Times 20 bold'),bg='dark salmon')
amount.grid(pady=10,padx=10,ipadx=30)
amount_entry = Entry(f7, width = 14, font = ('Times 10 bold'))
amount_entry.grid(pady=10,padx=10,ipady=10)

#convert button
convert_button = Button(f8, text = 'Convert', font = ('Times 20 bold'), command = conversion,bg='dark blue',fg="white")
convert_button.grid(pady=2)

#converted amount
result_text = Label(f11, text = 'Result:', font = 'Times 20 bold',bg="dark salmon")
result_text.grid(row=5)
result = Label(f11, text = '     ', font = 'Times 20 bold')
result.grid(row=6,pady=10,ipadx=80)

#addition of statusbar
statusvar=StringVar()
statusvar.set("Enter Amount")
sbar=Label(windows,textvariable=statusvar,relief=SUNKEN,anchor="w",width=120,justify=LEFT)
sbar.grid(row=7,column=0)


#menubar
menubar=Menu(f1)

windows.config(menu=menubar)
menubar.add_cascade(label="login",command=login)


#how to use button
m1=Menu(menubar)
m1.add_command(label="Step 1. Enter currency code from which you want to convert your currency")
m1.add_command(label="Step 2. Enter currency code to which you want to convert your currency")
m1.add_command(label="Step 3. Enter the Amount which you want to convert")
m1.add_command(label="Step 4. Press the convert button and your amount will be converted")
m1.add_command(label="Step 5. If you Dont know the currency code please refer the help tab")
windows.config(menu=menubar)
menubar.add_cascade(label="How to use",menu=m1)

#heip tab
m2=Menu(menubar)
m2.add_command(label="1.US:USD(dollar)")
m2.add_command(label="2.UK:GBP(UK POUND)")
m2.add_command(label="3.JAPAN:JPY(JAP.YEN)")
m2.add_command(label="4.INDIA:INR(INDIAN RUPEES)")
m2.add_command(label="5.CHINA:CNY(RENMINBI)")
m2.add_command(label="6.EU COUNTRIES:EUR(EURO)")
m2.add_command(label="7.RUSSIA:RUR(RUSSIAN RUBLE)")
m2.add_command(label="8.CANADA:CAD(CANADIAN DOLLAR)")
m2.add_command(label="9.DENMARK:DKK(DAN KRONER)")
m2.add_command(label="10.AUSTRALIA: AUD (AUSTRALIAN DOLLAR)")
m2.add_command(label="11.EGYPT: EGP (EGYPTIAN POUND)")
m2.add_command(label="12.HONG KONG: HKD (HONG KONG DOLLAR)")
m2.add_command(label="13.INDONESIA: IDR (RUPIAH)")
m2.add_command(label="14.IRAN: IRR (IRANIAN RIAL)")
m2.add_command(label="15.SRI LANKA:LKR(SRI LANKA RUPEE)")
m2.add_command(label="16.SWITZERLAND:CHF(SWISS FRANC)")
m2.add_command(label="17.THAILAND:THB(THAI BAHT)")
m2.add_command(label="18.TURKEY:TRY(YTL)")
m2.add_command(label="19.UAE:AED(UAE DIRHAM)")
m2.add_command(label="20.UKRAINE:UAH(UKRANIAN HRYVNIA)")
m2.add_command(label="21.VEITNAM:VND(VEITNAMISE DONG)")
m2.add_command(label="22.BRAZIL:BRL(BRAZILLIAN REAL)")
m2.add_command(label="23.SOUTH KOREA:KRW(WON)")
m2.add_command(label="24.MALDIVES:MVR(RUFIYA)")
m2.add_command(label="25.NEPAL:NPR(NEPALESE RUPEES)")
m2.add_command(label="26.NEW ZEALAND:NZD(NEW ZEALAND DOLLAR)")
m2.add_command(label="27.PAKISTAN: PKR(PAKISTANI RUPEES)")
m2.add_command(label="28.QATAR:QAR(QATARI RIAL )")
m2.add_command(label="29.SAUDI ARABIA:SAR(SAUDI RIAL)")
m2.add_command(label="30.SINGAPUR:SGD(SINGAPURI DOLAR)")
m2.add_command(label="31.SOUTH AFRICA:ZAR(RAND)")
m2.add_command(label="32.SRILANKA:LKR(SRILANKAN RUPEE)")
windows.config(menu=menubar)
menubar.add_cascade(label="Country and Code",menu=m2)

#rating tab
windows.config(menu=menubar)
menubar.add_cascade(label="Rate us",command=rating)

#suggestion tab
windows.config(menu=menubar)
menubar.add_cascade(label="Feedback",command=feedback)

#History
windows.config(menu=menubar)
menubar.add_cascade(label="My History",command=History)
m3=Menu(menubar)
#about
m4=Menu(menubar)
m4.add_command(label="Created by:")
m4.add_command(label="Swapnil Patil")
m4.add_command(label="Baltej Singh")
m4.add_command(label="Prafull Bhoirkar")
m4.add_command(label="Rucha patil")
m4.add_command(label="Saurabh Gadhe")
windows.config(menu=menubar)
menubar.add_cascade(label="About",menu=m4)




windows.mainloop()