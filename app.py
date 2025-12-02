from bottle import route, run, template, static_file, request, post, redirect, response
from models.produtos import ProdutoModel 
from models.cadastros import Login
import uuid

def usuarioLogado():        #verifica se usuário está logado
    sessaoID = request.get_cookie('sessaoID')
    if not sessaoID:
        return None
    else:
        usuario = Login()
        return usuario.buscarSessao(sessaoID)


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

@route('/Perfil', method=['GET'])
def perfil():
    usuario = usuarioLogado()
    if not usuario:
        redirect('/Login')
    
    if usuario['tipo'] == 'admin':
        return template('views/perfilAdm.tpl', produto=None, abaAtiva='criarProduto',termoPesquisa='')
    else:
        return template('views/perfilUser.tpl', usuario=usuario)
    
@post('/MudarDados')
def user():

    return template('views/perfilUser.tpl')

@route('/Login', method=['GET', 'POST'])
def login():
    usuario = usuarioLogado()
    if usuario:
        redirect('/Perfil')
    
    if request.method == 'POST':
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        usuarioLogar = Login()
        usuario = usuarioLogar.verificarLogin(email, senha)

        if usuario:
            sessaoIDnovo = str(uuid.uuid4())
            usuarioID = usuario['id']
            usuarioLogar.atualizarSessao(usuarioID, sessaoIDnovo)
            response.set_cookie('sessaoID', sessaoIDnovo, path='/')
            redirect('/Perfil')
        else:
            return "Login falhou"
        
    return template('views/perfilLogin.tpl')

@route('/Cadastro', method=['POST', 'GET'])
def cadastro():
    usuario = usuarioLogado()
    if usuario:
        redirect('/Perfil')
    
    if request.method == 'POST':
        email = request.forms.get('email')
        usuarioCadastro = Login()
        
        if usuarioCadastro.buscaEmail(email):
            return "Conta já existe, tente fazer login."
        else:
            dados = {
                "email": email, 
                "primeiroNome": request.forms.get('nome'), 
                "segundoNome": request.forms.get('sobrenome'),
                "senha": request.forms.get('senha'),
                "telefone": request.forms.get('telefone')
            }
            sucesso, mensagem = usuarioCadastro.addConta(dados)
            if sucesso:
                redirect('/Login')
            else:
                return mensagem
    
    return template('views/perfilCadastro.tpl')


@post('/CadastrarProduto')  #recebe todos os forms de perfilAdm
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

@route('/Usuario', method=['GET', 'POST'])
def perfil_usuario():
    usuario_model = Login()
    usuario_sessao = usuarioLogado()
    
    if not usuario_sessao:
        redirect('/Login')
        
    if request.method == 'POST':
        acao = request.forms.get('acao')
        
        if acao == 'salvar':
            novosDados =  {
                'primeiroNome': request.forms.get('nome'),
                'segundoNome': request.forms.get('sobrenome'),
                'telefone': request.forms.get('telefone'),
                'email': request.forms.get('email')
            }
            usuario_model.editar(novosDados, usuario_sessao['id'])
            usuario_sessao = usuario_model.buscarSessao(request.get_cookie('sessaoID'))

        elif acao == 'excluir':
            resultado = usuario_model.deletar(usuario_sessao['id'])
            response.delete_cookie('sessaoID')
            redirect('/')
            
        elif acao == 'sair':
            usuario_model.atualizarSessao(usuario_sessao['id'], None)
            response.delete_cookie('sessaoID')
            redirect('/')
    
    return template('views/perfilUser.tpl', usuario=usuario_sessao)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)