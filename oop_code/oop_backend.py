import sqlite3

class Database:
    #a positional argument is necessary to run this function and so self is assigned to let the code run
    #db is gonna be another positional argument thatll replace the database file 'books.db' and instead we will call the database file later
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur= self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, isbn INTEGER)")
        self.con.commit()

    def insert(self, Title, Author, Year, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(Title, Author, Year, isbn))
        self.con.commit()

    #a positional argument is needed and so we added self to have one
    def view(self):
        self.cur.execute("SELECT * FROM book")
        fetch=self.cur.fetchall()
        return fetch

    def search(self, Title="", Author="", Year="", isbn=""):
        self.cur.execute("SELECT * FROM book  WHERE Title=? OR Author=? OR Year=? OR isbn=?", (Title, Author, Year, isbn))
        fetch=self.cur.fetchall()
        return fetch

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.con.commit()

    def update(self, id, Title, Author, Year, isbn):
        self.cur.execute("UPDATE book SET Title=?, Author=?, Year=?, isbn=? WHERE id=?",(Title, Author, Year, isbn, id))
        self.con.commit()

    def __del__(self):
        self.con.close()

#delete(2)
#insert("HP: Goble of Fire","JK Rowling", 2005, 114433)
#print(search(Author="JK Rowling"))
#update(3, "Goblet of Fire", "JK Rowling",2005,114433)
#print(view())