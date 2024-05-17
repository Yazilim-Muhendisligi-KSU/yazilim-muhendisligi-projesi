document.addEventListener('DOMContentLoaded', function() {
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

   
    // İzleme listesini al
    document.getElementById('getWatchlistButton').addEventListener('click', function() {
        const userId = document.getElementById('user_id').value;
        fetch('{% url "accounts:get_watchlist" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ user_id: userId })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = JSON.stringify(data);
        })
        .catch(error => console.error('Error:', error));
    });

    // İzleme listesine ekle
    document.getElementById('addToWatchlistButton').addEventListener('click', function() {
        const userId = document.getElementById('user_id').value;
        const stockSymbol = prompt("Enter stock symbol to add to watchlist:");
        fetch('{% url "accounts:add_to_watchlist" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ user_id: userId, stock_symbol: stockSymbol })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = data.message || data.error;
        })
        .catch(error => console.error('Error:', error));
    });

    // İzleme listesinden çıkar
    document.getElementById('removeFromWatchlistButton').addEventListener('click', function() {
        const userId = document.getElementById('user_id').value;
        const stockSymbol = prompt("Enter stock symbol to remove from watchlist:");
        fetch('{% url "accounts:remove_from_watchlist" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ user_id: userId, stock_symbol: stockSymbol })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = data.message || data.error;
        })
        .catch(error => console.error('Error:', error));
    });

    // Çizimleri al
    document.getElementById('getDrawingButton').addEventListener('click', function() {
        const userId = document.getElementById('user_id').value;
        fetch('{% url "accounts:get_drawing" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ user_id: userId })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = data.message || data.error;
        })
        .catch(error => console.error('Error:', error));
    });

    // Çizim ekle
    document.getElementById('addDrawingButton').addEventListener('click', function() {
        const userId = document.getElementById('user_id').value;
        const stockSymbol = prompt("Enter stock symbol for the drawing:");
        const drawingData = prompt("Enter drawing data:");
        fetch('{% url "accounts:add_drawing" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ user_id: userId, stock_symbol: stockSymbol, data: drawingData })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = data.message || data.error;
        })
        .catch(error => console.error('Error:', error));
    });

    // Çizim sil
    document.getElementById('removeDrawingButton').addEventListener('click', function() {
        const userId = document.getElementById('user_id').value;
        const stockSymbol = prompt("Enter stock symbol for the drawing to remove:");
        const drawingData = prompt("Enter drawing data to remove:");
        fetch('{% url "accounts:remove_drawing" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ user_id: userId, stock_symbol: stockSymbol, data: drawingData })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = data.message || data.error;
        })
        .catch(error => console.error('Error:', error));
    });
    //bildirim al 
    document.getElementById('getNotificationsButton').addEventListener('click', function() {
        const userId = document.getElementById('user_id').value;
        fetch('{% url "accounts:get_notifications" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ user_id: userId })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = JSON.stringify(data);
        })
        .catch(error => console.error('Error:', error));
    });

    // Bildirim ekle
    document.getElementById('addNotificationButton').addEventListener('click', function() {
        const userId = document.getElementById('user_id').value;
        const notificationMessage = prompt("Enter notification message:");
        fetch('{% url "accounts:add_notification" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ user_id: userId, message: notificationMessage })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = data.message || data.error;
        })
        .catch(error => console.error('Error:', error));
    });

    // Bildirim sil
    document.getElementById('removeNotificationButton').addEventListener('click', function() {
        const userId = document.getElementById('user_id').value;
        const notificationId = prompt("Enter notification ID to remove:");
        fetch('{% url "accounts:remove_notification" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ user_id: userId, notification_id: notificationId })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerText = data.message || data.error;
        })
        .catch(error => console.error('Error:', error));
    });

});
