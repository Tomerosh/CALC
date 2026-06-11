// const form = document.getElementById('login_form');

// async function login() {
//     const data = new URLSearchParams(new FormData(form));
//     const name = document.getElementById('form-name').value
//     const pass = document.getElementById('form-pass').value
//     console.log(name, pass)
//     const response = await fetch('/login', {
//         method: 'POST',
//         body: data
//     })
//     const result = await response
//     if (result.ok) {
        
//         const response = await fetch('/solve', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({username:name, password: pass})
//         })
//         html = await response.text()
//         document.getElementById('content-container').innerHTML = html;

//     }
// }
// form.addEventListener('submit', function (event) {
//     event.preventDefault(); // Stops page refresh
//     login()
    
// });