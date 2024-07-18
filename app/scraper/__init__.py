import sqlite3
from app.scraper.kilimall_scraper import scrape_kilimall
from app.scraper.jiji_scraper import scrape_jiji
from app.scraper.jumia_scraper import scrape_jumia

def init_db():
    conn = sqlite3.connect('prices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS prices (
                    item_name TEXT,
                    website TEXT,
                    price REAL,
                    link TEXT
                 )''')
    conn.commit()
    conn.close()

init_db()

__all__ = ['scrape_kilimall', 'scrape_jiji', 'scrape_jumia']
