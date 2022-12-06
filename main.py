from helpers import add_watermark
from tkinter import filedialog
from tkinter import *


class Application(Frame):

    def main(self):
        self.filename = filedialog.askopenfilename(initialdir='/Users/macbook/Downloads', title='Select an Image:')
        watermark_text = self.watermark_text_entry.get()
        add_watermark(self.filename, watermark_text)

    def create_widgets(self):
        self.title_text = Label(text="Watermark app")
        self.title_text.grid(column=1, row=0, padx=20, pady=40)
        self.watermark_text = Label(text="Watermark text:")
        self.watermark_text.grid(column=0, row=2)
        self.watermark_text_entry = Entry(width=21)
        self.watermark_text_entry.grid(column=1, row=2)
        self.button = Button(root, text="Select Image", command=self.main)
        self.button.grid(column=1, row=3)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.filename = None
        self.create_widgets()


root = Tk()
root.title("Watermarkly")
app = Application(master=root)
root.config(padx=100, pady=50,)

app.mainloop()