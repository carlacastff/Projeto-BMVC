import sqlite3, os, hashlib

DB_PATH = "controllers/db/bancoCadastros.db"     #caminho banco de dados

class Login():
    def addConta(self, dados):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO cadastros 
                    (tipo, email, primeiroNome, segundoNome, senhaProtegida, telefone)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    dados.get('tipo', 'usuario'),
                    dados['email'],
                    dados['primeiroNome'],
                    dados['segundoNome'],
                    self._protegeSenha(dados['senha']),  # Salva o HASH, não a senha
                    dados.get('telefone', '')
                ))
                conn.commit()
                return True, "Conta criada com sucesso!"
        except sqlite3.IntegrityError:
            return False, "E-mail já cadastrado"
        except Exception as e:
            return False, f"Erro ao criar conta: {str(e)}"

    def _protegeSenha(self, senha): #deixa a senha protegida
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def verificarLogin(self, email, senha): #verifica se email e senhas estao corretos
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("""
                SELECT * FROM cadastros 
                WHERE email = ? AND senhaProtegida = ?
            """, (email, self._protegeSenha(senha)))
            usuario = cur.fetchone()
            return dict(usuario) if usuario else None

    def buscaEmail(self, email):        #busca usuario por email
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM cadastros WHERE email = ?", (email,))
            usuario = cur.fetchone()
            return dict(usuario) if usuario else None
        
    def deletar(self, sessaoID):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()

                cur.execute("SELECT * FROM cadastros WHERE id = ?", (sessaoID,))
                cadastro = cur.fetchone()
                cadastroDicionario = dict(cadastro)
                
                cur.execute("DELETE FROM cadastros WHERE id = ?", (sessaoID,))
                conn.commit()
                return f"Casdastro de '{cadastroDicionario['primeiroNome']}' deletado com sucesso"
        except Exception as e:
            return f"Erro ao deletar conta: {str(e)}"
        
    def atualizarSessao(self, usuarioID, sessaoID):  #Atualiza ID da sessão do usuário
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE cadastros SET sessaoID = ? WHERE id = ?", 
                    (sessaoID, usuarioID))
            conn.commit()

    def buscarSessao(self, sessaoID): #Busca usuário por ID de sessão
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM cadastros WHERE sessaoID = ?", (sessaoID,))
            usuario = cur.fetchone()
            return dict(usuario) if usuario else None
        
    def editar(self, novosDados, usuarioID=None):
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""UPDATE cadastros SET email = ?, primeiroNome = ?, segundoNome = ?, telefone = ?
                         WHERE id = ?""", (novosDados['email'], novosDados['primeiroNome'], novosDados['segundoNome'], novosDados['telefone'], usuarioID))
            conn.commit()

if __name__ == "__main__":
    usuario = Login()
    dados = {
        'tipo': 'admin', 
        'email': 'email@gmail.com', 
        'primeiroNome': 'Administrador', 
        'segundoNome': '1', 
        'senha': '12345',
        'telefone': '0000000000'
    }
    
    resultado, mensagem = usuario.addConta(dados)
    print(f"Sucesso: {resultado}, Mensagem: {mensagem}")