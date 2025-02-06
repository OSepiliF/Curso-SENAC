fetch("./dados.json").then(function(resposta){
    return resposta.json()
}).then(function(json){
    const divPesssoa = document.createElement("div")
    const paragrafo = document.createElement("p")

    const frase = `Meu nome é ${json.nome}, tenho ${json.idade} anos de idade e sou ${json.profissao}`;

    paragrafo.innerText = frase

    divPesssoa.appendChild(paragrafo);

    document.getElementById('app').appendChild(divPesssoa); 
})