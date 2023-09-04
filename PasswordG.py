from tkinter import *

# function
def check():
    global length
    l3["text"] = ""

    value = ""

    if (length.get() == ""):
        value = "please enter length"
    else:
        n = int(length.get())
        import random
        if strength.get() == 1:
            for i in range(n):
                value = value + \
                    random.choice(
                        "QAZWSXEDCRFVTGBYHNUJMIKOLP1234567890qazwsxedcrfvtgbyhnujmikolp,./;'[]!@#$%^&*()_+{?}\|<>")
        elif strength.get() == 2:
            for i in range(n):
                value = value + \
                    random.choice(
                        "QAZWSXEDCRFVTGBYHNUJMIKOLPazqwsxedcrfvtgbyhnujmikolp1234567890")
        elif (strength.get() == 3):
            for i in range(n):
                value = value + \
                    random.choice("qazwsxedcrfvtgbyhnujmiklop1234567890")
        else:
            value = "please select strength"
    l3["text"] = value


root = Tk()
root.geometry("420x600")
root.title("Password_Generator")
root.wm_iconbitmap("pass.ico")

root.configure(bg="#61c0bf")

# label
l1 = Label(root, text="Generate Password", bg="#61c0bf",
           fg="#36626a", font="lucida 30 bold")
l1.grid(row=0, column=0, columnspan=2, padx=13, pady=13, ipadx=7)

# text
l2 = Label(root, text="Enter Length", bg="#61c0bf",
           fg="#36626a", font="lucida 24 bold")
l2.grid(row=1, column=0, padx=13, pady=13, ipadx=7)

# input length
length = StringVar()

input = Entry(root, textvariable=length, bg="#bbded6", fg="#36626a",
              font="lucida 30 bold", width=2, border=6, justify=CENTER)
input.grid(row=1, column=1, padx=13, pady=12, ipadx=7)

# input strength
strength = IntVar()


r1 = Radiobutton(root, text="Strong", bg="#61c0bf", value=1, fg="#36626a", variable=strength,
                 font="lucida 20 bold", indicatoron=17).grid(row=2, column=0, columnspan=2, pady=4, ipadx=7)

r2 = Radiobutton(root, text="medium", bg="#61c0bf", value=2, fg="#36626a", variable=strength,
                 font="lucida 20 bold").grid(row=3, column=0, columnspan=2, pady=4, ipadx=7)

r3 = Radiobutton(root, text="weak", bg="#61c0bf", value=3, fg="#36626a", variable=strength,
                 font="lucida 20 bold").grid(row=4, column=0, columnspan=2, pady=4, ipadx=7)


b = Button(root, text="Generate", border=6, bg="#bbded6", fg="#36626a",
           command=check, font="lucida 20 bold", cursor="hand2")
b.grid(row=5, column=0, pady=13, columnspan=2, rowspan=2)

l3 = Label(root, text="", font="lucida 20 bold",
           bg="#bbded6", fg="#36626a", width=20, border=5)
l3.grid(row=7, column=0, columnspan=2, padx=13, pady=23, ipadx=7)

root.mainloop()
