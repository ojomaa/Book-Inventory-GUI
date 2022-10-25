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
import backend

#this is how we connect the view all button to the backend python script with the view function
def view_command():
    #this is added so that once you click the view all button in the front end you dont keep adding the information again and again
    #instead it deletes the information already there and replaces it with the new information in the view all button
    #its basically like refreshing
    list1.delete(0,END)
    for fetch in backend.view():
        #this would mean that in list 1, at to the end of the row the information gathered in the fetch command
        list1.insert(END, fetch)

def search_command():
    list1.delete(0,END)
    #this line takes the information from title_text, author_text, etc. and then the .get() will convert the information into
    #a string that will then be put into the backend.search() and look for the book.
    for fetch in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, fetch)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

#Python tkinter Listbox curselection is used to display the selected item(s).
#curselection is a predefined function that fetches the value(s) of a selected item or items
#now when you select a book in the program, it prints it out in the terminal
def get_selected(event):
    global select_tuple
    #the [0] here means we are grabbing item number zero in the tuple that is presented in the terminal and displaying just that
    #so instead of getting back (2,) which is the tuple, it will only take the first item which is just 2
    if list1.curselection():
        index= list1.curselection()[0]
        #this basically takes the information from the index which is the number in the tuple and gets the information associated with it
        #so itll take index 2 and present the information in it which is the book Goblet of Fire
        select_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,select_tuple[1])
        e2.delete(0,END)
        e2.insert(END,select_tuple[2])
        e3.delete(0,END)
        e3.insert(END,select_tuple[3])
        e4.delete(0,END)
        e4.insert(END,select_tuple[4])

#the delete function looks for the index(the id) of the item you selected(because we chose item 0) and deletes the entire row
def delete_command():
    backend.delete(select_tuple[0])

#update command looks for the select_tuple index(or id) then updates all the other information based on what is put in the entry
def update_command():
    backend.update(select_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())




window = Tk()

def bookstore():
    print()

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

#this takes the selected box in the program and puts it into the get selected function we defined above
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

