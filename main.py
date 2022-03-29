"""
This is the main program that when you run it, it loads the application
"""

# Import external modules
import config
import controller
import view

# Import libraries
import duckdb

# cursor = duckdb.connect()
# con = duckdb.connect(database='db/mib.db', read_only=False)
# # con.execute("CREATE SEQUENCE serial START 101")
#
# # con.execute("CREATE TABLE pictures (id INTEGER, img_path varchar)")
# con.execute("INSERT INTO pictures VALUES (nextval('serial'), 'img/hammer.jpg')")
# con.execute("SELECT * FROM pictures")
# print(con.fetchall())


conn = duckdb.connect('db/mib.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO pictures VALUES (nextval('serial'), 'img/hammer.jpg')")
print(cursor.execute("SELECT * FROM pictures").fetchall())
