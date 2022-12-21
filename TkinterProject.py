import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title('Parent Form')
root.geometry('280x200')

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu=tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Forms', menu = file_menu)

def frame_design(child, title, size, bgcolor):
    child.title(title)
    child.geometry(size)
    child.configure(bg=bgcolor)
    return(child)

def frame1_create():
    child1 = tk.Toplevel()
    title = 'Child Frame1'
    size = '800x600'
    bgcolor = 'white'
    frame_design(child1, title, size, bgcolor)

    label1=tk.Label(child1, text = 'I am a child Frame1', bg=bgcolor, fg='blue')
    b1=tk.Button(child1, text = 'close me', bg= 'black', fg= 'white', command=child1.destroy)
    label1.pack()
    b1.pack()
    child1.tkraise()

def frame2_create():
    child2 = tk.Toplevel()
    title = 'Child Frame2'
    size = '800x600'
    bgcolor = 'white'
    frame_design(child2, title, size, bgcolor)

    label2=tk.Label(child2, text = 'I am a child Frame2', bg=bgcolor, fg='blue')
    b2=tk.Button(child2, text = 'close me', bg= 'black', fg= 'white', command=child2.destroy)
    label2.pack()
    b2.pack()
    child2.tkraise()

file_menu.add_command(label='Child Form1', command=frame1_create)
file_menu.add_command(label='Child Form2', command=frame2_create)

file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.destroy)

root_button = tk.Button(root, text="Open Projects", font=('arial bold', 16), fg='white', bg='dark blue', command=frame1_create)
root_button2 = tk.Button(root, text="Open Members", font=('arial bold', 16), fg='white', bg='dark blue', command=frame2_create)
root_button3 = tk.Button(root, text="Open Settings", font=('arial bold', 16), fg='white', bg='dark blue', command=frame1_create)

root_button.place(x=15, y=20)
root_button2.place(x=15, y=80)
root_button3.place(x=15, y=140)

root.mainloop()