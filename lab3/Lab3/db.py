#Saul Morales, Donald Jalving, Malane Lieng, Brandon Nguyen, Matthew Hernandez,
#Monica Velasco, Kamari Hooks, Gabby Gil- Mazariegos, Gregorio Lopez

import time
import os
import sqlite3

#For this lab, first we create a folder named "data" within our PyCharm project lab3 folder. Then
#in the __init__ method, replace the "data" string with the path to your data folder on your
#machine. If everything was configured correctly, program.py will run and create a database
#object inside the newly created data folder.
class DB:
    def __init__(self):
        self.db_name = "TheDatabaseBlog"
        file = os.path.join("data", self.db_name + ".sqlite_db")
        self.db_file = os.path.abspath(file)

    def create_db(self):
        if os.path.exists(self.db_file):
            print("Database already exists at following location, skipping create")
            print(self.db_file)
            return

        print("Creating database file at: ")
        print(self.db_file)

        with sqlite3.connect(self.db_file) as db:
            db.execute(
                'create table Posts ' +
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'title text,'
                'content text,'
                'published datetime default current_timestamp)'
            )

        print('')


    def insert_base_data(self):
        print('')
        print('Inserting base data')

        if self.has_data():
            print("Data already inserted, skpping")
            return

        with sqlite3.connect(self.db_file) as db:
            db.execute(
                'INSERT INTO Posts (title, content) VALUES '
                '("The first blog post", "This is the content of the first post")')
            time.sleep(.200)
            db.execute(
                'INSERT INTO Posts (title, content) VALUES'
                ' ("The second blog post", "This is the content of another post")')
            time.sleep(.400)
            db.execute(
                'INSERT INTO Posts (title, content) VALUES'
                ' ("A funny post", "This is the content of funny post")')
            time.sleep(.100)
            db.execute(
                'INSERT INTO Posts (title, content) VALUES'
                ' ("A very funny post", "This is the content of funny post")')
        print("done")

    def has_data(self):
        with sqlite3.connect(self.db_file) as db:
            cursor = db.execute("SELECT count(*) FROM Posts")
            data_count = cursor.fetchone()[0]
            return data_count > 0

    def show_all_rows(self):
        print("Showing all rows")
        with sqlite3.connect(self.db_file) as db:
            cursor = db.execute("SELECT * FROM Posts ORDER BY published DESC ")
            for row in cursor:
                print(row)
        print()


    def show_funny_rows(self):
        print("Showing funny rows")
        with sqlite3.connect(self.db_file) as db:
            db.row_factory = sqlite3.Row
            cursor = db.execute("SELECT * FROM Posts WHERE Title LIKE '%funny%' ORDER BY published DESC")
            for row in cursor:
                print("{0}, pubished on {1}".format(row['title'], row['published']))
        print()

    def search_bad(self, search_text):
        print("Showing all rows")
        with sqlite3.connect(self.db_file) as db:
            db.row_factory = sqlite3.Row
            cursor = db.execute("SELECT * FROM Posts WHERE Title LIKE '%" + search_text + "%' ORDER BY published DESC")
            for row in cursor:
                print("{0}, published on {1}".format(row['title'], row['published']))
        print()

    def search(self, search_text):
        search_text = "%{0}%".format(search_text)
        print("Showing all rows")
        with sqlite3.connect(self.db_file) as db:
            db.row_factory = sqlite3.Row
            cursor = db.execute("SELECT * FROM Posts WHERE Title LIKE ? ORDER BY published DESC", (search_text,))
            for row in cursor:
                print("{0}, published on {1}".format(row['title'], row['published']))
        print()