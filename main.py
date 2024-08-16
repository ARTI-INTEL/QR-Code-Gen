import qrcode
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("QR Code Generator")
window.iconbitmap("Faiq Icon.ico")

def generate(data, name):
    for widget in window.winfo_children():
        widget.destroy()

    img = qrcode.make(data)
    type(img)  # qrcode.image.pil.PilImage
    img.save(f"{name}.png")

    # Adding the QR Code and resizing it
    image = Image.open(f"{name}.png")
    resized_image = image.resize((400, 400))  # Resize the image to 400x400 pixels
    image_ = ImageTk.PhotoImage(resized_image)
    image_label = Label(window, image=image_)
    image_label.image = image_  # Keep a reference to avoid garbage collection
    image_label.grid(row=0, column=0)

# Getting the Data and file name
data_label = Label(window, text="Enter what you want QR-Coded")
data_label.grid(row=0, column=0)
data = Entry(window, width=100, borderwidth=5)
data.grid(row=0, column=1)
name_label = Label(window, text="Enter what you want the QR Code Image file to be named")
name_label.grid(row=1, column=0)
name = Entry(window, width=100, borderwidth=5)
name.grid(row=1, column=1)
submit = Button(window, text="Submit", command=lambda: generate(data.get(), name.get()))
submit.grid(row=2, column=0, columnspan=2)

window.mainloop()