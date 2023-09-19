import sqlite3


conector = sqlite3.connect("transações.db")
curso = conector.cursor()

curso.execute("CREATE TABLE transações (id integer, transações text)")