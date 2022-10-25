import sqlite3

def structure():
    con = sqlite3.connect('books.db')
    cur= con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()

def insert(Title, Author, Year, isbn):
    con = sqlite3.connect('books.db')
    cur= con.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(Title, Author, Year, isbn))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect('books.db')
    cur= con.cursor()
    cur.execute("SELECT * FROM book")
    fetch=cur.fetchall()
    con.close()
    return fetch

#the "" in the function parameters (Title, Author, Year, isbn) is in case the user only searches using one of the parameters itll
#fill in the other ones as empty. this way it can search without having to fill in every parameter.
def search(Title="", Author="", Year="", isbn=""):
    con = sqlite3.connect('books.db')
    cur= con.cursor()
    cur.execute("SELECT * FROM book  WHERE Title=? OR Author=? OR Year=? OR isbn=?", (Title, Author, Year, isbn))
    fetch=cur.fetchall()
    con.close()
    return fetch

def delete(id):
    con = sqlite3.connect('books.db')
    cur= con.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    con.commit()
    con.close()

def update(id, Title, Author, Year, isbn):
    con = sqlite3.connect('books.db')
    cur= con.cursor()
    cur.execute("UPDATE book SET Title=?, Author=?, Year=?, isbn=? WHERE id=?",(Title, Author, Year, isbn, id))
    con.commit()
    con.close()

structure()
#delete(2)
#insert("HP: Goble of Fire","JK Rowling", 2005, 114433)
#print(search(Author="JK Rowling"))
#update(3, "Goblet of Fire", "JK Rowling",2005,114433)
#print(view())