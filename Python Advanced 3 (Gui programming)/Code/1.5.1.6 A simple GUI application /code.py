import tkinter as tk

win = tk.Tk()

label = tk.Label(win, text="Little label:")
label.pack()

frame = tk.Frame(win, height=30, width=100, bg="#000099")
frame.pack()

button = tk.Button(win, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(win, text="Check Button", variable=switch)
checkbutton.pack()

win.mainloop()
