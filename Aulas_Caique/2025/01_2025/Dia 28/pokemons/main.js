let nextUrl = "https://pokeapi.co/api/v2/pokemon?limit=14&offset=0"; 
let prevUrl = null;

async function requisicao(url) {
    const respostaRequisicao = await fetch(url);
    const jsonRequisicao = await respostaRequisicao.json();

    document.getElementById("pokemon").innerHTML = "";

    nextUrl = jsonRequisicao.next;
    prevUrl = jsonRequisicao.previous;

    for (let pokemonData of jsonRequisicao.results) {
        const pokemonResponse = await fetch(pokemonData.url);
        const pokemonJson = await pokemonResponse.json();

        const pokemon = {
            id: pokemonJson.id, 
            name: pokemonJson.name,
            habilidades: pokemonJson.abilities,
            tipo: pokemonJson.types.map(tipo => tipo.type.name).join(', '), 
            imagem: pokemonJson.sprites.front_default
        };

        const div = document.createElement("div");
        div.classList.add("pokemon-card");

        const nome = document.createElement("h3");
        nome.innerText = pokemon.name;

        const img = document.createElement("img");
        img.src = pokemon.imagem;

        const idDiv = document.createElement("div"); 
        idDiv.innerText = `ID: ${pokemon.id}`;

        const tipoDiv = document.createElement("div");
        tipoDiv.innerText = `Tipo: ${pokemon.tipo}`;

        const habilidadesDiv = document.createElement("div");
        habilidadesDiv.innerText = "Habilidades: ";

        pokemon.habilidades.forEach(abilities => {
            const span = document.createElement("span");
            span.innerText = abilities.ability.name;
            habilidadesDiv.appendChild(span);
        });

        div.appendChild(idDiv); 
        div.appendChild(nome);
        div.appendChild(img);
        div.appendChild(habilidadesDiv);
        div.appendChild(tipoDiv);

        document.getElementById("pokemon").appendChild(div);
    }
}

document.getElementById("proxima-btn").addEventListener("click", () => {
    if (nextUrl) {
        requisicao(nextUrl); 
    }
});

document.getElementById("voltar-btn").addEventListener("click", () => {
    if (prevUrl) {
        requisicao(prevUrl); 
    }
});

document.getElementById("search-button").addEventListener("click", () => {
    const input = document.getElementById("pokemon-input").value.toLowerCase();
    const url = `https://pokeapi.co/api/v2/pokemon/${input}`; 
    requisicao(url); 
});

requisicao(nextUrl);