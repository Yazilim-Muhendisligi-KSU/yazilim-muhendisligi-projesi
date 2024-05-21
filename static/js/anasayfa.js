
/*
document.addEventListener('DOMContentLoaded', function () {
    // Yükselen Hisseler tablosunu doldur
    const yükselenHisseler = [
        { symbol: 'XYZ', lastPrice: '50.00', change: '+2.5%' },
        { symbol: 'ABC', lastPrice: '75.20', change: '+1.8%' },
        { symbol: 'DEF', lastPrice: '42.80', change: '+1.2%' },
        { symbol: 'GHI', lastPrice: '30.50', change: '+0.9%' },
        { symbol: 'JKL', lastPrice: '18.60', change: '+0.5%' }
    ];
    const yükselenHisselerTablosu = document.getElementById('yükselen-hisseler-tablosu');
    yükselenHisseler.forEach(hisse => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${hisse.symbol}</td><td>${hisse.lastPrice}</td><td>${hisse.change}</td>`;
        yükselenHisselerTablosu.querySelector('tbody').appendChild(row);
    });

    // Düşen Hisseler tablosunu doldur
    const düşenHisseler = [
        { symbol: 'MNO', lastPrice: '22.40', change: '-2.3%' },
        { symbol: 'PQR', lastPrice: '37.80', change: '-1.5%' },
        { symbol: 'STU', lastPrice: '45.60', change: '-1.0%' },
        { symbol: 'VWX', lastPrice: '55.20', change: '-0.7%' },
        { symbol: 'YZA', lastPrice: '62.80', change: '-0.3%' }
    ];
    const düşenHisselerTablosu = document.getElementById('düşen-hisseler-tablosu');
    düşenHisseler.forEach(hisse => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${hisse.symbol}</td><td>${hisse.lastPrice}</td><td>${hisse.change}</td>`;
        düşenHisselerTablosu.querySelector('tbody').appendChild(row);
    });

    // Dinamik Tabloyu doldur
    const dinamikTablo = [
        { symbol: 'MNDR', prevClose: '6.95', open: '6.94', lastPrice: '6.95', change: '-1.00%', low: '6.9', high: '7.05' }
    ];
    const dinamikTabloTablosu = document.getElementById('dinamik-tablo');
    dinamikTablo.forEach(hisse => {
        const row = document.createElement('tr');
        row.innerHTML = `<td>${hisse.symbol}</td><td>${hisse.prevClose}</td><td>${hisse.open}</td><td>${hisse.lastPrice}</td><td>${hisse.change}</td><td>${hisse.low}</td><td>${hisse.high}</td>`;
        dinamikTabloTablosu.querySelector('tbody').appendChild(row);
    });
});
*/
/*
document.addEventListener('DOMContentLoaded', function () {
    // Kullanıcıya ilişkin hisse senedi bilgileri
    var kullaniciHisseleri = [
        { symbol: "XYZ", lastPrice: 50.00, change: "+2.5%" },
        { symbol: "ABC", lastPrice: 75.20, change: "+1.8%" },
        // Diğer hisseler buraya eklenebilir
    ];

    // Kullanıcıya ilişkin hisse senedi bilgilerini kullanarak bildirim gösterme fonksiyonu
    function showNotification() {
        var hisse = kullaniciHisseleri[Math.floor(Math.random() * kullaniciHisseleri.length)]; // Rastgele bir hisse seç
        var notification = new Notification("Yeni bildirim", {
            body: "Seçili hisseniz (" + hisse.symbol + ") son fiyatı: " + hisse.lastPrice + ", değişim: " + hisse.change,
            icon: "pic/notification-icon.png" // Opsiyonel, bildirimde gösterilecek ikon
        });

        // Bildirime tıklandığında sayfaya odaklan
        notification.onclick = function () {
            window.focus();
            notification.close();
        };
    }

    // Sayfa yüklendiğinde bildirimi göster
    showNotification();
});
*/





  