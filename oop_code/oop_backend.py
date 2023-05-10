import sqlite3

class Database:
    # create the main structure of the GUI
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur= self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, isbn INTEGER)")
        self.con.commit()

    #add the insert button func
    def insert(self, Title, Author, Year, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(Title, Author, Year, isbn))
        self.con.commit()

    #add the view button func
    def view(self):
        self.cur.execute("SELECT * FROM book")
        fetch=self.cur.fetchall()
        return fetch
    
    #add the search button func
    def search(self, Title="", Author="", Year="", isbn=""):
        self.cur.execute("SELECT * FROM book  WHERE Title=? OR Author=? OR Year=? OR isbn=?", (Title, Author, Year, isbn))
        fetch=self.cur.fetchall()
        return fetch
    
    #add the delete button func
    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.con.commit()

    #add the update button func
    def update(self, id, Title, Author, Year, isbn):
        self.cur.execute("UPDATE book SET Title=?, Author=?, Year=?, isbn=? WHERE id=?",(Title, Author, Year, isbn, id))
        self.con.commit()

    #close the app button
    def __del__(self):
        self.con.close()
