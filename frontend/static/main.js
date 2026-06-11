
const form = document.getElementById("exp-form");

form.addEventListener('submit', function (event) {
    event.preventDefault(); // Stops page refresh
    post_expression()
});

async function post_expression() {
    const data = new URLSearchParams(new FormData(form));
    const response = await fetch('/solve/', {
        method: 'POST',
        body: data
    })
    const res = await response.json()
    const result_box = document.getElementById("result_box");
    result_box.innerText = res.result
    

}