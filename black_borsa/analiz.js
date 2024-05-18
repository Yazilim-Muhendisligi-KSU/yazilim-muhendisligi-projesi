// İzleme listesi öğelerini seç
const hisseListesi = document.querySelectorAll('#hisse-listesi tbody tr');

// Her hisse öğesine tıklama olayını ekle
hisseListesi.forEach(hisse => {
    hisse.addEventListener('click', function(event) {
        event.preventDefault(); // Sayfanın yenilenmesini engelle

        const hisseKodu = this.querySelector('td:first-child a').getAttribute('href').split('/')[1]; // Hisse kodunu al

        // Grafik ve çizimleri göster
        showGrafikVeCizimler(hisseKodu);
    });
});

// Grafik ve çizimleri gösteren işlev
function showGrafikVeCizimler(hisseKodu) {
    // Grafik ve çizimler bölümünü seç
    const grafikCizimlerBolumu = document.getElementById('grafik-cizimler');

    // İlgili hissenin grafiği ve çizimlerini göster
    grafikCizimlerBolumu.innerHTML = `
        <h2>${hisseKodu} - Grafik ve Çizimler</h2>
        <div id="grafik">
            <!-- ${hisseKodu} hissesinin grafiği burada olacak -->
            <img src="grafikler/${hisseKodu}-grafik.png" alt="${hisseKodu} Grafiği">
        </div>
        <div id="kullanici-cizimleri">
            <!-- ${hisseKodu} hissesine yapılan çizimler burada olacak -->
            <img src="cizimler/${hisseKodu}-cizim1.png" alt="${hisseKodu} Çizim 1">
            <img src="cizimler/${hisseKodu}-cizim2.png" alt="${hisseKodu} Çizim 2">
            <!-- Eklemek istediğiniz çizimler buraya listeleyebilirsiniz -->
        </div>
    `;
}
