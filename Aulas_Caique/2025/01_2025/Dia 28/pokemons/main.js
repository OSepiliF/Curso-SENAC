async function requisicao(url){
    const respostaRequisicao = await fetch(url);
    const jsonRequisicao = await (await respostaRequisicao).json();

    console.log(jsonRequisicao);

    const body = await jsonRequisicao;
    const pokemon = {
        name: body.name,
        habilidades: body.abilities,
        imagem: body.sprites.front_default
    }

    const div = document.createElement("div");
    const span = document.createElement("span");
    const img = document.createElement("img");
    
    img.src = pokemon.imagem;
    span.innerText = pokemon.habilidades[0].ability.name

    div.appendChild(img);
    div.appendChild(span);
    
    document.getElementById("pokemon").appendChild(div);

    console.log(pokemon);
}  

requisicao("https://pokeapi.co/api/v2/pokemon/10");
requisicao("https://pokeapi.co/api/v2/pokemon/12");
requisicao("https://pokeapi.co/api/v2/pokemon/14");
requisicao("https://pokeapi.co/api/v2/pokemon/16");
requisicao("https://pokeapi.co/api/v2/pokemon/18");
requisicao("https://pokeapi.co/api/v2/pokemon/20");
requisicao("https://pokeapi.co/api/v2/pokemon/22");
requisicao("https://pokeapi.co/api/v2/pokemon/24");
requisicao("https://pokeapi.co/api/v2/pokemon/26");
requisicao("https://pokeapi.co/api/v2/pokemon/28");