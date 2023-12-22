# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter
import I15ProWindow
import I15Window

def createWindow():
    window = tkinter.Tk()
    window.title("Mini Apple Store")
    window.geometry('510x500')
    window.resizable(width=False, height=False)
    return window

def createChoiceButton():
    IP15Button = tkinter.Radiobutton(text="IPhone 15", value="IPhone 15", variable=ChoiceState)
    IP15ProButton = tkinter.Radiobutton(text="IPhone 15 Pro", value="IPhone 15 Pro", variable=ChoiceState)
    IMacButton = tkinter.Radiobutton(text="IMac", value="IMac", variable=ChoiceState)
    IP15Button.place(x=70, y=50)
    IP15Button.select()
    IP15ProButton.place(x=200, y=50)
    IMacButton.place(x=340, y=50)
    return

def runYourChoice():
    if ChoiceState.get() == "IPhone 15 Pro":
        myPurchase = I15ProWindow.IP15Pro()
        myPurchase.runWindow()

    if ChoiceState.get() == "IPhone 15":
        myPurchase = I15Window.IP15()
        myPurchase.runWindow()
    return

if __name__ == '__main__':
    print("Starting....")
    mainWindow = createWindow()
    title_Label = tkinter.Label(text="Choice Your IPhone", font=("Arial", 16, "bold"), padx=5, pady=5,
                                bg="Black", fg="white")
    title_Label.pack()

    ChoiceState = tkinter.StringVar()

    createChoiceButton()
    confirmButton = tkinter.Button(mainWindow, text="Confirm", font=('Arial', 16, 'bold'), command=runYourChoice)
    confirmButton.place(x=200, y=100)

    mainWindow.mainloop()


'''
    視窗選單
    menubar = tkinter.Menu(mainWindow)
    deviceMenu = tkinter.Menu(menubar)
    deviceMenu.add_command(label="IPhone15Pro")
    deviceMenu.add_command(label="IPhone15")
    deviceMenu.add_command(label="IMac")
    menubar.add_cascade(label="Device", menu=deviceMenu)
    mainWindow.config(menu=menubar)
'''
