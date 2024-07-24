import sqlite3

conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS books
(id INTEGER PRIMARY KEY, title TEXT, author TEXT, price REAL)
''')
conn.commit()

def add_book(title, author, price):
    cursor.execute('INSERT INTO books (title, author, price) VALUES (?, ?, ?)', (title, author, price))
    conn.commit()

add_book('The Catcher in the Rye', 'J.D. Salinger', 10.99)
