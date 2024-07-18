import sqlite3

def init_db():
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS prices
                 (item_name text, website text, price real, link text)''')
    conn.commit()
    conn.close()

init_db()
