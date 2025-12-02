<!DOCTYPE html>
<html lang="pt-BR">

<head>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="static/estiloPerfilUser.css">
  <link rel="icon" type="image/png" href="static/imagens/vinil.png">
  <title>Disco 2000</title>
</head>

<body>
  <div class="cabeçalho">
    <header>
      <nav>
        <ul>
          <li><a href="/"><img src='static/imagens/Logo cortada.png' class="logo"></a></li>
          <li><a href="/Catálogo" class="Catálogo">Catálogo</a></li>
          <li><a href="views/premium.tpl" class="Premium">Premium</a></li>
          <li><a href="/Sobre" class="Sobre">Sobre</a></li>
          <li><a href="/Favoritos" class="IconFav"><img src="static/imagens/heart.png"></a></li>
          <li><a href="/Carrinho" class="IconShop"><img src="static/imagens/shopping-cart.png"></a></li>
          <li><a href="/Perfil" class="IconPerfil"><img src="static/imagens/circle-user.png"></a></li>
        </ul>
      </nav>
      <hr class="linha">
    </header>
  </div>

  <section class="informaçõesPessoais">
    <h1>Perfil</h1>
    <form method="POST" action="/Usuario">
      <div class="blocoPerfil">

      <h2>Informações Pessoais</h2>
      <div class="caixa"><input class="texto" type="text" placeholder="Email" name="email" value="{{usuario['email'] or ''}}">
      </div>
      <div class="caixa"><input class="texto" type="text" placeholder="Telefone" name="telefone"  value="{{usuario['telefone'] or ''}}">
      </div>

      <div class="linhaDupla">
        <div class="caixaMetade1"><input class="texto" type="text" name="nome"  placeholder="Nome..."
            value="{{usuario['primeiroNome'] or ''}}"></div>
        <div class="caixaMetade2"><input class="texto" type="text" name="sobrenome" placeholder="Sobrenome..."
            value="{{usuario['segundoNome'] or ''}}"></div>
      </div>

      <div class="linhaDupla">
        <div class="caixaMetade1">
          <select name="País" class="seletor">
            <option value="" disabled selected>País</option>
            <option value="opcao1">Brasil</option>
          </select>
        </div>
        <div class="caixaMetade2"><input class="texto" type="number" placeholder="CEP..."></div>
      </div>

      <div class="linhaDupla">
        <div class="caixaMetade1">
          <select name="Estado" class="seletor">
            <option value="" disabled selected>Estado</option>
            <option value="opcao1">Distrito Federal</option>
            <option value="opcao2">São Paulo</option>
            <option value="opcao3">Rio de Janeiro</option>
          </select>
        </div>
        <div class="caixaMetade2"><input class="texto" type="text" placeholder="Cidade"></div>
      </div>

      <div class="caixa"><input class="texto" type="text" placeholder="Endereço..."></div>

      <div class="linhaDupla">
        <div class="caixaMetade1"><input class="texto" type="number" placeholder="Número..."></div>
        <div class="caixaMetade2"><input class="texto" type="text" placeholder="Complemento..."></div>
      </div>
      </div>
      <div class="containerBotao">
      <button type="submit" class="botao" name="acao" value="salvar">Salvar</button>
      <button type="submit" class="botao" name="acao" value="excluir">Excluir</button>
      <button type="submit" class="botao" name="acao" value="sair">Sair</button>
      </div>
    </form>
  </section>

  <section class="footer">
    <img src="static/imagens/logo disco 2000.png" class="logoFooter" alt="Disco 2000">
    <p>© 2025 Disco 2000, Rua Penny Lane, nº 33⅓ - Paradise City</p>
  </section>

</body>

</html>