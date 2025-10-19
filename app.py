import tkinter as tk
import time

root = tk.Tk()
root.title("Digital clock")
root.geometry("500x200")

def display_livetime():
    livetime = time.strftime("%H:%M:%S")
    label.config(text=livetime)
    label.after(1000,display_livetime)

label = tk.Label(root,font=("Arial",80,"bold"),bg="black",fg="pink")
label.pack(expand=True)

display_livetime()
root.mainloop()
