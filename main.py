from tkinter import *
from forex_python.bitcoin import BtcConverter
def selectCurrencyButton(currency,total):
    if currency == "2":
        b = BtcConverter()
        print(b.convert_to_btc(total, 'THB'))
        convert = b.convert_to_btc(total, 'THB')
        reult_convert.config(text=str(convert))
    else:
        reult_convert.config(text=str(total))

def TotalPrice(event):
    labelResult.configure(text=int(textbox_americano.get())*50+(int(textbox_latte.get())*55)+(int(textbox_cappuccino.get())*50))
    cappuccino = float(textbox_cappuccino.get())*50
    latte = float(textbox_latte.get())*55
    americano = float(textbox_americano.get())*40
    total = cappuccino + latte + americano

    if labelResult:
        label_currency_thai_baht = Label(MainWindow, text="Currencies for pay:")
        label_currency_thai_baht.grid(row=5, column=0,padx=20,sticky=W)

        label_currency_thai_baht = Label(MainWindow, text="1.Thai Baht")
        label_currency_thai_baht.grid(row=6, column=0,padx=20, sticky=W)

        label_currency_bitcoins = Label(MainWindow, text="2.Bit Coins")
        label_currency_bitcoins.grid(row=7, column=0, padx=20, sticky=W)

        label_currency = Label(MainWindow, text="Enter Curency:")
        label_currency.grid(row=8, column=0, padx=20, pady=20)

        textbox_currency = Entry(MainWindow)
        textbox_currency.insert(0, "")
        textbox_currency.grid(row=9, column=1, padx=20)
        enterButton = Button(MainWindow, text="Confirm")
        enterButton.bind('<Button-1>', lambda event: selectCurrencyButton(textbox_currency.get(),total))
        enterButton.grid(row=9, column=2, padx=20, pady=20)

MainWindow = Tk()
MainWindow.geometry('800x800')
MainWindow.title('Coffee Shop')

MainWindow.option_add("*Font","consolas 14")

labelMenu = Label(MainWindow,text="Drink Menu")
labelMenu.grid(row=0,column=0,padx=20,pady=20,sticky=W)

label_latte = Label(MainWindow,text="1.Latte : 55฿")
label_latte.grid(row=1,column=0,padx=20,pady=20,sticky=W)

textbox_latte = Entry(MainWindow)
textbox_latte.insert(0, "0")
textbox_latte.grid(row=1,column=1,padx=20,pady=20)

label_americano = Label(MainWindow,text="2.Americano : 40฿")
label_americano.grid(row=2,column=0,padx=20,pady=20,sticky=W)

textbox_americano = Entry(MainWindow)
textbox_americano.insert(0, "0")
textbox_americano.grid(row=2,column=1,padx=20,pady=20)

label_cappuccino = Label(MainWindow,text="3.Cappuccin : 50฿")
label_cappuccino.grid(row=3,column=0,padx=20,pady=20,sticky=W)

textbox_cappuccino = Entry(MainWindow)
textbox_cappuccino.insert(0, "0")
textbox_cappuccino.grid(row=3,column=1,padx=20,pady=20)

calculateButton = Button(MainWindow,text="Total Price")
calculateButton.bind('<Button-1>',TotalPrice)
calculateButton.grid(row=4,column=0,padx=20,pady=20)

labelResult = Label(MainWindow,text="0.00")
labelResult.grid(row=4,column=1,padx=20,pady=20)

labelCurrency = Label(MainWindow,text="Baht")
labelCurrency.grid(row=4,column=2,padx=20,pady=20)

reult_convert = Label(MainWindow, text="")
reult_convert.grid(row=10,column=1,padx=20,pady=20)

MainWindow.mainloop()

