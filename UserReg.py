import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, email TEXT, pword TEXT)")

name = input("Enter Name: ")

email = input("Enter Email: ")

pword = input("Enter Password: ")

cursor.execute("INSERT INTO users(name,email, pword)VALUES(?,?,?)",(name,email,pword))


conn.commit()

print("Successfully Registered")
