import sqlite3

# Создание базы данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы пользователей
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Добавление тестовых данных
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', '1234')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'password')")

conn.commit()
conn.close()

print("Database initialized!")
