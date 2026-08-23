import tkinter
from tkinter import messagebox


# click command gets executed when the button is clicked
def Click():
    # to ask questions you can create messageboxes
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        # we can destroy the created element by destroy() command on it
        skylight.destroy();


skylight = tkinter.Tk()
skylight.title("Skylight")

# we make the button invoke commnad click when clicked
# we just gotta utilize the command option to create subscriptable event
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()
