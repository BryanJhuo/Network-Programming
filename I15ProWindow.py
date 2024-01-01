import IPhone15Pro
import tkinter

# phoneState : 0    colorState : 1    capacityState : 2    detailState : 3    pickupState : 4
class IP15Pro:
    def __int__(self):
        self.listState = None
        self.window = None
        return

    def createWindow(self):
        self.window = tkinter.Tk()
        self.window.title("Mini Apple Store : IPhone 15 Pro")
        self.window.geometry('510x500')
        self.window.resizable(width=False, height=False)
        self.listState = [tkinter.StringVar(self.window) for _ in range(5)]
        return

    def createRadioButton(self):
        colors = IPhone15Pro.getColor()
        capacity = IPhone15Pro.getCapacity()

        colorButtons = []
        capacityButtons = []
        phoneButton1 = tkinter.Radiobutton(self.window, text="IPhone 15 Pro", value="6.1-",
                                           variable=self.listState[0])
        phoneButton2 = tkinter.Radiobutton(self.window, text="IPhone 15 ProMax", value="6.7-",
                                           variable=self.listState[0])
        for i in range(4):  # colors
            colorButtons.append(tkinter.Radiobutton(self.window, text=""+colors[i], value=colors[i],
                                                    variable=self.listState[1]))
            colorButtons[i].place(x=200, y=85 + i*20)
            capacityButtons.append(tkinter.Radiobutton(self.window, text=""+capacity[i], value=capacity[i],
                                                       variable=self.listState[2]))
            capacityButtons[i].place(x=340, y=85 + i*20)

        phoneButton1.place(x=55, y=85)
        phoneButton1.select()
        phoneButton2.place(x=55, y=105)
        colorButtons[0].select()
        capacityButtons[0].select()
        return
    
    def createItemLabel(self):
        mainLabel = tkinter.Label(self.window, text="客製化你的IPhone 15 Pro", font=("標楷體", 15, "bold"), padx=5, pady=5, bg="pink", fg="black")
        sizeLabel = tkinter.Label(self.window, text="尺寸", font=("標楷體", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")
        colorLabel = tkinter.Label(self.window, text="顏色", font=("標楷體", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")
        capacityLabel = tkinter.Label(self.window, text="容量", font=("標楷體", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")

        mainLabel.place(x=125, y=5)
        sizeLabel.place(x=100, y=50)
        colorLabel.place(x=225, y=50)
        capacityLabel.place(x=350, y=50)
        return

    def updateResult(self):
        if self.listState[0].get() == "6.7-" and self.listState[2].get() == "128gb":
            self.listState[3].set("Error")
            self.listState[4].set("Error")
        else:
            myChoice = IPhone15Pro.getDetail(self.listState[0].get(), self.listState[2].get(), self.listState[1].get())
            self.listState[3].set(myChoice[0] + " " + myChoice[1])
            pickupData = IPhone15Pro.getPickUp(myChoice[2])
            if pickupData[0]:
                self.listState[4].set(pickupData[1] + " " + pickupData[2] + " " + pickupData[3])
            else:
                self.listState[4].set(pickupData[1])
        return

    def runWindow(self):
        print("Starting IPhone 15 Pro Series......")
        self.createWindow()
        self.createRadioButton()
        self.createItemLabel()
        result_Label = tkinter.Label(self.window, textvariable=self.listState[3], font=("標楷體", 16, "bold"), padx=5,
                                     pady=5, bg="white", fg="black")
        result_Label.place(x=0, y=235)

        pickup_Label = tkinter.Label(self.window, textvariable=self.listState[4], font=("標楷體", 16, "bold"), padx=5,
                                     pady=5, bg="pink", fg="black")
        pickup_Label.place(x=100, y=285)

        confirmButton = tkinter.Button(self.window, text="Confirm", font=('Arial', 16, 'bold'), command=self.updateResult)
        confirmButton.place(x=200, y=185)

        closeButton = tkinter.Button(self.window, text="Close", font=('Arial', 16, 'bold'), command=self.window.destroy)
        closeButton.place(x=210, y=340)

        self.window.mainloop()
        return

