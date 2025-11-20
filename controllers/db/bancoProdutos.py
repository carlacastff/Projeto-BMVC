import sqlite3

con = sqlite3.connect('bancoProdutos.db')
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    capa TEXT NOT NULL,
    fotos TEXT,
    titulo TEXT NOT NULL,
    artista TEXT,
    descricao TEXT NOT NULL,
    tracklist TEXT,
    genero TEXT,
    ano INTEGER,
    preco REAL NOT NULL,
    quantidade INTEGER NOT NULL
)
""")

con.commit()
con.close()
