import tkinter
def ConvertToC():
    Far = float(TextBox1.get())
    Cel = (Far - 32) * 5/9
    TextBox2.delete(0, END)
    TextBox2.insert(0, Cel)
def ConvertToF():
    Cel = float(TextBox1.get())
    Far = (9/5 * Cel) + 32
    TextBox2.delete(0, END)
    TextBox2.insert(0, Far)
MainWindow=Tk()
MainWindow.title("GUITempConverter")
MainWindow.geometry("300x150")
Label1 = Label(MainWindow, text="Δώσε θερμοκρασία: ")
Label1.pack()
TextBox1 = Entry(MainWindow)
TextBox1.pack()
Button1 = Button(MainWindow, text="Μετατροπή σε Κελσίου", command=ConvertToC)
Button1.pack()
Button2 = Button(MainWindow, text="Μετατροπή σε Φαρενάιτ", command=ConvertToF)
Button2.pack()
TextBox2 = Entry(MainWindow)
TextBox2.pack()
MainWindow.mainloop()
