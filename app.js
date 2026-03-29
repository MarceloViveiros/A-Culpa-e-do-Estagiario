// Variável global O baú onde vamos guardar as vagas depois que o carteiro entregar
let todasAsVagas = []; 

// 1. O Carteiro (Apenas busca os dados e guarda no baú)
async function carregarVagas() {
    try {
        const resposta = await fetch('vagas.json?t=' + new Date().getTime());
        todasAsVagas = await resposta.json(); // Guardamos no baú global!
        
        // Agora mandamos desenhar a tela inteira pela primeira vez
        renderizarVagas(todasAsVagas); 

    } catch (erro) {
        console.error("Ops! Deu ruim:", erro);
        document.getElementById('container-vagas').innerHTML = '<p>🚨 Erro ao carregar as vagas.</p>';
    }
}

// 2. O Construtor (Apenas desenha os cards que receber na lista)
function renderizarVagas(listaDeVagas) {
    const container = document.getElementById('container-vagas');
    container.innerHTML = ''; 

    if (listaDeVagas.length === 0) {
        container.innerHTML = '<p>Nenhuma vaga encontrada para essa busca. O estagiário descansou! 😴</p>';
        return; 
    }

    listaDeVagas.forEach(vaga => {
        const card = document.createElement('div');
        card.className = 'card-vaga';
        card.innerHTML = `
            <h2>${vaga.titulo}</h2>
            <p>📍 Fonte: <strong>${vaga.repositorio}</strong></p>
            <a href="${vaga.link}" target="_blank">Acessar Vaga 🚀</a>
        `;
        container.appendChild(card);
    });
}

// 3. O Detetive do Teclado (O Filtro Mágico)
document.getElementById('input-busca').addEventListener('input', function(evento) {
    // Pegamos o que o usuário digitou e transformamos tudo em minúsculo para facilitar a busca
    const textoDigitado = evento.target.value.toLowerCase();

    // Filtramos o nosso baú global (todasAsVagas)
    const vagasFiltradas = todasAsVagas.filter(vaga => {
        const tituloMinunsculo = vaga.titulo.toLowerCase();
        // Se o título da vaga contiver o texto digitado, ele passa no filtro!
        return tituloMinunsculo.includes(textoDigitado);
    });

    // Mandamos o construtor apagar a tela e desenhar APENAS as vagas que passaram no filtro
    renderizarVagas(vagasFiltradas);
});

// Damos a ordem de partida!
carregarVagas();