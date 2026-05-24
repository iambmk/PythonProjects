from tkinter import *

def button_clicked():
    print("clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI")
window.minsize(500, 300)
window.config(padx=100,pady=100)

#label
my_label = Label(text="I am a label", font=("Arial", 12, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

#Button
button = Button(window, text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(window, text="New Button")
new_button.grid(row=0, column=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(row=2, column=3)



window.mainloop()