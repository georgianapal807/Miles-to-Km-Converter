from tkinter import *


def convert():
    converted_value = int(input_value.get()) * 1.609344
    converted_value_label.config(text=f"{round(converted_value, 2)}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# User Input box
input_value = Entry(width=7)
input_value.grid(column=1, row=0)

# Labels define
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

label = Label(text="is equal to")
label.grid(column=0, row=1)

converted_value_label = Label(text="0")
converted_value_label.grid(column=1, row=1)

Km_label = Label(text="Km")
Km_label.grid(column=2, row=1)

# Button define
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)

window.mainloop()
