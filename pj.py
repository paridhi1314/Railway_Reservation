import tkinter as tk
import sys
from tkinter import messagebox

w1=tk.Tk()
w1.geometry("1366x720")



#main method 

def main():
    f=tk.PhotoImage(file="background_image.png")
    background_label=tk.Label(w1,image=f)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)


    #creating the frame

    frame_input=tk.Frame(w1,bg='#f48d51')
    frame_input.place(x=320,y=130,height=500,width=400)


    #adding text to the frame
    tk.Label(text="IRCTC LOGIN", font=("Century Gothic BOLD",30),fg="red").place(x=400,y=150)



    w1.mainloop()

main()
