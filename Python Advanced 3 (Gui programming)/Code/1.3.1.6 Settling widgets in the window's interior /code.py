import tkinter as tk


window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")
button_1.pack(side="left", fill="y")
button_2.pack(side="left", fill="y")
button_3.pack(side="left", fill="y")
window.mainloop()