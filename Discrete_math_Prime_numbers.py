from tkinter import *                   # tkinter so user interface can be used

ptest = 0                               # global variable
pgenr = 0
root = Tk()
root.title("Prime numbers")
root.resizable(False,False)
# root.config(background="blue")



# def showExpenseList():  # show expense list on the right side
#     listbox = Listbox(expenseListFr)
#     for i in range(0, 10):
#         listbox.insert(ptest)
#
#     listbox.grid(row=1, column=0)
def showTextBox():
    textBox = Text(expenseListFr, heigh=35, width=50)
    textBox.insert(END, "===================== RESULT =====================\n")
    textBox.grid(row=1, column=0)
    return textBox


def addText(number, time, info):
    # calculation

    textBox.insert(END, "Number: "+str(number)+"\n")
    textBox.insert(END, "Time: "+str(time)+"\n")
    textBox.insert(END, "Info: "+str(info)+"\n")


def ptestBtnClick():  # event function for ptest

    global ptest
    global items
    if ptestTxt.get() == '':
        ptest = ptest
    else:
        ptest = int(ptestTxt.get())

    addText(ptest, 5.3, True)
    nowptestValLB = Label(infoFr, text=ptest, width=30)
    nowptestValLB.grid(row=0, column=1)


def pgenrBtnClick():  # event function for ptest
    global pgenr
    if pgenrTxt.get() == '':
        pgenr = pgenr
    else:
        pgenr = int(pgenrTxt.get())
    nowpgenrValLb = Label(infoFr, text=pgenr, width=30)
    nowpgenrValLb.grid(row=0, column=3)


rowCnt = 0
rowCnt += 1
infoFr = Frame(root)
infoFr.grid(row=rowCnt, column=0, columnspan=3)

nowptestLB = Label(infoFr, text="P test num: ")  # print ptest
nowptestLB.grid(row=0, column=0)
nowptestValLB = Label(infoFr, text=ptest, width=30)
nowptestValLB.grid(row=0, column=1)

nowpgenrLB = Label(infoFr, text="P genr num: ")  # print expense
nowpgenrLB.grid(row=0, column=2)
nowpgenrValLB = Label(infoFr, text=pgenr, width=30)
nowpgenrValLB.grid(row=0, column=3)

# for ptest input
rowCnt += 1
ptestLB = Label(root, text="P test")
ptestLB.grid(row=rowCnt, column=0)
ptestTxt = Entry(root, width=75)
ptestTxt.grid(row=rowCnt, column=1)
ptestBtn = Button(root, text="OK", width=5, command=ptestBtnClick)
ptestBtn.grid(row=rowCnt, column=2)

# for adding an item about expenditure
rowCnt += 1
lb2 = Label(root, text="")
lb2.grid(row=rowCnt)

rowCnt += 1
pgenrLB = Label(root, text="P genr")
pgenrLB.grid(row=rowCnt, column=0)
pgenrTxt = Entry(root, width=75,  exportselection=0)
pgenrTxt.grid(row=rowCnt, column=1)
pgenrBtn = Button(root, text="OK", width=5, command=pgenrBtnClick)
pgenrBtn.grid(row=rowCnt, column=2)

rowCnt = 1
expenseListFr = Frame(root)
expenseListFr.grid(row=rowCnt, rowspan=6, column=5, columnspan=2)

lb3 = Label(expenseListFr, text="The result", justify=LEFT)
lb3.grid(row=0, column=0)

# showExpenseList()
textBox = showTextBox()
root.mainloop()
