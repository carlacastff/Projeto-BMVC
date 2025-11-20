<!DOCTYPE html>
<html lang="pt-BR">

<head>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="static/estiloLandingPage.css">
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

  <section class="pesquisa">
    <div class="retangulo"></div>
    <img src="static/imagens/disco tocando.png" class="discoTocando" alt="Vinil tocando">
    <img src="static/imagens/linha.png" class="linhaLogo">
    <p class="textoPesquisa1">O verdadeiro som tem rotação.</p>

    <div class="searchBarra">
      <input type="text" class="pesquisaLiteral" placeholder="O que você quer escutar hoje?">
      <button class="botãoPesquisa">
        <img src="static/imagens/search.png" alt="Pesquisar">
      </button>
    </div>
  </section>

  <section class="maisVendidos">
  <p class="textoVendas">Mais Vendidos</p>
  <div class="vitrineVendidos">
    <a href="#" class="card-vendido">
      <div class="retanguloMaisVendidos"><img src="static/imagens/logo vinil.png" alt="Disco 1"></div>
    </a>
    <a href="#" class="card-vendido">
      <div class="retanguloMaisVendidos"><img src="static/imagens/logo vinil.png" alt="Disco 2"></div>
    </a>
    <a href="#" class="card-vendido">
      <div class="retanguloMaisVendidos"><img src="static/imagens/logo vinil.png" alt="Disco 3"></div>
    </a>
  </div>
</section>


  <section class="bannerPremium">
    <div class="conteudoPremium">
      <div class="vinilDecorativo"></div>
      <h2 class="tituloPremium">Descubra o prazer de ouvir o passado no presente</h2>
      <p class="textoPremium">
        Assine o plano <span>Disco 2000 Premium</span> e receba, todo mês, um vinil raro direto na sua casa.
      </p>
      <button class="botaoAssine">Quero ser Premium</button>
    </div>
  </section>

 <section class="generos">
  <h2>Gêneros</h2>
  <div class="carrossel-container">
    <button class="seta seta-esquerda"><img src="static/imagens/arrow-small-left.png"></button>

    <div class="carrossel">
      <div class="card-genero"><img src="static/imagens/Catálogo/Discos de Vinil/rock/Abbey Road - The Beatles.jpg" alt="Rock"><p>Rock</p></div>
      <div class="card-genero"><img src="static/imagens/Catálogo/Discos de Vinil/pop/Thriller - Michael Jackson.jpg" alt="Pop"><p>Pop</p></div>
      <div class="card-genero"><img src="static/imagens/Catálogo/Discos de Vinil/Hip-Hop & R&B/Greatest Hits - 2Pac.jpg" alt="Hip Hop"><p>Hip Hop & R&B</p></div>
      <div class="card-genero"><img src="static/imagens/Catálogo/Discos de Vinil/festivos/Merry Christmas - Mariah Carey.jpg" alt="Festivo"><p>Festivo</p></div>
      <div class="card-genero"><img src="static/imagens/Catálogo/Discos de Vinil/nacional/Tim Maia 1973 - Tim Maia.jpg" alt="Nacional"><p>Nacional</p></div>
      <div class="card-genero"><img src="static/imagens/Catálogo/Discos de Vinil/jazz/Come Fly With Me - Frank Sinatra.jpg" alt="Jazz"><p>Jazz</p></div>
      <div class="card-genero"><img src="static/imagens/Catálogo/Discos de Vinil/soundtracks/Senhor dos Anéis - Howard Shore.jpg" alt="Soundtrack"><p>Soundtrack</p></div>
    </div>

    <button class="seta seta-direita"><img src="static/imagens/arrow-small-right.png"></button>
    <script src="static/jsLandingPage.js"></script>
  </div>
</section>

<section class="footer">
  <img src="static/imagens/logo disco 2000.png" class="logoFooter" alt="Disco 2000">
  <p>© 2025 Disco 2000, Rua Penny Lane, nº 33⅓ - Paradise City</p>
</section>
  <script src="static/jsCatálogo.js"></script>
</body>
</html>
