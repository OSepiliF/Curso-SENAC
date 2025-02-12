const container = document.querySelector('.container');
const slides = document.querySelectorAll('.slide');
const prev = document.getElementById('prev');
const next = document.getElementById('next');

let index = 0;

// Função para atualizar o carrossel
function updateCarousel() {
    container.style.transform = `translateX(${-index * 300}px)`;
}

// Avançar automaticamente a cada 3 segundos
function autoPlay() {
    index = (index + 1) % slides.length;
    updateCarousel();
}

// Botões de navegação manual
next.addEventListener('click', () => {
    index = (index + 1) % slides.length;
    updateCarousel();
    resetAutoPlay();
});

prev.addEventListener('click', () => {
    index = (index - 1 + slides.length) % slides.length;
    updateCarousel();
    resetAutoPlay();
});

// Iniciar autoplay
let autoSlide = setInterval(autoPlay, 3000);

// Resetar o autoplay quando o usuário clicar
function resetAutoPlay() {
    clearInterval(autoSlide);
    autoSlide = setInterval(autoPlay, 3000);
}
