  const carrossel = document.querySelector('.carrossel');
  const btnEsquerda = document.querySelector('.seta-esquerda');
  const btnDireita = document.querySelector('.seta-direita');

  function atualizarSetas() {
    btnEsquerda.disabled = carrossel.scrollLeft <= 0;
    btnDireita.disabled = Math.ceil(carrossel.scrollLeft + carrossel.clientWidth) >= carrossel.scrollWidth;
    btnEsquerda.style.opacity = btnEsquerda.disabled ? '0.4' : '1';
    btnDireita.style.opacity = btnDireita.disabled ? '0.4' : '1';
    
  }

  btnDireita.addEventListener('click', () => {
    carrossel.scrollBy({ left: 300, behavior: 'smooth' });
  });

  btnEsquerda.addEventListener('click', () => {
    carrossel.scrollBy({ left: -300, behavior: 'smooth' });
  });

  carrossel.addEventListener('scroll', () => {
    window.requestAnimationFrame(atualizarSetas);
  });
  
  atualizarSetas()