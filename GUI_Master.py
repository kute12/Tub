
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk


global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Tuberculosis detection using Machine learning ")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('mastertu.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)





video_label =tk.Label(root)
video_label.pack()


#
label_l1 = tk.Label(root, text="Tuberculosis detection using Machine learning",font=("Times New Roman", 35, 'bold'),
                    background="#152238", fg="white", width=55, height=1)
label_l1.place(x=0, y=0)



def reg():
    from subprocess import call
    call(["python","socialdistance.py"])

def log():
    from subprocess import call
    call(["python","GUI_Master_old.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Tuberculosis detection ", command=log, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=160)

#button2 = tk.Button(root, text="Future Forecasting",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
#button2.place(x=100, y=240)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=100, y=260)

root.mainloop()