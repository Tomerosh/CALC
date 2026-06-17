const username = JSON.parse(document.getElementById('jinja-data').textContent);
const form = document.getElementById("exp-form");
form.addEventListener('submit', function (event) {
    event.preventDefault(); // Stops page refresh
    post_expression()
});

function show_profile() {
    window.location.href = `/${username}`
}

const successIcon = 'https://media.tenor.com/aGvGeHFp14kAAAAm/check-check-mark.webp'
const failIcon = 'https://media.tenor.com/aRX6P1QWSeAAAAAm/cross.webp'
const profile_link = document.getElementsByClassName('profile-link');
profile_link.onclick = show_profile
async function post_expression() {
    const formData = new FormData(form);
    const formDict = Object.fromEntries(formData.entries());
    formDict.username = username
    const response = await fetch('/solve/', {
        method: 'POST',
        body: JSON.stringify(formDict)
    })
    const res = await response.json()
    const result_box = document.getElementById("result_box");
    const solution_correct = res.score == -1? '':`<img src=${res.score==1? successIcon: failIcon}></img>`
    console.log('SCORE:', res.score)
    let result = `<h3 class='result_text'>${res.result}</h3>`
    let expression = `<h4>${res.expression}<h4>`
    let type = `<h5>Expression type: ${res.type}<h5>`
    let path = ''
    res.path.map(step => {
        path += `<div class="result_step" <span>${step.description}:</span><span>${step.expression}</span></div>`
    })
    result_box.innerHTML = solution_correct + result + expression + type + path
    

}