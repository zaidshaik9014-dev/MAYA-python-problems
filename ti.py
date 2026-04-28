import tkinter as tk
root = tk.Tk()
root.geometry("300x300")
root.title("Welcome to GUI")
label = tk.Label(root, text = "Hello GUI")
label.pack()
root.mainloop()