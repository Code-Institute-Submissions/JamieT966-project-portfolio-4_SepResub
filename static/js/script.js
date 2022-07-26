console.log('hello')

// Function to make alerts disappear automatically
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);