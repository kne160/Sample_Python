
'''
GUI Tk Sample
'''

import tkinter as tk

# Tkの作成
root = tk.Tk()
root.title("Tkinter sample")

# StringVarの作成
val = tk.StringVar()
val.set('Type integer:')

# Frameの作成
frm = tk.Frame(root)
frm.configure(bg='white')
frm.pack(expand=False, fill=tk.X)

# Labelの作成
label1 = tk.Label(frm, textvariable=val)
label1.configure(bg = 'white')
label1.pack(expand=True, fill=tk.X, padx=10, pady=10)

# Entryの作成
entry1 = tk.Entry(frm)
entry1.pack(expand=True, fill=tk.X, padx=10, pady=10)

# Buttonのcommand用関数
def doAction():
    n = int(entry1.get())
    total = 0
    for i in range(n + 1):
        total += i
    val.set('Total: ' + str(total))

# Buttonの作成
btn1 = tk.Button(frm, text='Calculate', command=doAction)
btn1.configure(bg='white')
btn1.pack(expand=True, fill=tk.X, padx=10, pady=10)

# イベントループの実行
root.mainloop()
