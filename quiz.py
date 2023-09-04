from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x800")
root.title("QUIZ")
root.wm_iconbitmap("quiz.ico")

# function

def getWidgets():
    global questions, v, correct
    l1 = Label(text=questions[0], border=20, fg="blue",
               font="lucida 18 bold", cursor="hand2")
    l2 = Label(text="", border=20, fg="blue", font="lucida 40 bold")
    r1 = Radiobutton(canvas, border=20, text="", value=1, variable=v,
                     fg="blue", font="lucida 18 bold", cursor="hand2")
    r2 = Radiobutton(canvas, border=20, text="", value=2, fg="blue",
                     variable=v, font="lucida 18 bold", cursor="hand2")
    r3 = Radiobutton(canvas, border=20, text="", value=3, fg="blue",
                     variable=v, font="lucida 18 bold", cursor="hand2")
    r4 = Radiobutton(canvas, border=20, text="", value=4, fg="blue",
                     variable=v, font="lucida 18 bold", cursor="hand2")
    quitBtn = Button(root, bg="#eaeaea", cursor="hand2", fg="#0c005a",
                     text="END", border=20, font="poppins 15 bold", command=quit)

    return l1, l2, r1, r2, r3, r4, quitBtn


def startQuiz(l1, l2, r1, r2, r3, r4, quitBtn):
    quitBtn.destroy()
    global index, correct
    canvas.delete('all')
    canvas.create_image(0, 0, anchor='nw', image=photo1)
    canvas.image = photo1

    canvas2.delete('all')
    l2.destroy()
    startBtn['text'] = "START"
    index = 0
    correct = 0
    l1, l2, r1, r2, r3, r4, quitBtn = getWidgets()
    startBtn['command'] = lambda: getBody(l1, l2, r1, r2, r3, r4, quitBtn)


def showResult(correct, l1, l2, r1, r2, r3, r4, quitBtn):

    l1.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    canvas.delete('all')
    img3 = Image.open("./quizGameImg/endquiz.jpg")
    img3 = img3.resize((800, 800))
    photo3 = ImageTk.PhotoImage(img3)
    canvas.create_image(0, 0, anchor='nw', image=photo3)
    canvas.image = photo3

    quitBtn.place(x=310, y=60, height=70, width=200)
    canvas2.delete('all')
    startBtn['text'] = "PLAY AGAIN"
    startBtn['command'] = lambda: startQuiz(l1, l2, r1, r2, r3, r4, quitBtn)
    l2['text'] = str(correct)+"/"+"4"
    l2.place(x=270, y=330, width=260, height=150)


def disableButton(state, l1, l2, r1, r2, r3, r4, quitBtn):
    r1['state'] = state
    r2['state'] = state
    r3['state'] = state
    r4['state'] = state


def check(l1, l2, r1, r2, r3, r4, quitBtn):
    global correct, options, questions, v, correctOpt, index
    if (v.get()-1 == correctOpt[index]):
        correct = correct+1

    index = index+1
    disableButton('disable', l1, l2, r1, r2, r3, r4, quitBtn)
    v.set(0)
    getOptions(l1, l2, r1, r2, r3, r4, quitBtn)


def getOptions(l1, l2, r1, r2, r3, r4, quitBtn):

    global correct, options, questions, v, correctOpt, index
    if (index < len(questions)):
        disableButton('normal', l1, l2, r1, r2, r3, r4, quitBtn)
        l1['text'] = questions[index]
        r1['text'] = options[index][0]
        r2['text'] = options[index][1]
        r3['text'] = options[index][2]
        r4['text'] = options[index][3]

    else:

        showResult(correct, l1, l2, r1, r2, r3, r4, quitBtn)


def getBody(l1, l2, r1, r2, r3, r4, quitBtn):

    canvas.delete('all')
    img2 = Image.open("./quizGameImg/quizbody.jpeg")
    img2 = img2.resize((800, 800))
    photo2 = ImageTk.PhotoImage(img2)
    canvas.create_image(0, 0, anchor='nw', image=photo2)
    canvas.image = photo2

    canvas2.delete('all')
    startBtn['text'] = "NEXT"
    startBtn['command'] = lambda: check(l1, l2, r1, r2, r3, r4, quitBtn)
    if (index == 0):
        display(l1, l2, r1, r2, r3, r4, quitBtn)


def display(l1, l2, r1, r2, r3, r4, quitBtn):
    global questions, options, index, correct

    l1['text'] = questions[index]
    r1['text'] = options[index][0]
    r2['text'] = options[index][1]
    r3['text'] = options[index][2]
    r4['text'] = options[index][3]

    l1.place(x=130, y=233, height=80, width=548)
    r1.place(x=130, y=438, height=50, width=210)
    r2.place(x=485, y=438, height=50, width=210)
    r3.place(x=130, y=560, height=50, width=210)
    r4.place(x=485, y=560, height=50, width=210)


# canvas1
canvas = Canvas(root, bg="yellow")
canvas.place(x=0, y=0, height=800, width=800)

# bgimg
img1 = Image.open(fp="./quizGameImg/startquiz.jpg")
img1 = img1.resize((800, 800))
photo1 = ImageTk.PhotoImage(img1)
canvas.create_image(0, 0, anchor='nw', image=photo1)


# canvas2
canvas2 = Canvas(root)
canvas2.place(x=310, y=660, height=70, width=200)
# start button
startBtn = Button(root, bg="#eaeaea", cursor="hand2", fg="#0c005a", text="START", border=20,
                  font="poppins 15 bold", command=lambda: getBody(l1, l2, r1, r2, r3, r4, quitBtn))
startBtn.place(x=310, y=660, height=70, width=200)
# quit
quitBtn = Button(root, bg="#eaeaea", cursor="hand2", fg="#0c005a",
                 text="END", border=20, font="poppins 15 bold", command=quit)


# ques and options
correct = IntVar()
correct = 0
questions = ["What function creates your main window?", "What function is used to define an entry box?",
             "What function is used to create a label?", "print type(type(int))"]
options = [["Tkinter()", "Tk()", "main()", "label()"], ["tk.entry()", "tk.Entry()", "ttk.Entry()", "tkk.entry()"], [
    "ttk.Label()", "tk.label()", "tk.Label()", "tkk.label()"], ["type 'int'", "Error", "type 'type'", "0"]]
correctOpt = [1, 2, 0, 2]
v = IntVar()

index = IntVar()
index = 0

l1 = Label(text=questions[0], fg="blue", border=20,
           font="lucida 18 bold", cursor="hand2")


r1 = Radiobutton(canvas, border=20, text="", value=1, variable=v,
                 fg="blue", font="lucida 18 bold", cursor="hand2")


r2 = Radiobutton(canvas, border=20, text="", value=2, fg="blue",
                 variable=v, font="lucida 18 bold", cursor="hand2")


r3 = Radiobutton(canvas, border=20, text="", value=3, fg="blue",
                 variable=v, font="lucida 18 bold", cursor="hand2")


r4 = Radiobutton(canvas, border=20, text="", value=4, fg="blue",
                 variable=v, font="lucida 18 bold", cursor="hand2")

# label result

l2 = Label(text="", border=20, fg="blue", font="lucida 40 bold")


root.mainloop()
