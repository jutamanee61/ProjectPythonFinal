from tkinter import *
from forex_python.converter import CurrencyRates
def leftClickButton(event):
    labelResult.configure(text=int(textbox_americano.get())*50+(int(textbox_latte.get())*55)+(int(textbox_cappuccino.get())*50))
    if labelResult:
        labelCurrencyPay = Label(MainWindow,text="Currency for Pay:")
        labelCurrencyPay.grid(row=5, column=0)
        labelCurrencyPay = Label(MainWindow, text="1.EUR")
        labelCurrencyPay.grid(row=6, column=0)
        labelCurrencyPay = Label(MainWindow, text="2.JPY")
        labelCurrencyPay.grid(row=7, column=0)
        labelCurrencyPay = Label(MainWindow, text="3.THB")
        labelCurrencyPay.grid(row=8, column=0)
        c = CurrencyRates()
        result =c.get_rates('USD')
        print(result)
        # for key, value in result.items():
        #     print(key +":", round(value, 2))
        #     labelCurrencyRates = Label(MainWindow, key +":", round(value, 2))
        #     labelCurrencyRates.grid(row=6, column=0, padx=20, pady=20, sticky=W)
        #     labelCurrencyRates = Label(MainWindow, text=str(key) + ": " + str(value))
    else:
        print("So Sad !! T_T")
    print("Bye Bye")

MainWindow = Tk()
MainWindow.geometry('600x600')
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
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=4,column=0,padx=20,pady=20)

labelResult = Label(MainWindow,text="0.00")
labelResult.grid(row=4,column=1,padx=20,pady=20)

labelCurrency = Label(MainWindow,text="Bath")
labelCurrency.grid(row=4,column=2,padx=20,pady=20)

MainWindow.mainloop()

