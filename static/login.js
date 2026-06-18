const form = document.getElementById('login_form');

async function login() {
    const data = new URLSearchParams(new FormData(form));
    const name = document.getElementById('form-name').value
    const pass = document.getElementById('form-pass').value
    console.log(name, pass)
    let response = await fetch('/login', {
        method: 'POST',
        body: data
    })
    const status = response.status
    if (status == 200) {
        
        // response = await fetch('/solve', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify({username:name, password: pass})
        // })
        // response = await response.text()
        window.location.href = '/solve'

    }
    else if (status == 401) {
        alert('Username or password are incorrect!')
    }
}
form.addEventListener('submit', function (event) {
    event.preventDefault(); // Stops page refresh
    login()
    
});