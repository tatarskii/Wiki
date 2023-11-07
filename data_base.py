import sqlite3
import json

with open('parsed_links.json', 'r') as f:
    parsed_links = json.load(f)
def connect():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    # Create table if not exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Wiki_links (
    id INTEGER PRIMARY KEY,
    parent_link TEXT NOT NULL,
    link TEXT NOT NULL,
    title TEXT NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


def into():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Wiki_links (parent_link, link, title) VALUES (?, ?, ?)',
                   ('https://en.wikipedia.org/wiki/Dildo', 'https://en.wikipedia.org/wiki/Dildo', 'Dildo'))

    connection.commit()
    connection.close()


def read():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Wiki_links')
    parent_link = cursor.fetchall()

    for parent_link in parent_link:
        print(parent_link)

    connection.close()


class DataBase:
    pass


print(into())
