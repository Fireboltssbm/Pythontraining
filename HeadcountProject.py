import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import CENTER, W, Button, ttk
from tkinter.messagebox import NO

matplotlib.use('TkAgg')

root = tk.Tk()
root.geometry('800x800')
root.title('Headcount Project')

def home_page():
    home_frame=tk.Frame(main_frame)

    label = tk.Label(home_frame, text='Home page', font=('bold', 35))
    label.pack()

    home_frame.pack(pady=20)

def event_page():
    event_frame = tk.Frame(main_frame)

    label = tk.Label(event_frame, text='Event Page', font=('bold', 35))
    label.pack()

    my_tree_event = ttk.Treeview(event_frame)
    my_tree_event['columns'] = ("Name", "Tag", "Smash Bros Main")
    my_tree_event.column("#0", width = 0, stretch=NO)
    my_tree_event.column("Name", anchor = W, width = 70)
    my_tree_event.column("Tag", anchor = CENTER, width = 70)
    my_tree_event.column("Smash Bros Main", anchor=W, width = 120)

    my_tree_event.heading("#0", text = "", anchor = W)
    my_tree_event.heading("Name", text = "Name", anchor = W)
    my_tree_event.heading("Tag", text = "Tag", anchor = CENTER)
    my_tree_event.heading("Smash Bros Main", text = "Smash Bros Main", anchor = W)

    data = [
        ["John", "Firebolt", "Marth"],
        ["Austin", "Footloose", "Link"],
        ["abby", "eclipsar", "kirby"]
        ]
    count = 0
    for record in data:
        my_tree_event.insert(parent='', index='end', iid = count, text='', values=(record[0], record[1], record[2]))
        count +=1

    my_tree_event.pack(pady=20)

    event_frame.pack(pady=20)
    
def members_page():
    members_frame=tk.Frame(main_frame)

    label = tk.Label(members_frame, text='Members Page\n\nPage: 3', font=('bold', 35))
    label.pack()

    my_tree = ttk.Treeview(members_frame)
    my_tree['columns'] = ("Name", "Tag", "Smash Bros Main")
    my_tree.column("#0", width = 0, stretch=NO)
    my_tree.column("Name", anchor = W, width = 120)
    my_tree.column("Tag", anchor = CENTER, width = 70)
    my_tree.column("Smash Bros Main", anchor=W, width = 120)

    my_tree.heading("#0", text = "", anchor = W)
    my_tree.heading("Name", text = "Name", anchor = W)
    my_tree.heading("Tag", text = "Tag", anchor = CENTER)
    my_tree.heading("Smash Bros Main", text = "Smash Bros Main", anchor = W)

    data = [
        ["John", "Firebolt", "Marth"],
        ["Austin", "Footloose", "Link"],
        ["abby", "eclipsar", "kirby"]
        ]
    count = 0
    for record in data:
        my_tree.insert(parent='', index='end', iid = count, text='', values=(record[0], record[1], record[2]))
        count +=1

    my_tree.pack(pady=20)
    members_frame.pack(pady=20)

def email_Page():
    email_frame=tk.Frame(main_frame)

    label = tk.Label(email_frame, text='Email Page', font=('bold', 35))
    label.pack()

    emailTxt = tk.Text(email_frame, height=1, width=25)
    emailTxt.pack()

    emailButton = Button(email_frame, text="Send Email", font=('bold', 20), fg="white", bd=0, bg='black')
    emailButton.pack()

    email_frame.pack()

def graph_page():
    graph_frame=tk.Frame(main_frame)

    label = tk.Label(graph_frame, text='Graph Page', font=('bold', 35))
    label.pack()

    f = Figure(figsize=(5,5), dpi=100)
    a = f.add_subplot(111)
    a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,5,7,8,10])

    canvas = FigureCanvasTkAgg(f, master=graph_frame)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    graph_frame.pack()



def hide_indicators():
    home_indicate.config(bg='#c3d3c3')
    event_indicate.config(bg='#c3d3c3')
    member_indicate.config(bg='#c3d3c3')
    email_indicate.config(bg='#c3d3c3')
    graph_indicate.config(bg='#c3d3c3')

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

def indicate(label, page):
    hide_indicators()
    label.config(bg='#158aff')
    delete_pages()
    page()


options_frame = tk.Frame(root, bg="#c3d3c3")

home_btn = tk.Button(options_frame, text='Home', font=('bold', 15), fg="#158aff", bd=0, bg='#c3d3c3', command=lambda: indicate(home_indicate, home_page))

home_btn.place(x=10,y=50)

home_indicate = tk.Label(options_frame, text='', bg ='#c3d3c3')
home_indicate.place(x=3, y=50, width=5, height=40)

event_btn = tk.Button(options_frame, text='Events', font=('bold', 15), fg="#158aff", bd=0, bg='#c3d3c3', command=lambda: indicate(event_indicate, event_page))

event_btn.place(x=10,y=100)

event_indicate = tk.Label(options_frame, text="", bg = "#c3d3c3")
event_indicate.place(x=3, y=100, width=5, height=40)

member_btn = tk.Button(options_frame, text='Members', font=('bold', 15), fg="#158aff", bd=0, bg='#c3d3c3', command=lambda: indicate(member_indicate, members_page))

member_btn.place(x=10,y=150)

member_indicate = tk.Label(options_frame, text="", bg = "#c3d3c3")
member_indicate.place(x=3, y=150, width=5, height=40)


email_btn = tk.Button(options_frame, text='Email', font=('bold', 15), fg="#158aff", bd=0, bg='#c3d3c3', command=lambda: indicate(email_indicate, email_Page))

email_btn.place(x=10,y=200)

email_indicate = tk.Label(options_frame, text="", bg= "#c3d3c3")
email_indicate.place(x=3, y=200, width=5, height=40)

graph_btn = tk.Button(options_frame, text='Graph', font=('bold', 15), fg="#158aff", bd = 0, bg="#c3d3c3", command=lambda: indicate(graph_indicate, graph_page))
graph_btn.place(x=10, y=250)

graph_indicate = tk.Label(options_frame, text="", bg="#c3d3c3")
graph_indicate.place(x=3, y=250, width=5, height=40)

options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=125, height=800)

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)

main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=800, width = 800)

root.mainloop()
