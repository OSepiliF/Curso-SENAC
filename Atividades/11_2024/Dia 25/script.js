function validar_botao() {
    const inputNome = document.querySelector('.input_nome_required');
    const inputSenha = document.querySelector('.input_senha_required');
    const inputConfirmarSenha = document.querySelector('.input_confirm_senha_required');

    // Validação do Nome
    if (inputNome.value.length <= 3) {
        document.querySelector('.span-nome-required').style.display = 'block';
        document.querySelector('.span-nome-valid').style.display = 'none';
    } 
    if (inputNome.value === inputSenha.value) {
        document.querySelector('.span-nome-required').style.display = 'none';
        document.querySelector('.span-nome-valid').style.display = 'none';
        document.querySelector('.span-nome-senha-iguais').style.display = 'block';
    }

    else  {
        document.querySelector('.span-nome-required').style.display = 'none';
        document.querySelector('.span-nome-valid').style.display = 'block';
    }

    // Validação da Senha
    if (inputSenha.value.length < 6) {
        document.querySelector('.span-senha-required').style.display = 'none';
        document.querySelector('.span-senha-required').style.display = 'block';
        document.querySelector('.span-senha-valid').style.display = 'none';
    } 
    else if (inputNome.value === inputSenha.value) {
        document.querySelector('.span-senha-required').style.display = 'none';
        document.querySelector('.span-senha-valid').style.display = 'none';
        document.querySelector('.span-nome-senha-iguais').style.display = 'block';
    } 
    else {
        document.querySelector('.span-senha-required').style.display = 'none';
        document.querySelector('.span-senha-valid').style.display = 'block';
    }

    // Validação da Confirmar Senha
    if (inputSenha.value !== inputConfirmarSenha.value) {
        document.querySelector('.span-confirm-senha-required').style.display = 'block';
        document.querySelector('.span-confirm-senha-valid').style.display = 'none';
    } 
    else {
        document.querySelector('.span-confirm-senha-required').style.display = 'none';
        document.querySelector('.span-confirm-senha-valid').style.display = 'block';
    }

    // Verifica se o nome é igual à senha e exibe a mensagem apropriada
    if (inputNome.value === inputSenha.value) {
        document.querySelector('.span-nome-senha-iguais').style.display = 'block';
    } 
    else {
        document.querySelector('.span-nome-senha-iguais').style.display = 'none';
    }
}
