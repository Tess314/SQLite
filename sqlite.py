#link to video I used to create this code
#https://www.youtube.com/watch?v=pd-0G0MigUA

import sqlite3

connection = sqlite3.connect('employee.db')

#a database cursor enables traversal over records
cursor = connection.cursor()

#SQL
cursor.execute("""CREATE TABLE employees(
                firstname text,
                lastname text,
                pay integer
                )""")


cursor.execute("INSERT INTO employees VALUES ('Tess', 'Watt', 1000000)")

#query
cursor.execute("SELECT * FROM employees WHERE lastname='Watt'")

#print query result
print(cursor.fetchone()) #fetchone as result should only be 1 row

connection.commit()
connection.close()
