import sqlite3

DB_NAME = "krown.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, is_banned INTEGER DEFAULT 0)''')
    c.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, cat TEXT, img TEXT)''')
    c.execute("SELECT COUNT(*) FROM products")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO products (name, price, cat, img) VALUES (?, ?, ?, ?)", ("Rick and Morty", 17, "Жидкости", "https://picsum.photos/seed/vape1/200"))
    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, name, price, cat, img FROM products")
    prods = [{"id": r[0], "name": r[1], "price": r[2], "cat": r[3], "img": r[4]} for r in c.fetchall()]
    conn.close()
    return prods

# Инициализация базы данных при запуске сервера
init_db()
