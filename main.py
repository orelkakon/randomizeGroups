from tkinter import *
from logic import generate_excel

root = Tk()
root.geometry("300x300")
root.title('Randomize Excel')
# title
var1 = StringVar()
label1 = Label(root, textvariable=var1, relief=RAISED, bd=4, bg='gold')
var1.set("WELCOME RANDOMIZE COLUMNS FOR EXCEL")
label1.pack()


def number_validation(S):
    if S in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    root.bell()  # .bell() plays that ding sound telling you there was invalid input
    return False


vcmd = (root.register(number_validation), '%S')

# Total sum
total_sum_label = Label(root, text="Total sum:")
total_sum_label.pack()
total_sum = Entry(root, bd=5, validate='key', vcmd=vcmd)
total_sum.pack()

# Columns number
columns_number_title = Label(root, text="Columns number:")
columns_number_title.pack()
columns_number = Entry(root, bd=5, validate='key', vcmd=vcmd)
columns_number.pack()

# Max number
max_number_title = Label(root, text="Max number:")
max_number_title.pack()
max_number = Entry(root, bd=5, validate='key', vcmd=vcmd)
max_number.pack()

# Min number
min_number_title = Label(root, text="Min number:")
min_number_title.pack()
min_number = Entry(root, bd=5, validate='key', vcmd=vcmd)
min_number.pack()

# generate button
GenerateButton = Button(root, text="generate file!", command=lambda: generate_excel(total_sum.get(), columns_number.get(), max_number.get(), min_number.get()), bg='gold')
GenerateButton.pack()

root.mainloop()
