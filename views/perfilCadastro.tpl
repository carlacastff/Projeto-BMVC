<!DOCTYPE html>
<html lang="pt-BR">

<head>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="static/estiloPerfilCadastro.css">
  <link rel="icon" type="image/png" href="static/imagens/vinil.png">
  <title>Disco 2000</title>
</head>

<body>

  <!-- Cabeçalho -->
  <div class="cabeçalho">
    <header>
      <nav>
        <ul>
          <li><a href="/"><img src='/static/imagens/Logo cortada.png' class="logo"></a></li>
          <li><a href="/Catálogo" class="Catálogo">Catálogo</a></li>
          <li><a href="/Premium" class="Premium">Premium</a></li>
          <li><a href="/Sobre" class="Sobre">Sobre</a></li>
          <li><a href="/Favoritos" class="IconFav"><img src="/static/imagens/heart.png"></a></li>
          <li><a href="/Carrinho" class="IconShop"><img src="/static/imagens/shopping-cart.png"></a></li>
          <li><a href="/Perfil" class="IconPerfil"><img src="/static/imagens/circle-user.png"></a></li>
        </ul>
      </nav>
      <hr class="linha">
    </header>
  </div>

  <!-- Título -->
  <section class="título">
    <h1>Cadastrar</h1>
  </section>

  <!--Formulario de Criar conta-->
  <section class="Cadastro">
    <form method="POST" action="/Cadastro">

      <label>Email:</label>
      <input type="text" name="email" placeholder="Email" required>

      <label>Nome:</label>
      <input type="text" name="nome" placeholder="Nome" required>

      <label>Sobrenome:</label>
      <input type="text" name="sobrenome" placeholder="Sobrenome" required>

      <label>Telefone:</label>
      <input type="text" name="telefone" placeholder="Telefone (opcional)" id="telefone"
        onkeyup="validarTelefone('telefone')">
      <span id="erroTelefone" style="color: red; font-size: 12px; display: none;">Digite um telefone válido</span>


      <div class="containerDaSenha">
        <label>Senha:</label>
        <div class="dentroSenha">
          <input type="password" name="senha" placeholder="Senha" id="senha1" required onkeyup="validarSenhas()">
          <div id="icon1" onclick="mostrar('senha1', 'icon1')"></div>
        </div>
      </div>

      <div class="containerDaSenha">
        <label>Confirmar senha:</label>
        <div class="dentroSenha">
          <input type="password" name="confirmar_senha" placeholder="Confirmar Senha" id="senha2" required
            onkeyup="validarSenhas()">
          <div id="icon2" onclick="mostrar('senha2', 'icon2')"></div>
        </div>
        <span id="erroSenha" style="color: red; font-size: 12px; display: none;">As senhas não coincidem</span>
      </div>
      <button type="submit" class="botao">Cadastrar-se</button>
      <div>
        <p>Já possui um cadastro?</p>
        <a href="/Login">Faça login.</a> <!--Leva para cadastro-->
      </div>
    </form>
  </section>
  <script src="/static/jsCadastro.js"></script>

  <section class="footer">
    <img src="static/imagens/logo disco 2000.png" class="logoFooter" alt="Disco 2000">
    <p>© 2025 Disco 2000, Rua Penny Lane, nº 33⅓ - Paradise City</p>
  </section>

</body>