import sqlite3

DB_PATH = "controllers/db/bancoProdutos.db"

def verificar_produtos():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    print("=== TODOS OS PRODUTOS NO BANCO ===")
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    
    for produto in produtos:
        print(f"ID: {produto['id']}, Título: {produto['titulo']}, Artista: {produto['artista']}, Preço: {produto['preco']}")
    
    conn.close()
    return produtos

if __name__ == "__main__":
    verificar_produtos()