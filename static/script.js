let questions = [];

async function fetchQuestions() {
    const res = await fetch('/quiz/');
    questions = await res.json();
    const form = document.getElementById("quiz-form");
    form.innerHTML = '';

    questions.forEach((q, index) => {
        const div = document.createElement('div');
        div.innerHTML = `
            <p>${index + 1}. ${q.question}</p>
            <label><input type="radio" name="q${q.id}" value="A"> ${q.option_a}</label><br>
            <label><input type="radio" name="q${q.id}" value="B"> ${q.option_b}</label><br>
            <label><input type="radio" name="q${q.id}" value="C"> ${q.option_c}</label><br>
            <label><input type="radio" name="q${q.id}" value="D"> ${q.option_d}</label><br><br>
        `;
        form.appendChild(div);
    });
}

async function submitAnswers() {
    const answers = questions.map(q => {
        const selected = document.querySelector(`input[name="q${q.id}"]:checked`);
        return {
            question_id: q.id,
            selected_option: selected ? selected.value : ""
        };
    });

    const res = await fetch('/quiz/submit', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ answers })
    });

    const result = await res.json();
    document.getElementById("result").innerText = `Your Score: ${result.score} / ${result.total}`;
}

window.onload = fetchQuestions;
