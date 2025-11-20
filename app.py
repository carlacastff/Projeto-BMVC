from bottle import route, run, template, static_file, request, post, get
from models.produtos import ProdutoModel

@route('/<filepath:path>')      #rota generica para arquivos estáticos
def serve_static(filepath):
    return static_file(filepath, root='.')

@route('/')
def landingPage():
    return template('views/landingPage.tpl')

@route('/Catálogo')
def catalogo():
    return template('views/catálogo.tpl')

@route('/Premium')  #não concluido
def premium():
    return template('views/premium.tpl')

@route('/Sobre')    #não concluido
def sobre():
    return template('views/sobre.tpl')

@route('/Perfil')   #perfil -> produto = none e template deve mostrar a aba de criar produto
def perfil_get():
    return template('views/perfilUser.tpl', produto=None, abaAtiva='criarProduto')

@post('/Perfil') #processa o form de tipoPerfil para saber se é usuario ou adm
def perfil():
    tipo = request.forms.get('tipoPerfil')
    if tipo == "usuario":
        return template('views/perfilUser.tpl')
    else:
        return template('views/perfilAdm.tpl', produto=None, abaAtiva='criarProduto',termoPesquisa='')

@post('/CadastrarProduto')  #recebe todos os forms de perfilAdm (menos tipoPerfil)
def cadastrar_produto():
    if request.forms.get('adicionarProduto'):       #adiciona produto
        titulo = request.forms.get('titulo')
        artista = request.forms.get('artista')
        
        model = ProdutoModel()                      # instancia ProdutoModel() e verifica se o produto já existe
        if model.produtoExiste(titulo, artista):    # método que procura titulo e artista
            return template('views/perfilAdm.tpl', produto=None, abaAtiva='criarProduto', mensagem=f"Erro: Já existe um produto com o título '{titulo}' e artista '{artista}'", 
                            tipo_mensagem='error', termoPesquisa='')
        
        dados = {   
            "tipo": request.forms.get('tipoProd'),
            "titulo": titulo,
            "artista": artista,
            "descricao": request.forms.get('descricao'),
            "tracklist": request.forms.get('tracklist'),
            "genero": request.forms.get('genero'),
            "ano": request.forms.get('ano'),
            "preco": request.forms.get('preco'),
            "quantidade": request.forms.get('quantidade'),
    }   #dicionario com dados do produto

        capa = request.files.get('capa')
        fotos = request.files.getall('fotos')
        
        novoId = model.criar(dados, capa, fotos)        #salva e insere no banco
        return template('views/perfilAdm.tpl', produto=None,  abaAtiva='criarProduto', mensagem=f"Produto cadastrado com sucesso! ID: {novoId}", tipo_mensagem='success', termoPesquisa='')
    
    if request.forms.get('editarProduto'):      #procura produto se tiver na aba editar produto
        termo = request.forms.get('termo')
        model = ProdutoModel()
        produto = model.pesquisar(termo)
        return template('views/perfilAdm.tpl', produto=produto, abaAtiva='editarProduto', termoPesquisa=termo)

    if request.forms.get('salvarEd'):       #botao de salvar clicado
        idProd = request.forms.get('idProd')
        termo = request.forms.get('termo', '')
        
        dados = {   
            "tipo": request.forms.get('tipoProd'),
            "titulo": request.forms.get('titulo'),
            "artista": request.forms.get('artista'),
            "descricao": request.forms.get('descricao'),
            "tracklist": request.forms.get('tracklist'),
            "genero": request.forms.get('genero'),
            "ano": request.forms.get('ano'),
            "preco": request.forms.get('preco'),
            "quantidade": request.forms.get('quantidade'),
        }

        capa = request.files.get('capa')
        fotos = request.files.getall('fotos')
        
        model = ProdutoModel()
        resultado = model.editar(idProd, dados, capa, fotos)    #literalmente edita e muda o que for inserido de novo
        
        produtoAtualizado = model.pesquisaID(idProd)  #renderiza o template
        
        return template('views/perfilAdm.tpl', produto=produtoAtualizado, abaAtiva='editarProduto', mensagem=resultado, tipo_mensagem='success', termoPesquisa=termo)

    if request.forms.get('deletarProduto'):     #aba deletar e pesquisa o produto
        termo = request.forms.get('termo')
        model = ProdutoModel()
        produto = model.pesquisar(termo)
        return template('views/perfilAdm.tpl', produto=produto, abaAtiva='deletarProduto', termoPesquisa=termo)
    
    if request.forms.get('confirmar_delecao'):
        idProd = request.forms.get('idProd')
        termo = request.forms.get('termo', '')
        
        model = ProdutoModel()
        resultado = model.delete(idProd)
        
        produto = model.pesquisar(termo)    # busca novamente (vai retornar None se tiver sido deletado)
        
        return template('views/perfilAdm.tpl', produto=produto, abaAtiva='deletarProduto',mensagem=resultado, tipo_mensagem='success',  termoPesquisa=termo)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)