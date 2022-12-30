from tkinter import *


class Window(Tk):
    def __init__(self, size, title, mode):
        super().__init__()
        self.geometry(size)
        self.title(title)
        self.bgColor = mode
        self.config(background=mode)
        self.attributes('-alpha', 0.8)

    def createScreen(self):
        self.screenValue = StringVar()
        self.screenValue.set("")
        self.screen = Entry(self, textvariable=self.screenValue,
                            font="lucida 50 bold", justify=RIGHT, state=DISABLED)
        self.screen.pack(fill=X, padx=10, pady=10)

    def createFrame(self):
        f = Frame(self, background=self.bgColor)
        return f

    def calculate(self, event):
        exp = event.widget.cget("text").strip()
        if exp == 'C':
            self.screenValue.set("")
        elif exp == '=':
            try:
                self.screenValue.set(eval(self.screenValue.get()))
            except Exception as e:
                self.screenValue.set("ERROR")
        else:
            self.screenValue.set(self.screenValue.get()+exp)
        self.screen.update()

    def createButton(self, frame, buttonValue):
        b = Button(frame, text=buttonValue, font="lucida 40 bold",
                   bg=self.bgColor, fg="white")
        b.pack(side=LEFT, padx=20, pady=10)
        b.bind('<Button-1>', self.calculate)


if __name__ == '__main__':
    calculator = Window("475x710", "Calculator by Ritwick", "black")
    calculator.maxsize(width=475,height=710)
    calculator.minsize(width=475,height=710)
    calculator.createScreen()
    f = calculator.createFrame()
    for i in range(1, 4):
        calculator.createButton(f, f"{i}")
    calculator.createButton(f, "C")
    f.pack()

    f = calculator.createFrame()
    for i in range(4, 7):
        calculator.createButton(f, f"{i}")
    calculator.createButton(f, "+")
    f.pack()

    f = calculator.createFrame()
    for i in range(7, 10):
        calculator.createButton(f, f"{i}")
    calculator.createButton(f, " *")
    f.pack()

    f = calculator.createFrame()
    calculator.createButton(f, "0")
    calculator.createButton(f, " .")
    calculator.createButton(f, " /")
    calculator.createButton(f, " -")

    f.pack()

    f = calculator.createFrame()
    b = Button(f, text="=", font="lucida 40 bold",
               bg="black", fg="white", width="13")
    b.pack(side=LEFT, padx=20, pady=10, fill=X)
    b.bind('<Button-1>', calculator.calculate)

    f.pack()

    calculator.mainloop()
