# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

import apple
import tkinter

def createWindow():
    window = tkinter.Tk()
    window.title("Mini Apple Store")
    window.geometry('510x500')
    window.resizable(width=False, height=False)
    return window

def createRadioButton(phoneState, colorState, capacityState):
    colors = apple.getColor()
    capacity = apple.getCapacity()
    phoneButton1 = tkinter.Radiobutton(text="IPhone 15 Pro", value="6.1-", variable=phoneState)
    phoneButton2 = tkinter.Radiobutton(text="IPhone 15 ProMax", value="6.7-", variable=phoneState)
    colorButton1 = tkinter.Radiobutton(text=""+colors[0], value=colors[0], variable=colorState)
    colorButton2 = tkinter.Radiobutton(text=""+colors[1], value=colors[1], variable=colorState)
    colorButton3 = tkinter.Radiobutton(text=""+colors[2], value=colors[2], variable=colorState)
    colorButton4 = tkinter.Radiobutton(text=""+colors[3], value=colors[3], variable=colorState)
    capacityButton1 = tkinter.Radiobutton(text=""+capacity[0], value=capacity[0], variable=capacityState)
    capacityButton2 = tkinter.Radiobutton(text=""+capacity[1], value=capacity[1], variable=capacityState)
    capacityButton3 = tkinter.Radiobutton(text=""+capacity[2], value=capacity[2], variable=capacityState)
    capacityButton4 = tkinter.Radiobutton(text=""+capacity[3], value=capacity[3], variable=capacityState)
    phoneButton1.place(x=55, y=50)
    phoneButton1.select()
    phoneButton2.place(x=55, y=70)
    colorButton1.place(x=200, y=50)
    colorButton1.select()
    colorButton2.place(x=200, y=70)
    colorButton3.place(x=200, y=90)
    colorButton4.place(x=200, y=110)
    capacityButton1.place(x=300, y=50)
    capacityButton1.select()
    capacityButton2.place(x=300, y=70)
    capacityButton3.place(x=300, y=90)
    capacityButton4.place(x=300, y=110)
    return

def updateResult():
    if phoneState.get() == "6.7-" and capacityState.get() == "128gb":
        detailState.set("Error")
    else:
        myChoice = apple.getDetail(phoneState.get(), capacityState.get(), colorState.get())
        detailState.set(myChoice[0] + " " + myChoice[1])

if __name__ == '__main__':
    print("Starting....")
    mainWindow = createWindow()
    title_Label = tkinter.Label(text="Choice Your IPhone", font=("Arial", 16, "bold"), padx=5, pady=5,
                                bg="Black", fg="white")
    title_Label.pack()

    phoneState = tkinter.StringVar()
    colorState = tkinter.StringVar()
    capacityState = tkinter.StringVar()
    detailState = tkinter.StringVar()
    createRadioButton(phoneState, colorState, capacityState)
    result_Label = tkinter.Label(textvariable=detailState, font=("Arial", 16, "bold"), padx=5,
                                 pady=5, bg="white", fg="black")
    result_Label.place(x=0, y=200)

    confirmButton = tkinter.Button(text="Confirm", font=('Arial', 16, 'bold'), command=updateResult)
    confirmButton.place(x=200, y=150)

    mainWindow.mainloop()

