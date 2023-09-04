from tkinter import *

# function

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if sc.get().isdigit():
            value = int(sc.get())
        else:
            try:
                value = eval(sc.get())
            except Exception as e:
                value = "Error"

        sc.set(value)
        entry.update()
    elif text == "C":
        sc.set("")
        entry.update()
    else:
        sc.set(sc.get()+text)
        entry.update()


root = Tk()
root.geometry("400x590")
root.title("Calculator")
root.wm_iconbitmap("cal.ico")
sc = StringVar()
sc.set("")
root.configure(background="#4b81ab")
# entry
entry = Entry(root, textvariable=sc, bg="#233142", fg="#d3d6db",
              border=6, font="lucida 30 bold", justify="right")
entry.pack(fill=X, padx=13, ipadx=13, pady=13)

# buttons
f = Frame(root, bg="#4b81ab")
b = Button(f, text="(", width=3, bg="#455d7a", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text=")", width=3, bg="#455d7a", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="%", width=3, bg="#455d7a", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="C", width=3, bg="#ff5722", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
f.pack(padx=13, pady=3)


f = Frame(root, bg="#4b81ab")
b = Button(f, text="7", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="8", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="9", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="/", width=3, bg="#ff5722", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
f.pack(padx=13, pady=3)


f = Frame(root, bg="#4b81ab")
b = Button(f, text="4", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="5", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="6", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="*", width=3, bg="#ff5722", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
f.pack(padx=13, pady=3)


f = Frame(root, bg="#4b81ab")
b = Button(f, text="1", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="2", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="3", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="-", width=3, bg="#ff5722", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
f.pack(padx=13, pady=3)


f = Frame(root, bg="#4b81ab")
b = Button(f, text="0", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text=".", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="=", width=3, bg="#233142", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
b = Button(f, text="+", width=3, bg="#ff5722", pady=2, border=6,
           fg="#d3d6db", font="lucida 30 bold", cursor="hand2")
b.pack(side=LEFT, padx=2)
b.bind("<Button-1>", click)
f.pack(padx=13, pady=3)


root.mainloop()
