const btn = document.querySelector("#menu-header>nav>button");


btn.addEventListener("click", function() {
    const ul = document.querySelector("#menu-header>nav>ul");

    if(ul.classList.contains("ativo")){
        ul.classList.remove("ativo")
    } else {
        ul.classList.add("ativo")
    }
})