var socket = io.connect('http://198.168.1.115:5000');

socket.emit('join', {user_id: 1});  // Example user

function sendMessage() {
    var message = document.getElementById('message').value;
    socket.emit('send_message', {
        sender_id: 1,
        receiver_id: 2,
        message: message
    });
}

socket.on('send_message', function(data) {
    console.log("New message:", data.message);
});

