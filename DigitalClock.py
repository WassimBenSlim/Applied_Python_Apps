from time import strftime
from tkinter import Label, Tk

#window config for clock
window = Tk()
window.title("")
window.geometry('200x80')
window.configure(bg="black")
window.resizable(False,False)

#label config
clock_label=Label(window, bg="black", fg="white", font = ("Times", 20, 'bold'), relief='flat')
clock_label.place(x = 20,y = 20)

#updating
def updatingLabel():
    currentTime= strftime('%p  ' '%I:' '%M:' '%S')
    clock_label.configure(text = currentTime)
    clock_label.after(80,updatingLabel)

updatingLabel()
window.mainloop()
