import sqlite3

con = sqlite3.connect('bancoCadastros.db')
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS cadastros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT DEFAULT 'usuario',
    email TEXT UNIQUE NOT NULL,
    primeiroNome TEXT NOT NULL,
    segundoNome TEXT NOT NULL,
    senhaProtegida TEXT NOT NULL,
    telefone TEXT,
    sessaoID TEXT
)
""")

con.commit()
con.close()