function validarSenhas() {
    const senha1 = document.getElementById('senha1').value;
    const senha2 = document.getElementById('senha2').value;
    const erro = document.getElementById('erroSenha');
    const botao = document.querySelector('.botao');
    
    if (senha2 === "") {
        erro.style.display = 'none';
        botao.disabled = false;
    } else if (senha1 !== senha2) {
        erro.style.display = 'block';
        botao.disabled = true;
    } else {
        erro.style.display = 'none';
        botao.disabled = false;
    }
}

function validarTelefone(inputId){
    const input = document.getElementById(inputId);
    const telefone = input.value;
    const erro = document.getElementById('erroTelefone');
    const botao = document.querySelector('.botao');
    
    // Remove tudo que não é número
    const apenasNumeros = telefone.replace(/\D/g, '');
    
    if (apenasNumeros && (apenasNumeros.length > 11 || apenasNumeros.length < 9)) {
        erro.style.display = 'block';
        botao.disabled = true;
    } else {
        erro.style.display = 'none';
        botao.disabled = false;
    }
}

document.querySelector('form').addEventListener('submit', function(e) {
    const senha1 = document.getElementById('senha1').value;
    const senha2 = document.getElementById('senha2').value;
    
    if (senha1 !== senha2) {
        e.preventDefault();
        alert('As senhas não coincidem!');
        return false;
    }
    return true;
});

function mostrar(senhaId, iconId){
    const senha = document.getElementById(senhaId);
    const icon = document.getElementById(iconId);

    if(senha.type === 'password'){
        senha.type = 'text';
        icon.classList.add('hide');
    } else {
        senha.type = 'password';
        icon.classList.remove('hide');
    }
}