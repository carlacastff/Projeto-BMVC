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