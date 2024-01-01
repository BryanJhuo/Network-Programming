import MacPro
import tkinter

core = {"24核心CPU 60核心GPU": "065-CDJD", "24核心CPU 72核心GPU": "065-CDJF"}
memory = {"64GB": "065-CDJG", "128GB": "065-CDJH", "192GB": "065-CDJJ"}
ssd = {"1TB": "065-CDJK", "2TB": "065-CDJL", "4TB": "065-CDJM", "8TB": "065-CDJN"}
case = {"不鏽鋼框架配備腳座": "065-CDJ7", "不鏽鋼框架配備滾輪": "065-CDJ8"}
mouse = {"巧控滑鼠": "TA065-CDKC", "巧控板": "TA065-CDKD", "巧控滑鼠+巧控板": "TA065-CDKF"}
finalCut = {"No": "065-CDKM", "Yes": "065-CDKN"}
logicPro = {"No": "065-CDKP", "Yes": "065-CDKQ"}

class Mac_Pro:
    def __init__(self):
        self.listState = None
        self.window = None
        self.resultState = None
        return

    def createWindow(self):
        self.window = tkinter.Tk()
        self.window.title("Mini Apple Store : IMac")
        self.window.geometry('510x510')
        self.window.resizable(width=False, height=False)
        self.listState = [tkinter.StringVar(self.window) for _ in range(7)]
        self.resultState = [tkinter.StringVar(self.window) for _ in range(2)]
        return

    def createRadioButton(self):
        coreButtons = []
        memoryButtons = []
        ssdButtons = []
        caseButtons = []
        mouseButtons = []
        finalCutButtons = []
        logicProButtons = []

        for i in enumerate(core.items()):
            index = int(i[0])
            coreButtons.append(tkinter.Radiobutton(self.window, text=i[1][0], value=i[1][1], variable=self.listState[0]))
            coreButtons[index].place(x=10, y=85 + index * 20)

        for i in enumerate(memory.items()):
            index = int(i[0])
            memoryButtons.append(
                tkinter.Radiobutton(self.window, text=i[1][0], value=i[1][1], variable=self.listState[1]))
            memoryButtons[index].place(x=170, y=85 + index * 20)

        for i in enumerate(ssd.items()):
            index = int(i[0])
            ssdButtons.append(tkinter.Radiobutton(self.window, text=i[1][0], value=i[1][1], variable=self.listState[2]))
            ssdButtons[index].place(x=270, y=85 + index * 20)

        for i in enumerate(case.items()):
            index = int(i[0])
            caseButtons.append(
                tkinter.Radiobutton(self.window, text=i[1][0], value=i[1][1], variable=self.listState[3]))
            caseButtons[index].place(x=340, y=85 + index * 20)

        for i in enumerate(mouse.items()):
            index = int(i[0])
            mouseButtons.append(
                tkinter.Radiobutton(self.window, text=i[1][0], value=i[1][1], variable=self.listState[4]))
            mouseButtons[index].place(x=50, y=230 + index * 20)

        for i in enumerate(finalCut.items()):
            index = int(i[0])
            finalCutButtons.append(
                tkinter.Radiobutton(self.window, text=i[1][0], value=i[1][1], variable=self.listState[5]))
            finalCutButtons[index].place(x=230, y=230 + index * 20)

        for i in enumerate(logicPro.items()):
            index = int(i[0])
            logicProButtons.append(
                tkinter.Radiobutton(self.window, text=i[1][0], value=i[1][1], variable=self.listState[6]))
            logicProButtons[index].place(x=340, y=230 + index * 20)

        coreButtons[0].select()
        memoryButtons[0].select()
        ssdButtons[0].select()
        caseButtons[0].select()
        mouseButtons[0].select()
        finalCutButtons[0].select()
        logicProButtons[0].select()
        return

    def updateResult(self):
        state = [self.listState[i].get() for i in range(len(self.listState))]
        price = MacPro.getPrice(state)
        pickDate = MacPro.getDetail(state)
        self.resultState[0].set("總金額: "+price)
        self.resultState[1].set(pickDate[0] + " " + pickDate[1])
        return

    def createItemLabel(self):
        mainLabel = tkinter.Label(self.window, text="客製化你的Mac Pro", font=("標楷體", 15, "bold"), padx=5, pady=5, bg="pink", fg="black")
        coreLabel = tkinter.Label(self.window, text="Core", font=("Arial", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")
        memoryLabel = tkinter.Label(self.window, text="Memory", font=("Arial", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")
        ssdLabel = tkinter.Label(self.window, text="SSD", font=("Arial", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")
        caseLabel = tkinter.Label(self.window, text="Case", font=("Arial", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")
        mouseLabel = tkinter.Label(self.window, text="巧控滑鼠或巧控板", font=("標楷體", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")
        finalCutLabel = tkinter.Label(self.window, text="Final Cut", font=("Arial", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")
        logicProLabel = tkinter.Label(self.window, text="Logic Pro", font=("Arial", 12, "bold"), padx=5, pady=5, bg="yellow", fg="black")

        mainLabel.place(x=150, y=5)
        coreLabel.place(x=70, y=50)
        memoryLabel.place(x=170, y=50)
        ssdLabel.place(x=270, y=50)
        caseLabel.place(x=380, y=50)
        mouseLabel.place(x=40, y=200)
        finalCutLabel.place(x=220, y=200)
        logicProLabel.place(x=330, y=200)
        return


    def runWindow(self):
        print("Starting Mac Pro .......")
        self.createWindow()
        self.createRadioButton()
        self.createItemLabel()

        confirmButton = tkinter.Button(self.window, text="Confirm", font=('Arial', 16, 'bold'), command=self.updateResult)
        confirmButton.place(x=200, y=300)
        priceLabel = tkinter.Label(self.window, textvariable=self.resultState[0], font=("標楷體", 16, "bold"), padx=5, pady=5, bg="white", fg="black")
        pickupLabel = tkinter.Label(self.window, textvariable=self.resultState[1], font=("標楷體", 16, "bold"), padx=5, pady=5, bg="pink", fg="black")
        priceLabel.place(x=110, y=360)
        pickupLabel.place(x=110, y=410)

        closeButton = tkinter.Button(self.window, text="Close", font=('Arial', 16, 'bold'), command=self.window.destroy)
        closeButton.place(x=210, y=455)

        self.window.mainloop()
        return
