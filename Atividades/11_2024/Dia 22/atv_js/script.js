function atividade_1() {
    var temp_F = window.prompt('Qual é a temperatura em Fahrenheit? ')
    temp_C = (5/9) * (temp_F - 32)
    window.alert("Temperatura em Celcius: " + temp_C.toFixed(2) + "°")
}

function atividade_2() {
    var nome_produto = window.prompt('Digite o nome do produto: ')
    var quant_comprada = window.prompt('Digite a quantidade comprada do produto: ')
    var valor_unit = window.prompt('Digite o valor unitário do produto comprado: ')
    var porcent_desconto = window.prompt('Digite o desconto: ')

    valor_total = (quant_comprada * valor_unit) * (1 - (porcent_desconto / 100)) 

    window.alert(`
    - Produto: ${nome_produto}
    - ${quant_comprada} x R$${valor_unit} = R$${(quant_comprada * valor_unit).toFixed(2)}
    - R$${valor_unit} com o desconto de ${porcent_desconto}% = R$${valor_total.toFixed(2)}
    `);
}

function atividade_3() {
    var valor_reais = window.prompt('Digite o valor em reais da compra: ')
    var valor_dolar = window.prompt('Digite a cotação atual do dólar: ')

    valor_equivalente = valor_reais / valor_dolar

    window.alert(`Valor em dólar fica: ${valor_equivalente.toFixed(2)}`)
}