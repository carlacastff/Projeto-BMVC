<!DOCTYPE html>
<html lang="pt-BR">

<head>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="static/estiloPerfilAdm.css">
  <link rel="icon" type="image/png" href="static/imagens/vinil.png">
  <title>Disco 2000</title>
</head>

<body>

  <!-- Cabeçalho -->
  <div class="cabeçalho">
    <header>
      <nav>
        <ul>
          <li><a href="/"><img src='static/imagens/Logo cortada.png' class="logo"></a></li>
          <li><a href="/Catálogo" class="Catálogo">Catálogo</a></li>
          <li><a href="/Premium" class="Premium">Premium</a></li>
          <li><a href="/Sobre" class="Sobre">Sobre</a></li>
          <li><a href="/Favoritos" class="IconFav"><img src="static/imagens/heart.png"></a></li>
          <li><a href="/Carrinho" class="IconShop"><img src="static/imagens/shopping-cart.png"></a></li>
          <li><a href="/Perfil" class="IconPerfil"><img src="static/imagens/circle-user.png"></a></li>
        </ul>
      </nav>
      <hr class="linha">
    </header>
  </div>

  <!-- Título -->
  <section class="título">
    <h1>Administrador</h1>
  </section>

  <!-- Principal -->
  <div class="selecionarOp">

    <!-- Select de Escolha de Produtos -->
    <select name="Produtos" id="selecionarOp" class="selectB">
      <option value="criarProduto">Adicionar Produto</option>
      <option value="editarProduto">Editar Produto</option>
      <option value="deletarProduto">Deletar Produto</option>
    </select>

    <!-- Adicionar Produto -->
    <div class="adicionarProduto" id="adicionarProduto">
      <form method="POST" action="/CadastrarProduto" enctype="multipart/form-data">
        <input type="hidden" name="adicionarProduto" value="1">

        <label>Tipo do Produto:</label>
        <select name="tipoProd" id="tipoProd" class="selectA" required>
          <option value="vitrola">Vitrola</option>
          <option value="album">Álbum</option>
          <option value="boxset">Box Set</option>
          <option value="acessorio">Acessório</option>
        </select>

        <label>Capa do Produto:</label>
        <input type="file" name="capa" accept="image/*" class="arquivo" required>

        <label>Fotos Adicionais:</label>
        <input type="file" name="fotos" accept="image/*" class="arquivo" multiple>

        <label>Nome do Produto:</label>
        <input type="text" name="titulo" required>

        <div class="disco">
          <label>Artista:</label>
          <input type="text" name="artista">
        </div>

        <label>Descrição:</label>
        <textarea name="descricao" required></textarea>

        <div class="disco">
          <label>Tracklist:</label>
          <textarea name="tracklist"></textarea>
        </div>

        <div class="disco">
          <label class="album">Gênero:</label>
          <select name="genero" id="genero" class="selectA">
            <option value="Rock">Rock</option>
            <option value="Nacional">Nacional</option>
            <option value="Pop">Pop</option>
            <option value="Hip-Hop & R&B">Hip-Hop & R&B</option>
            <option value="Jazz">Jazz</option>
            <option value="SoundTrack">Pop</option>
            <option value="Festivo">Festivo</option>
          </select>

          <label class="album">Ano:</label>
          <input type="number" name="ano">
        </div>

        <label>Preço:</label>
        <input type="number" step="0.01" name="preco" required>

        <label>Quantidade:</label>
        <input type="number" name="quantidade" required>

        <button type="submit" class="botaoAdd">Cadastrar Produto</button>
      </form>
    </div>

    <!--Editar Produto -->
    <div class="editarProduto" id="editarProduto" style="display: none;">
      <form method="POST" action="/CadastrarProduto">
        <input type="hidden" name="editarProduto" value="1">
        <label>Nome do Produto:</label>
        <input type="text" name="termo" required value="{{termoPesquisa or ''}}">
        <button type="submit" class="botaoAdd">Pesquisar</button>
      </form>

      % if produto:
      <div class="produtoCard">
        <h2>Editando: {{produto['titulo']}}</h2>

        <form method="POST" action="/CadastrarProduto" enctype="multipart/form-data"
          onsubmit="return confirmarEdicao()">
          <input type="hidden" name="idProd" value="{{produto['id']}}">
          <input type="hidden" name="salvarEd" value="1">

          <!-- Mantem a pesquisa -->
          <input type="hidden" name="termo" value="{{termoPesquisa or ''}}">

          <!-- ps. odeio minha vidaaaaaaaaaaaaaaaaaaaaaaaa, a partir daqui ficou dificil pra crlh -->
          <label>Tipo do Produto:</label>
          <select name="tipoProd" id="tipoProd_editar" class="selectA" required>
            <option value="vitrola" {{!'selected' if produto['tipo']=='vitrola' else '' }}>Vitrola</option>
            <option value="album" {{!'selected' if produto['tipo']=='album' else '' }}>Álbum</option>
            <option value="boxset" {{!'selected' if produto['tipo']=='boxset' else '' }}>Box Set</option>
            <option value="acessorio" {{!'selected' if produto['tipo']=='acessorio' else '' }}>Acessório</option>
          </select>

          <label>Capa do Produto (Atual):</label>
          % if produto['capa']:
          <div>
            <img src="/static/imagens/Catalogo/teste/{{produto['capa']}}"
              style="max-width: 200px; display: block; margin: 10px 0;">
            <small>Imagem atual - deixe em branco para manter</small>
          </div>
          % end
          <input type="file" name="capa" accept="image/*" class="arquivo">

          <label>Fotos Adicionais (Atuais):</label>
          % if produto['fotos']:
          <div>
            % for foto in produto['fotos'].split(','):
            % if foto.strip():
            <img src="/static/imagens/Catalogo/teste/{{foto.strip()}}" style="max-width: 100px; margin: 5px;">
            % end
            % end
            <br><small>Fotos atuais - deixe em branco para manter</small>
          </div>
          % end
          <input type="file" name="fotos" accept="image/*" class="arquivo" multiple>

          <label>Nome do Produto:</label>
          <input type="text" name="titulo" value="{{produto['titulo']}}" required>

          <div class="disco">
            <label>Artista:</label>
            <input type="text" name="artista" value="{{produto['artista'] or ''}}">
          </div>

          <label>Descrição:</label>
          <textarea name="descricao" required>{{produto['descricao']}}</textarea>

          <div class="disco">
            <label>Tracklist:</label>
            <textarea name="tracklist">{{produto['tracklist'] or ''}}</textarea>
          </div>

          <div class="disco">
            <label class="album">Gênero:</label>
            <select name="genero" id="genero_editar" class="selectA">
              <option value="Rock" {{!'selected' if produto['genero']=='Rock' else '' }}>Rock</option>
              <option value="Nacional" {{!'selected' if produto['genero']=='Nacional' else '' }}>Nacional</option>
              <option value="Pop" {{!'selected' if produto['genero']=='Pop' else '' }}>Pop</option>
              <option value="Hip-Hop & R&B" {{!'selected' if produto['genero']=='Hip-Hop & R&B' else '' }}>Hip-Hop & R&B
              </option>
              <option value="Jazz" {{!'selected' if produto['genero']=='Jazz' else '' }}>Jazz</option>
              <option value="SoundTrack" {{!'selected' if produto['genero']=='SoundTrack' else '' }}>SoundTrack</option>
              <option value="Festivo" {{!'selected' if produto['genero']=='Festivo' else '' }}>Festivo</option>
            </select>

            <label class="album">Ano:</label>
            <input type="number" name="ano" value="{{produto['ano'] or ''}}">
          </div>

          <label>Preço:</label>
          <input type="number" step="0.01" name="preco" value="{{produto['preco']}}" required>

          <label>Quantidade:</label>
          <input type="number" name="quantidade" value="{{produto['quantidade']}}" required>

          <button type="submit" class="botaoAdd">Salvar Alterações</button>
        </form>
      </div>
      % end
    </div>

    <!-- Deletar Produto -->
    <div class="deletarProduto" id="deletarProduto" style="display: none;">
      <form method="POST" action="/CadastrarProduto">
        <label>Nome do Produto:</label>
        <input type="text" name="termo" required value="{{termoPesquisa or ''}}">
        <button type="submit" name="deletarProduto" value="1" class="botaoAdd">Pesquisar</button>
      </form>

      % if produto:
      <div class="produtoCard">
        <img src="/static/imagens/Catalogo/teste/{{produto['capa']}}" class="produtoCapa">
        <h1>{{produto['titulo']}}</h1>
        <p><strong>Artista:</strong> {{produto['artista']}}</p>
        <p><strong>Descrição:</strong> {{produto['descricao']}}</p>
        <p><strong>Gênero:</strong> {{produto['genero']}}</p>
        <p><strong>Ano:</strong> {{produto['ano']}}</p>
        <p><strong>Preço:</strong> R$ {{produto['preco']}}</p>
        <p><strong>Quantidade:</strong> {{produto['quantidade']}}</p>

        <!-- Confirmar Seleção? :/ -->
        <form method="POST" action="/CadastrarProduto" onsubmit="return confirmarDelecao()">
          <input type="hidden" name="idProd" value="{{produto['id']}}">
          <!-- Mantem o termo para pesquisa -->
          <input type="hidden" name="termo" value="{{termoPesquisa or ''}}">
          <button type="submit" name="confirmar_delecao" value="1" class="botaoAdd" style="background-color: #992800;">
            Confirmar Deleção
          </button>
        </form>
      </div>
      % end
    </div>
  </div>
    <!-- Sair da conta -->
    <section class="tipoPerfil">
      <form method="POST" action="/Usuario">
        <button type="submit" class="botao" name="acao" value="sair">Sair da conta</button>
      </form>
    </section>

    <script src="static/jsAdmin.js"></script>
    <!--Por algum motivo essa parte só funcionou dentro do .tpl-->
    <script>
      document.addEventListener('DOMContentLoaded', function () {
        let abaAtiva = 'criarProduto'; // valor padrão

        try {
          // Tenta pegar do template, se não existir usa padrão
          abaAtiva = "{{abaAtiva or 'criarProduto'}}";
        } catch (error) {
          console.log('Usando aba padrão');
        }

        const select = document.getElementById('selecionarOp');
        const abas = {
          'criarProduto': document.getElementById('adicionarProduto'),
          'editarProduto': document.getElementById('editarProduto'),
          'deletarProduto': document.getElementById('deletarProduto')
        };

        // Esconde todas as abas
        Object.values(abas).forEach(aba => {
          if (aba) aba.style.display = 'none';
        });

        // Mostra apenas a aba ativa
        if (abas[abaAtiva]) {
          abas[abaAtiva].style.display = 'block';
          select.value = abaAtiva;
        }

        // Adiciona validação aos botões de pesquisa
        const botoesPesquisa = document.querySelectorAll('button[name="deletarProduto"], button[name="editarProduto"]');
        botoesPesquisa.forEach(botao => {
          botao.addEventListener('click', function (e) {
            const form = this.closest('form');
            const termoInput = form.querySelector('input[name="termo"]');

            if (!termoInput.value.trim()) {
              e.preventDefault(); // Impede o envio do formulário
              alert("Por favor, digite um termo para pesquisar.");
            }
          });
        });
      });

      // Funcoes de confirmaç~ao
      function confirmarDelecao() {
        return confirm("Tem certeza de que deseja deletar este produto?\nEsta ação não poderá ser desfeita.");
      }

      function confirmarCriacao() {
        return confirm("Tem certeza de que deseja cadastrar este produto?\nVerifique se todos os dados estão corretos.");
      }
    </script>
</body>