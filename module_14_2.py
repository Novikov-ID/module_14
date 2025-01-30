import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_username ON Users (username)")

for i in range(10):
    cursor.execute('INSERT INTO Users('
                   'username,'
                   'email,'
                   'age,'
                   'balance)'
                   ' VALUES(?,?,?,?)',
                   (
                       f'User{i + 1}',
                       f'example{i + 1}@gmail.com',
                       (i + 1) * 10,
                       1000
                   )
                   )

cursor.execute('UPDATE Users SET balance = balance - 500 WHERE id % 2 = 1')
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
total_users = cursor.execute('SELECT COUNT(*) FROM Users').fetchone()[0]
total_balance = cursor.execute('SELECT SUM(balance) FROM Users').fetchone()[0]
print(total_balance / total_users)

connection.commit()
connection.close()
