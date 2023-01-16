import sqlite3

con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()
sql = 'select * from Acount where user = {}'.format(123)
aaa = cursor.execute(sql)
print(aaa)