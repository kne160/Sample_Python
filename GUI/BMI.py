'''
Sample Tk cal BMI add
'''

import tkinter as tk

root = tk.Tk()
root.title("BMI Calculate")

val = tk.StringVar()
val.set('身長と体重を入力')

frm = tk.Frame(root)
frm.configure(bg='white')
frm.pack(expand=False, fill=tk.X)

label1 = tk.Label(frm, textvariable=val)
label1.configure(bg='white')
label1.pack(expand=True, fill=tk.X, padx=10, pady=10)

frm2 = tk.Frame(frm)
frm2.configure(bg='white')
frm2.pack(expand=True, fill=tk.BOTH)

label2 = tk.Label(frm2, text="身長")
label2.configure(bg='white')
label2.grid(row=0, column=0)

entry1 = tk.Engry(frm2)
entry1.grid(row=0, column=1)

label3 = tk.Label(frm2, text="体重")
label3.configure(bg='white')
label3.grid(row=1, column=0)

entry2 = tk.Entry(frm2)
entry2.grid(row=1, column=1)

def doAction():
    height = float(entry1.get())
    weight = float(entry2.get())
    bmi = int(weight/(height/100)**2 * 100)/100
    cmt = '適正体重です'
    w = int((height/100)**2 * 22 * 10)/10
    if bmi < 18.5:
        cmt = '痩せすぎです'
    elif bmi < 25:
        cmt = '太り過ぎです'
    val.set(str(bmi) + cmt + '\r(適正:' + str(w) + 'Kg)')

button1 = tk.Button(frm, text='Calculate', command=doAction())
button1.configure(bg='white')
button1.pack(expand=True, fill=tk.X, padx=10, pady=10)

root.mainloop()

