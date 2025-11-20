document.addEventListener("DOMContentLoaded", () => {
  // Controle dos campos de disco
  const tipoSelect = document.getElementById("tipoProd");
  const camposDiscos = document.querySelectorAll(".disco");
  
  function atualizarCampos() {
    const tipo = tipoSelect.value;
    camposDiscos.forEach(campo => {
      if (tipo === "vitrola" || tipo === "acessorio") {
        campo.style.display = "none";
      } else {
        campo.style.display = "block";
      }
    });
  }

  tipoSelect.addEventListener("change", atualizarCampos);
  atualizarCampos(); // ativa ao iniciar

  // Controle das abas
  const select = document.getElementById("selecionarOp");
  const forms = {
    criarProduto: document.getElementById("adicionarProduto"),
    editarProduto: document.getElementById("editarProduto"),
    deletarProduto: document.getElementById("deletarProduto"),
  };

  // Função para mostrar uma aba específica
  function mostrarAba(escolha) {
    // Esconde todas as abas
    Object.values(forms).forEach(f => {
      if (f) f.style.display = "none";
    });

    // Mostra só o escolhido
    if (forms[escolha]) {
      forms[escolha].style.display = "block";
    }
  }

  // Event listener para mudança no select
  select.addEventListener("change", () => {
    const escolha = select.value;
    mostrarAba(escolha);
  });

});

// FUNÇÕES DE CONFIRMAÇÃO (adicionadas ao jsAdmin.js)
function confirmarDelecao() {
  return confirm("Tem certeza de que deseja deletar este produto?\nEsta ação não poderá ser desfeita.");
}

function confirmarCriacao() {
  return confirm("Tem certeza de que deseja cadastrar este produto?\nVerifique se todos os dados estão corretos.");
}

function confirmarEdicao() {
  return confirm("Tem certeza de que deseja salvar as alterações?\nVerifique se todos os dados estão corretos.");
}

function confirmarPesquisa() {
  const termo = document.querySelector('input[name="termo"]').value;
  if (!termo.trim()) {
    alert("Por favor, digite um termo para pesquisar.");
    return false;
  }
  return true;
}

function confirmarEdicao() {
  return confirm("Tem certeza de que deseja salvar as alterações?\nVerifique se todos os dados estão corretos.");
}