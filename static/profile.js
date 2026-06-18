const user_data = JSON.parse(document.getElementById('jinja-data').textContent);
const logs = user_data.logs;
console.log(logs)
const username = user_data.username;
const greeting = document.getElementById("greeting");
const scoreTitle = document.getElementById("user-score");

greeting.textContent = `Hello ${username}!`
const table = document.getElementById("log-table");
let totalScore = 0
for (let i=logs.length-1;i>=0 ;i--){
    totalScore += logs[i].score > 0? parseFloat(logs[i].score): 0
table.innerHTML += `<tr>
            <th>${String(parseInt(i)+1)}</th>
            <th>${String(logs[i].time)}</th>
            <th>${String(logs[i].type)}</th>
            <th>${String(logs[i].expression)}</th>
            <th>${String(logs[i].result)}</th>
            <th>${String(logs[i].score == -1? '-': logs[i].score)}</th>
        </tr>`
}
scoreTitle.textContent = `Your score: ${totalScore}`