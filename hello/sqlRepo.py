import sqlite3
from sqlite3 import Error
import json
from sqlalchemy import create_engine


with open('config\\settings.json', 'r') as f:
    config = json.load(f)




def DBTestFunction():
    # if __name__ == '__main__':
    #create_connection("D:\\DB\\sqlite\\pythonsqlite.db")
    #create_connection("pythonsqlite.db")
    conn = config['Database']['ConnectionString']
    #create_connection(conn)
    alchemyConnection(conn)


def alchemyConnection(db_file):
    engineConn = 'sqlite:///' + db_file
    engine = create_engine(engineConn,echo = True)


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
