import sqlite3

with sqlite3.connect("sample.db") as connection:

	c = connection.cursor()
	c.execute("""CREATE TABLE review(titl))