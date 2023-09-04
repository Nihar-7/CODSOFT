from tkinter import *

# functions
List = []


def update():
    lb.delete(0, END)
    for i in List:
        lb.insert(END, i)


def add():
    value = input.get()
    if value == "":
        l["text"] = "Please Enter A Task !"

    else:
        l["text"] = ""
        List.append(value)
        input.set("")

    update()


def deleteAll():
    l["text"] = ""
    global List
    List = []
    update()


def deleteOne():
    l["text"] = ""
    val = lb.get("active")
    List.remove(val)
    update()


def ASC():
    l["text"] = ""
    List.sort()
    update()


def DESC():
    l["text"] = ""
    List.reverse()
    update()


def random():
    import random
    rand = random.choice(List)
    l["text"] = rand
    update()


def size():
    length = str(len(List))
    l["text"] = length


def edit():
    val = lb.get("active")
    deleteOne()
    inBox["textvariable"] = input.set(val)
    update()


root = Tk()
root.geometry("870x750")
root.title("To-Do-List")
root.wm_iconbitmap("to-do.ico")


root.configure(bg="#ff5722")
input = StringVar()
input.set("")

# label
l = Label(root, text="", border=6, bg="#ff5722",
          fg="#d3d6db", font="lucida 30 bold")
l.grid(row=0, column=0, padx=13, pady=13, columnspan=2)
# inputsc
inBox = Entry(root, textvariable=input, border=6,
              font="lucida 30 bold", bg="#d3d6db", fg="#2d4059", justify=CENTER)
inBox.grid(row=1, column=0, padx=13, pady=23)
# listbox
lb = Listbox(root, border=6, font="lucida 30 bold", bg="#d3d6db", fg="#2d4059")
lb.grid(row=2, column=0, rowspan=7)
# buttons
b1 = Button(root, text="Add Task", bg="#d3d6db", width=21, border=6,
            fg="#2d4059", font="lucida 20 bold", command=add, cursor="hand2")
b1.grid(row=1, column=1)

b2 = Button(root, text="Delete Task", bg="#d3d6db", width=21, border=6,
            fg="#2d4059", font="lucida 20 bold", command=deleteOne, cursor="hand2")
b2.grid(row=2, column=1)

b3 = Button(root, text="Delete All", bg="#d3d6db", width=21, border=6,
            fg="#2d4059", font="lucida 20 bold", command=deleteAll, cursor="hand2")
b3.grid(row=3, column=1)

b4 = Button(root, text="ASC", bg="#d3d6db", width=21, border=6,
            font="lucida 20 bold", fg="#2d4059", command=ASC, cursor="hand2")
b4.grid(row=4, column=1)

b5 = Button(root, text="DESC", bg="#d3d6db", width=21, border=6,
            font="lucida 20 bold", fg="#2d4059", command=DESC, cursor="hand2")
b5.grid(row=5, column=1)

b6 = Button(root, text="Lucky Task", bg="#d3d6db", width=21, border=6,
            fg="#2d4059", font="lucida 20 bold", command=random, cursor="hand2")
b6.grid(row=6, column=1)

b7 = Button(root, text="Total Tasks", bg="#d3d6db", width=21, border=6,
            fg="#2d4059", font="lucida 20 bold", command=size, cursor="hand2")
b7.grid(row=7, column=1)


b8 = Button(root, text="Edit Task", bg="#d3d6db", width=21, border=6,
            fg="#2d4059", font="lucida 20 bold", command=edit, cursor="hand2")
b8.grid(row=8, column=1)


root.mainloop()
