// const username = JSON.parse(document.getElementById('jinja-data').textContent);
const logs = JSON.parse(document.getElementById('jinja-data').textContent);
console.log('LOGS:', logs)




// const form = document.getElementById("exp-form");
// form.addEventListener('submit', function (event) {
//     event.preventDefault(); // Stops page refresh
//     post_expression()
// });

// function show_profile() {
//     window.location.href = `/${username}`
// }
// const profile_link = document.getElementsByClassName('profile-link');
// profile_link.onclick = show_profile
// async function post_expression() {
//     const data = new URLSearchParams(new FormData(form));
//     const response = await fetch('/solve/', {
//         method: 'POST',
//         body: data
//     })
//     const res = await response.json()
//     const result_box = document.getElementById("result_box");
//     console.log(res)
//     let result = `<h3 class='result_text'>${res.result}</h3>`
//     let expression = `<h4>${res.expression}<h4>`
//     let type = `<h5>Expression type: ${res.type}<h5>`
//     let path = ''
//     res.path.map(step => {
//         path += `<div class="result_step" <span>${step.description}</span><span> = </span><span>${step.expression}</span></div>`
//     })
//     result_box.innerHTML = result + expression + type + path
    

// }