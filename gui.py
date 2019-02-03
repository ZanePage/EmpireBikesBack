from tkinter import *
import linedetectiontemp as ld
import matplotlib.image as mpimg
# pip install pillow
from PIL import Image, ImageTk

def getAnotatedImage():
    return ld.annotate_image(mpimg.imread('lines.jpeg'))

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open("lines.jpeg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

class OtherWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open(getAnotatedImage())
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)



root = Tk()
right = Window(root)
right.pack(side=RIGHT)
left = OtherWindow(root)
left.pack(side=LEFT)
root.wm_title("Tkinter window")
root.geometry("1500x450")
root.mainloop()
