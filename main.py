from tkinter import *
def leftClickButton(event):
    labelResult.configure(text=int(textbox_americano.get())*50+(int(textbox_latte.get())*55)+(int(textbox_cappuccino.get())*50))

MainWindow = Tk()
MainWindow.geometry('600x600')
MainWindow.title('Coffee Shop')
MainWindow.option_add("*Font","consolas 14")

labelMenu = Label(MainWindow,text="เมนูเครื่องดื่ม")
labelMenu.grid(row=0,column=0,padx=20,pady=20)

label_latte = Label(MainWindow,text="1.ลาเต้ : 55฿")
label_latte.grid(row=1,column=0,padx=20,pady=20,sticky=W)

textbox_latte = Entry(MainWindow)
textbox_latte.grid(row=1,column=1,padx=20,pady=20)

label_americano = Label(MainWindow,text="2.อเมริกาโน่ : 40฿")
label_americano.grid(row=2,column=0,padx=20,pady=20,sticky=W)

textbox_americano = Entry(MainWindow)
textbox_americano.grid(row=2,column=1,padx=20,pady=20)

label_cappuccino = Label(MainWindow,text="3.คาปูชิโน่ : 50฿")
label_cappuccino.grid(row=3,column=0,padx=20,pady=20,sticky=W)

textbox_cappuccino = Entry(MainWindow)
textbox_cappuccino.grid(row=3,column=1,padx=20,pady=20)

calculateButton = Button(MainWindow,text="คำนวณราคา")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=4,column=0,padx=20,pady=20)

labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=4,column=1,padx=20,pady=20)

MainWindow.mainloop()

