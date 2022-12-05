import sqlite3

db_con = sqlite3.connect("db/energy_api.db")
db_cursor = db_con.cursor()
db_cursor.execute(
    ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='street' ''')
