# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter
from tkinter import ttk
import I15ProWindow
import I15Window
import MacProWindow

def createWindow():
    window = tkinter.Tk()
    window.title("Mini Apple Store")
    window.geometry('510x300')
    window.resizable(width=False, height=False)
    return window

def createChoiceButton():
    IP15Button = tkinter.Radiobutton(text="IPhone 15", value="IPhone 15", variable=ChoiceState)
    IP15ProButton = tkinter.Radiobutton(text="IPhone 15 Pro", value="IPhone 15 Pro", variable=ChoiceState)
    IMacButton = tkinter.Radiobutton(text="Mac Pro", value="Mac Pro", variable=ChoiceState)
    IP15Button.place(x=70, y=50)
    IP15Button.select()
    IP15ProButton.place(x=200, y=50)
    IMacButton.place(x=340, y=50)
    return

def runRadioYourChoice():
    if ChoiceState.get() == "IPhone 15":
        myPurchase = I15Window.IP15()
        myPurchase.runWindow()

    if ChoiceState.get() == "IPhone 15 Pro":
        myPurchase = I15ProWindow.IP15Pro()
        myPurchase.runWindow()

    if ChoiceState.get() == "Mac Pro":
        myPurchase = MacProWindow.Mac_Pro()
        myPurchase.runWindow()

    return

def runComboboxYourChoice():
    if box.get() == "IPhone 15 Pro":
        myPurchase = I15ProWindow.IP15Pro()
        myPurchase.runWindow()

    if box.get() == "IPhone 15":
        myPurchase = I15Window.IP15()
        myPurchase.runWindow()

    if box.get() == "Mac Pro":
        myPurchase = MacProWindow.Mac_Pro()
        myPurchase.runWindow()

    return

if __name__ == '__main__':
    print("Starting....")
    mainWindow = createWindow()
    title_Label = tkinter.Label(text="選擇你想要購買的產品", font=("標楷體", 16, "bold"), padx=5, pady=5,
                                bg="Black", fg="white")
    title_Label.pack()

    ChoiceState = tkinter.StringVar()

    createChoiceButton()
    radioConfirmButton = tkinter.Button(mainWindow, text="Confirm", font=('Arial', 16, 'bold'), command=runRadioYourChoice)
    radioConfirmButton.place(x=200, y=100)

    comboboxConfirmButton = tkinter.Button(mainWindow, text="Confirm", font=('Arial', 16, 'bold'), command=runComboboxYourChoice)
    comboboxConfirmButton.place(x=200, y=200)

    box = ttk.Combobox(mainWindow, values=["IPhone 15", "IPhone 15 Pro", "Mac Pro"])
    box.place(x=170, y=170)

    closeButton = tkinter.Button(mainWindow, text="Close", font=('Arial', 16, 'bold'), command=mainWindow.destroy)
    closeButton.place(x=210, y=250)

    mainWindow.mainloop()
