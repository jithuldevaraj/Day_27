import tkinter

window = tkinter.Tk()
window.title("Mile to Kilometers")
window.config(padx=20, pady=20)

def calculate():
   miles = int(entry.get())
   kilometers = miles / 1.60934
   result_label.config(text=f"{kilometers:.2f}")


# Entry
entry = tkinter.Entry(window)
entry.grid(row=0, column=1)

# Entry label
miles_label = tkinter.Label(window, text ="Miles")
miles_label.grid(row=0, column=2)

# label
is_equal_label = tkinter.Label(window, text ="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = tkinter.Label(window, text ="0")
result_label.grid(row=1, column=1)

km_label = tkinter.Label(window, text ="Km")
km_label.grid(row=1, column=2)

button = tkinter.Button(window, text = "Calculate", command=calculate)
button.grid(row=2, column=1)



window.mainloop()