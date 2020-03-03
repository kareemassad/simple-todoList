# A simple To Do List by Kareem El Assad
#Python 3.6.7

import tkinter
import random

# Create root window
root = tkinter.Tk()
# Change window background color
root.configure(bg="white")
# Change Title
root.title("My To-Do List")
# Change window size
root.geometry("200x500")

# Create an empty list
tasks = []
tasks = ["Call mom", "buy toilet paper", "ahmed gay"]

# Functions
def update_listbox():
    clear_listbox()
    for task in tasks:
        listBox_tasks.insert("end",task) #list at end stack style

def clear_listbox():
    listBox_tasks.delete(0, "end")

def add_task():
    update_listbox()

def del_all():
    pass
def del_one():
    pass
def sort_asc():
    pass
def sort_desc():
    pass
def random():
    pass
def show_tasks():
    pass

label_title = tkinter.Label(root, text="TO-DO-List", bg="white")
label_title.pack()

label_display = tkinter.Label(root, text="", bg="white")
label_display.pack()

text_input = tkinter.Entry(root, width=15)
text_input.pack()

# buttons

btn_add_task = tkinter.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.pack()

btn_del_all = tkinter.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_del_all.pack()

btn_del_one = tkinter.Button(root, text="Delete One", fg="green", bg="white", command=del_one)
btn_del_one.pack()

btn_sort_asc = tkinter.Button(root, text="Sort Ascending", fg="green", bg="white", command=sort_asc)
btn_sort_asc.pack()

btn_sort_desc = tkinter.Button(root, text="Sort Descending", fg="green", bg="white", command=sort_desc)
btn_sort_desc.pack()

btn_random = tkinter.Button(root, text="Choose Random", fg="green", bg="white", command=random)
btn_random.pack()

btn_show_tasks= tkinter.Button(root, text="Show All Tasks", fg="green", bg="white", command=show_tasks)
btn_show_tasks.pack()

btn_exit = tkinter.Button(root, text="Exit", fg="green", bg="white", command=exit)
btn_exit.pack()

listBox_tasks = tkinter.Listbox(root)
listBox_tasks.pack()
#start the main event loop
root.mainloop()