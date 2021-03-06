# A simple To Do List by Kareem El Assad
#Python 3.6.7

import tkinter
import random
import tkinter.messagebox

# Create root window
root = tkinter.Tk()
# Change window background color
root.configure(bg="white")
# Change Title
root.title("My To-Do List")
# Change window size
root.geometry("325x275")

# Create an empty list
tasks = []
tasks = ["Call mom", "buy toilet paper", "Finish this thing(lol)"]

# Functions
def update_listbox():
    clear_listbox()
    for task in tasks:
        listBox_tasks.insert("end",task) #list at end stack style

def clear_listbox():
    listBox_tasks.delete(0, "end")

def add_task():
    task = text_input.get()

    if task != "":  #if task is not blank
        tasks.append(task)
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Warning","You need to enter a task")
    
    text_input.delete(0,"end")

def del_all():
    confirmed = tkinter.messagebox.askyesno("Please Confirm", "Sir are you sure about that")
    if confirmed == True:
        global tasks
        tasks = []
        update_listbox()

def del_one():
    #get the item selected
    task = listBox_tasks.get("active")
    #confirm it exists in list
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def randomOne():
    task = random.choice(tasks)
    label_display["text"] = task

def show_tasks_count():
    count = len(tasks)
    msg = "Number of Tasks %s" %count
    label_display["text"] = msg

# GUI
label_title = tkinter.Label(root, text="TO-DO-List", bg="white")
label_title.grid(row=0,column=0)

label_display = tkinter.Label(root, text="", bg="white")
label_display.grid(row=0,column=1)

text_input = tkinter.Entry(root, width=15)
text_input.grid(row=1,column=1)

# Buttons

btn_add_task = tkinter.Button(root, text="Add task", fg="green", bg="white", command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = tkinter.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = tkinter.Button(root, text="Delete One", fg="green", bg="white", command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc = tkinter.Button(root, text="Sort Ascending", fg="green", bg="white", command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = tkinter.Button(root, text="Sort Descending", fg="green", bg="white", command=sort_desc)
btn_sort_desc.grid(row=5,column=0)

btn_randomOne = tkinter.Button(root, text="Choose Random", fg="green", bg="white", command=randomOne)
btn_randomOne.grid(row=6,column=0)

btn_show_tasks_count= tkinter.Button(root, text="Show All Tasks", fg="green", bg="white", command=show_tasks_count)
btn_show_tasks_count.grid(row=7,column=0)

btn_exit = tkinter.Button(root, text="Exit", fg="green", bg="white", command=exit)
btn_exit.grid(row=8,column=0)

listBox_tasks = tkinter.Listbox(root)
listBox_tasks.grid(row=2, column=1, rowspan=7)
#start the main event loop
root.mainloop()