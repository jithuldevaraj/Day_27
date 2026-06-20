import tkinter

window = tkinter.Tk()
window.geometry("500x400")
window.title("Grid Challenge")
window.config(padx=100, pady=130, bg="white")  # Padding common in window (border)

# Label
label_1 = tkinter.Label(window, text = "Label ")
label_1.grid(column=0, row=0)
label_1.config(padx=20, pady=20, bg="blue")  # padding a widget

# Button
button_1 = tkinter.Button(window, text = "Button")
button_1.grid(column=1, row=1)

# Button
new_button = tkinter.Button(window, text ="New Button")
new_button.grid(column=2, row=0)

# Entry
entry = tkinter.Entry(window)
entry.grid(column=3, row=2)


window.mainloop()