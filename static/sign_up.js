const form = document.getElementById('sign-form');

async function register() {
    const data = new URLSearchParams(new FormData(form));
    const name = document.getElementById('form-name').value
    const pass = document.getElementById('form-pass').value
    console.log(name, pass)
    const response = await fetch('/sign_up', {
        method: 'POST',
        body: data
    })
    const status = response.status
    console.log(status)
    if (status == 201) {
        alert('User created successfuly!')
        window.location.href = `/`
    }
    if (status == 409) {
        alert('User already taken!')
    }
}
form.addEventListener('submit', function (event) {
    event.preventDefault(); // Stops page refresh
    register()
    
});