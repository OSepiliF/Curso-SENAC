// ============================================
// Prompt e Concatenar
// ============================================

// var nome = window.prompt('Qual seu nome? ')

// Concatenar com + e template literals
console.log(`Meu nome é ` + nome)
console.log(`Meu nome é ${nome}`)
window.alert('Olá ' + nome + ' seja bem-vindo!')

// ============================================
// Operadores Aritméticos
// ============================================

let t = 10;
let y = 5;
console.log(t + y)  // Soma
console.log(t - y)  // Subtração
console.log(t * y)  // Multiplicação
console.log(t / y)  // Divisão
console.log(t % y)  // Módulo (resto da divisão)

// ============================================
// Operadores Lógicos
// ============================================

// "&&" == and
// "||" == or
// "!" == not

let a = true;
let b = false;
console.log(a && b)  // AND
console.log(a || b)  // OR
console.log(!a)      // NOT

// ============================================
// Operadores Ternários
// ============================================

// Sintaxe: condição ? valor_se_verdadeiro : valor_se_falso
var media = 8;
var resultado = media >= 7 ? 'Aprovado' : 'Reprovado';
console.log(resultado)

// ============================================
// Saídas
// ============================================

// Usando document.write para saída em página
document.write('Olha a data aí: ')
document.write(Date())

// Outros tipos de saída
window.alert('Um alerta')
console.log('Ta aqui')

// ============================================
// Métodos de String
// ============================================

// String.length - Comprimento da string
// String.charAt(0) - Retorna o caractere no índice especificado
// String.slice(1,7) - Fatia a string de índice 1 até 7
// String.toUpperCase() - Converte a string para maiúsculas
// String.toLowerCase() - Converte a string para minúsculas

let str = "JavaScript";
console.log(str.length)
console.log(str.charAt(0))
console.log(str.slice(1, 7))
console.log(str.toUpperCase())
console.log(str.toLowerCase())

// ============================================
// Funções
// ============================================

// Função simples de multiplicação
function myFunction(p1, p2) {
    return p1 * p2
}
let x = myFunction(10, 20);
console.log(x)

// ============================================
// Seleção de Elementos
// ============================================

// Alterando o estilo de um parágrafo
window.onload = function() {
    var p1 = window.document.getElementsByTagName('p')[1];
    p1.style.background = 'blue';
    p1.innerHTML = 'Teste';
}

// ============================================
// Eventos HTML
// ============================================

// Função que altera conteúdo e estilo ao clicar
function a() {
    var a = window.document.getElementById('a');
    a.innerText = 'Certa Resposta';
    a.style.backgroundColor = 'green';
}

// ============================================
// Expressões Regulares
// ============================================

// Exemplos de expressões regulares
// Testes com expressões regulares
document.write(/[az]/i.test("AZ"));
document.write('<br>');
document.write(/love/i.test('LovE'));
document.write('<br>');
document.write(/[\bx]/.test('123x'));
document.write('<br>');
document.write(/\s/.test(' w'));

document.write('<p>Dia: ');
var dia = /^(0[1-9]|1[0-9]|2[0-9]|3[0-1])$/;
document.write(dia.test("32"));  // Testa dia inválido

document.write('<br>Mês: ');
var mes = /^(0[1-9]|1[0-2])$/;
document.write(mes.test("12"));  // Testa mês válido

document.write('<br>Ano: ');
var ano = /^\d{4}$/;
document.write(ano.test("24"));  // Testa ano inválido

document.write('<br>Data: ');
var data = /^(0[1-9]|1[0-9]|2[0-9]|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}$/;
document.write(data.test("22/12/2120"));  // Testa data válida

document.write('<p>CPF: ');
var cpf = /^([0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2})$/;
document.write(cpf.test('957.877.555-55'));  // Testa CPF válido

document.write('<p>Email: ');
var email = /^[a-zA-Z0-9._%+-]+\@[a-zA-Z0-9.-]+\.[a-zA-Z.]{2,}$/;
document.write(email.test('exemplo@email.com'));  // Testa email válido
