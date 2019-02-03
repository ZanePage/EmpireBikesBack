import tkinter
import cv2
from PIL import Image, ImageTk

# create a window
window = tkinter.Tk()

cv_img = cv2.imread("road.jpeg")

# get image dimensions
height, width, no_channels = cv_img.shape

canvas = tkinter.Canvas(window, width = width, height = height)
canvas.pack()

image = ImageTk.PhotoImage(image = Image.fromarray(cv_img))
edged = ImageTk.PhotoImage(image = Image.fromarray(cv_img))

# add image to Canvas
# canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

if panelA is None or panelB in None:
    panelA = Label(image=image)
    panelA.image = image
    panelA.pack(side="left", padx=10, pady=10)

    panelB = Label(image=edged)
    panelB.image = edged
    panelB.pack(side="right", padx=10, pady=10)

else:
    panelA.configure(image=image)
    panelB.configure(image=edged)
    panelA.image = image
    panelB.image = edged
# Run the window loop
window.mainloop()
