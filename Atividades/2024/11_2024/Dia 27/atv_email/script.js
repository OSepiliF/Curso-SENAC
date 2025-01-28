function validar_botao() {
    const emailInput = document.querySelector('#emailInput');
    const errorSpan = document.querySelector('.span-required');
    const successSpan = document.querySelector('.span-valid'); 
    const emailPattern = /^[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z.]{2,}$/;

    if (emailPattern.test(emailInput.value)) {
        removeError();
    } else {
        setError();
    }
}

function emailValidate() {
    const emailInput = document.querySelector('#emailInput');
    const errorSpan = document.querySelector('.span-required');
    const successSpan = document.querySelector('.span-valid'); 
    const emailPattern = /^[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z.]{2,}$/;

    if (emailPattern.test(emailInput.value)) {
        removeError();
    } else {
        setError();
    }
}

function setError() {
    const errorSpan = document.querySelector('.span-required');
    errorSpan.style.display = 'block';
    errorSpan.style.color = 'red';

    const successSpan = document.querySelector('.span-valid');
    successSpan.style.display = 'none';
}

function removeError() {
    const errorSpan = document.querySelector('.span-required');
    errorSpan.style.display = 'none';

    const successSpan = document.querySelector('.span-valid');
    successSpan.style.display = 'block';
    successSpan.style.color = 'green';
}
