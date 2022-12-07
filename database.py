import sqlite3
from sqlite3 import Error


#https://www.sqlitetutorial.net/



def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



sql_create_table_street = """ CREATE TABLE IF NOT EXISTS  streets(
                                    street_id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL
                                ); """

sql_create_table_houses = """CREATE TABLE IF NOT EXISTS houses(
                                house_id   INTEGER PRIMARY KEY,
                                number     TEXT    NOT NULL,
                                lat        TEXT,
                                lng        TEXT,
                                street_id INTEGER NOT NULL,
                                FOREIGN KEY (street_id)
                                REFERENCES streets (street_id) 
                                );"""

gr = """CREATE TABLE supplier_groups (
	group_id integer PRIMARY KEY,
	group_name text NOT NULL
);"""

supp = """CREATE TABLE houses(
    house_id   INTEGER PRIMARY KEY,
    number     TEXT    NOT NULL,
    lat        TEXT,
    lng        TEXT,
    street_id INTEGER NOT NULL,
    FOREIGN KEY (street_id)
       REFERENCES streets (street_id) 
);"""

db_con = create_connection('db/energy_api.db')
create_table(db_con, sql_create_table_street)
create_table(db_con, sql_create_table_houses)
#create_table(db_con, gr)
#create_table(db_con, supp)
db_con.close()
