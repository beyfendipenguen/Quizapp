console.log("hello world");
const modalBtns = [...document.getElementsByClassName("modal-button")]
const modalBody = document.getElementById("modal-body-confirm")
const startBtn = document.getElementById("start-button")

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute("data-pk")
    const name = modalBtn.getAttribute("data-name")
    const numQuestions = modalBtn.getAttribute("data-questions")
    const difficultly = modalBtn.getAttribute("data-difficultly")
    const time = modalBtn.getAttribute("data-time")
    const pass = modalBtn.getAttribute("data-pass")

    modalBody.innerHTML = `
        <div class="h-5 mb-3">Are you sure you want to begin "<b>${name}</b>"?</div>
        <div class="text-muted">
            <ul>
                <li>difficultly: ${difficultly}</li>
                <li>number of question: ${numQuestions}</li>
                <li>score to pass: ${pass}</li>
                <li>time: ${time} min</li>
            </ul>
        </div>
    
    `
    startBtn.addEventListener('click', () => {
        window.location.href = url + pk
    })

}))

