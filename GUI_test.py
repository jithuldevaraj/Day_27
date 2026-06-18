import tkinter
import time

# Create the main window
window_1 = tkinter.Tk()
window_1.title("Test_title")
window_1.geometry("500x300")

# Create Label
label = tkinter.Label(window_1, text="Test_label")
label.place(x=5, y=14)


# Function to reset the label text
def reset_label():
    label["text"] = "Test_label"

def button_cmd():
    # 1. Change the text immediately
    label["text"] = "Button clicked"
    # 2. Schedule the reset_label function to run after 2000 ms (2 seconds)
    window_1.after(2000, reset_label)

# Button
button = tkinter.Button(window_1, text="Click Me", command=button_cmd)
button.place(x=400, y=14)


def print_tkinter_coords(event):
    # Tkinter passes an 'event' object containing the x and y properties
    print(f"Tkinter Clicked at: X={event.x}, Y={event.y}")
# Bind the left mouse button ("<Button-1>") to the function
window_1.bind("<Button-1>", print_tkinter_coords)

window_1.mainloop()
