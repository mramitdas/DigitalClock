import pytz
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

canvas = Canvas(root, width=1280, height=720)
canvas.pack()

root.resizable(0,0)
root.title('Digital clock')

image_open = Image.open("digital clock.jpg").resize((1280, 720))

img = ImageTk.PhotoImage(image_open)
canvas.create_image(0,0,anchor=NW, image=img)

ui = Frame(root, width=442, height=100, bg='#92c1c9')
ui.place(x=270, y=310)

def time():

    IST = pytz.timezone('Asia/Kolkata')
    time_zone = datetime.now(IST)

    day = datetime.today().strftime('%A')[0:2].upper()

    current_time = time_zone.strftime('%I:%M:%S')

    text.config(text=f"{day}+{current_time}")
    text.after(1000,time)

text = Label(ui, font=(('Ds-Digital', 'bold'), 84), bg='#92c1c9', fg='#000000')
text.place(x=10, y=3)
time()

root.mainloop()