import sqlite3

def select(cursor):
    inf = cursor.execute("SELECT * FROM users;")
    result = inf.fetchall()
    return result

def insert(cursor):
    cursor.execute("INSERT INTO users (name, surname, gender) VALUES (?,?,?); ",(name, surname, gender))

def select_id(cursor,id_):
    inf = cursor.execute("SELECT * FROM USERS WHERE id = ?;",(id_,))
    result = inf.fetchall()
    return result 

def dele(cursor):
    cursor.execute("DELETE FROM USERS")

with sqlite3.connect("C:\\Users\\bzk\\Documents\\python\\3модуль\\data_1.db") as cursor:
    #print(select(cursor))
    #print(select(cursor))
    print(select(cursor))
    dele(cursor,1)
    print(select(cursor))

   