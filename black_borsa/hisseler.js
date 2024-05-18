// Genel hisselerin tablosunu alın
const hisselerTablosu = document.getElementById('hisseler-tablosu');
const hisseDetaylariDiv = document.getElementById('hisse-detaylari');

// Genel hisselerin bilgileri
const hisseler = [
    { kod: 'AAPL', ad: 'Apple Inc.' },
    { kod: 'GOOGL', ad: 'Alphabet Inc.' },
    { kod: 'MSFT', ad: 'Microsoft Corporation' },
    { kod: 'AMZN', ad: 'Amazon.com Inc.' },
    { kod: 'TSLA', ad: 'Tesla Inc.' },
    { kod: 'FB', ad: 'Meta Platforms Inc.' },
    { kod: 'NVDA', ad: 'NVIDIA Corporation' },
    { kod: 'JPM', ad: 'JPMorgan Chase & Co.' },
    { kod: 'V', ad: 'Visa Inc.' },
    { kod: 'JNJ', ad: 'Johnson & Johnson' }
];

// Her hisse için bir tablo satırı oluşturun
hisseler.forEach(hisse => {
    const row = document.createElement('tr');
    row.innerHTML = `<td>${hisse.kod}</td><td>${hisse.ad}</td>`;
    row.addEventListener('click', () => {
        hisseDetaylariGoster(hisse);
    });
    hisselerTablosu.querySelector('tbody').appendChild(row);
});

function hisseDetaylariGoster(hisse) {
    hisseDetaylariDiv.innerHTML = `
        <h2>${hisse.ad} (${hisse.kod})</h2>
        <div id="grafik-${hisse.kod}" class="grafik"></div>
    `;
    // Buraya hissenin grafiğini çizmek için gerekli kodları ekleyebilirsiniz
}
