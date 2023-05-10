"""
Create a Front End Program that stores the following book information:
1. Title 2. Author 3. Year 4. ISBN

The following functions can be used in this program:
1. Add Entry
2. Delete Entry
3. View all the records
4. Search for a specific Entry
5. Update an Entry
6. Close the program
"""
from tkinter import *
from oop_backend import Database

database = Database('books.db')

#add the view command
def view_command():
    list1.delete(0,END)
    for fetch in database.view():
        list1.insert(END, fetch)

#add the search command
def search_command():
    list1.delete(0,END)
    for fetch in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, fetch)

#add the add command
def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def get_selected(event):
    global select_tuple
    if list1.curselection():
        index= list1.curselection()[0]
        select_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,select_tuple[1])
        e2.delete(0,END)
        e2.insert(END,select_tuple[2])
        e3.delete(0,END)
        e3.insert(END,select_tuple[3])
        e4.delete(0,END)
        e4.insert(END,select_tuple[4])

# add the delete command
def delete_command():
    database.delete(select_tuple[0])

#add the update command
def update_command():
    database.update(select_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())



#create the GUI
window = Tk()


def bookstore():
    print()

#create the entire frontend design
l1 = Label(window, text= "Title", justify= 'center')
l1.grid(row=0, column=0)

l2 = Label(window, text= "Author", justify= 'center')
l2.grid(row=0, column=2)

l3 = Label(window, text= "Year", justify= 'center')
l3.grid(row=1, column=0)

l4 = Label(window, text= "ISBN", justify= 'center')
l4.grid(row=1, column=2)

l5 = Label(window, text= "Omar Jomaa's Collection", justify= 'center')
l5.grid(row=0, column=4, rowspan=2, columnspan=2)

title_text= StringVar()
e1 = Entry(window, textvariable= title_text)
e1.grid(row=0, column=1)

author_text= StringVar()
e2 = Entry(window, textvariable= author_text)
e2.grid(row=0, column=3)

year_text= StringVar()
e3 = Entry(window, textvariable= year_text)
e3.grid(row=1, column=1)

isbn_text= StringVar()
e4 = Entry(window, textvariable= isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=10, width=67)
list1.grid(row=2, column=0, rowspan=6, columnspan=4, sticky=W, pady=3)

sb1= Scrollbar(window)
sb1.grid(row=2, column=4, rowspan=6, sticky=W)

list1.bind('<<ListboxSelect>>', get_selected)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text= "View All", width=20, command= view_command)
b1.grid(row=2, column = 5, columnspan=2, pady=3, padx=5)

b2 = Button(window, text= "Add", width=20, command= add_command)
b2.grid(row=3, column = 5, columnspan=2, pady=3, padx=5)

b3 = Button(window, text= "Delete", width=20, command= delete_command)
b3.grid(row=4, column = 5, columnspan=2, pady=3, padx=5)

b4 = Button(window, text= "Update", width=20, command=update_command)
b4.grid(row=5, column = 5, columnspan=2, pady=3, padx=5)

b5 = Button(window, text= "Search", width=20, command=search_command)
b5.grid(row=6, column = 5, columnspan=2, pady=3, padx=5)

b6 = Button(window, text= "Exit App", width=20, command= window.destroy)
b6.grid(row=7, column = 5, columnspan=2, pady=3, padx=5)

window.wm_title("Omar's Book Collection")


window.mainloop()