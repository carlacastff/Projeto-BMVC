import sqlite3, os, uuid

DB_PATH = "controllers/db/bancoProdutos.db"     #caminho banco de dados
UPLOAD_PATH = "static/imagens/Catalogo/teste"   #pasta das imagens

class ProdutoModel:
    def _nomeUnico(self, filename):
        if not filename:
            return None
        extensao = os.path.splitext(filename)[1]    #extensão do arquivo
        return f"{uuid.uuid4().hex}{extensao}"      #gera um ID unico para nào ter repetição

    def _salvaArqv(self, arquivo, nomeUnico):
        arquivo.save(os.path.join(UPLOAD_PATH, nomeUnico))  #grava o caminho final do arquivo
        return nomeUnico

    def _salvaCapa(self, capa): #salva capa do produto, se nao tiver n retorna nada, mas é pra ter!!!
        if capa and capa.filename:  
            nome = self._nomeUnico(capa.filename)
            return self._salvaArqv(capa, nome)
        return None

    def _salvaFts(self, fotos):     #salva fotos adicionais, uma por uma
        nomes = []
        for foto in fotos:
            if foto and foto.filename:
                nome = self._nomeUnico(foto.filename)
                self._salvaArqv(foto, nome)
                nomes.append(nome)      #armazena todos os nomes em uma string
        return ",".join(nomes)

    def _delArqvsProduto(self, produto):  # deleta capa e fotos
        if produto.get('capa'):
            caminho = os.path.join(UPLOAD_PATH, produto['capa'])
            if os.path.exists(caminho):
                os.remove(caminho)

        if produto.get('fotos'):
            for foto in produto['fotos'].split(","):
                foto = foto.strip()
                if foto:
                    caminho = os.path.join(UPLOAD_PATH, foto)
                    if os.path.exists(caminho):
                        os.remove(caminho)

    ################# CRUD ###############################################################################

    def criar(self, dados, capa, fotos):
        os.makedirs(UPLOAD_PATH, exist_ok=True)     #garante que a pasta existe

        capaNome = self._salvaCapa(capa)    #salva
        ftsString = self._salvaFts(fotos)   #salva

        with sqlite3.connect(DB_PATH) as conn:  #basicamente insere tudo no banco
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO produtos 
                (tipo, capa, fotos, titulo, artista, descricao, tracklist, genero, ano, preco, quantidade)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                dados["tipo"], capaNome, ftsString, dados["titulo"], dados["artista"],
                dados["descricao"], dados["tracklist"], dados["genero"], dados["ano"],
                dados["preco"], dados["quantidade"]
            ))

            conn.commit()
            return cur.lastrowid

    def pesquisar(self, termo):
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row      # permite acessar colunas pelo nome
            cur = conn.cursor()
            cur.execute("SELECT * FROM produtos WHERE titulo LIKE ?", (f"%{termo}%",)) # busca parcial
            return cur.fetchone()   #retorna primeiro resultado

    def pesquisaID(self, produto_id):       #mesma coisa que o de cima
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
            return cur.fetchone()

    def editar(self, produto_id, dados, capa=None, fotos=None):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()

                cur.execute("SELECT capa, fotos FROM produtos WHERE id = ?", (produto_id,)) #procura produto
                produtoAtual = cur.fetchone()

                if not produtoAtual:
                    return f"Produto com ID {produto_id} não encontrado"    #não achou? retorna essa mensagem

                produtoAtual = dict(produtoAtual)   #tranforma em dicionario

                if capa and capa.filename:      # se veio nova capa então apaga antiga e salva nova
                    if produtoAtual.get("capa"):
                        pathAntigo = os.path.join(UPLOAD_PATH, produtoAtual["capa"])
                        if os.path.exists(pathAntigo):
                            os.remove(pathAntigo)
                    capaNome = self._salvaCapa(capa)
                else:                           # senão mantem a antiga
                    capaNome = produtoAtual["capa"]

                if fotos and any(f.filename for f in fotos):        #se recebeu novas fotos add e apaga antigas
                    if produtoAtual.get("fotos"):
                        self._delArqvsProduto({"fotos": produtoAtual["fotos"], "capa": None})
                    ftsString = self._salvaFts(fotos)
                else:                                       #  senão mantem a antiga
                    ftsString = produtoAtual["fotos"]

                cur.execute("""                                         
                    UPDATE produtos SET 
                    tipo = ?, capa = ?, fotos = ?, titulo = ?, artista = ?, 
                    descricao = ?, tracklist = ?, genero = ?, ano = ?, preco = ?, quantidade = ?
                    WHERE id = ?
                """, (
                    dados["tipo"], capaNome, ftsString, dados["titulo"], dados["artista"],
                    dados["descricao"], dados["tracklist"], dados["genero"], dados["ano"],
                    dados["preco"], dados["quantidade"], produto_id
                ))      #atualiza banco

                conn.commit()
                return f"Produto '{dados['titulo']}' atualizado com sucesso!"      #não aparece, mas existe

        except Exception as e:
            return f"Erro ao editar produto: {str(e)}"

    def delete(self, idProd):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()

                cur.execute("SELECT * FROM produtos WHERE id = ?", (idProd,))
                produto = cur.fetchone()

                if not produto:         #verifica existencia do produto
                    return f"Erro: Produto com ID {idProd} não encontrado"  #pq nao aparece???? :(

                produtoDicionario = dict(produto)

                self._delArqvsProduto(produtoDicionario)    # Deleta arquivos

                cur.execute("DELETE FROM produtos WHERE id = ?", (idProd,)) # Deleta do banco
                conn.commit()

                return f"Produto '{produtoDicionario['titulo']}' deletado com sucesso" #???

        except Exception as e:
            return f"Erro ao deletar produto: {str(e)}"

    def produtoExiste(self, titulo, artista=None):      #produto existe, procura artista e título. Se não tiver só titulo
        with sqlite3.connect(DB_PATH) as conn:
            cur = conn.cursor()
            if artista:
                cur.execute("SELECT id FROM produtos WHERE titulo = ? AND artista = ?", (titulo, artista))
            else:
                cur.execute("SELECT id FROM produtos WHERE titulo = ?", (titulo,))

            return cur.fetchone() is not None

    def listar(self):       # literalmente o nome
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM produtos")
            rows = cur.fetchall()
            return [dict(row) for row in rows]
