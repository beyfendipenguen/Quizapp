console.log('hello')
const url = window.location.href

const quizBox = document.getElementById("quiz-box")


$.ajax({
    type:'GET',
    url: `${url}data`,
    success: function(response){
        const data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)) {
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>

                    </div>
                `
                answers.forEach(answer=>{
                    quizBox.innerHTML +=`
                    <div>
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <label for="${question}">${answer}</label>    
                    </div>
                    `
                })
            }
        })
    },
    error: function(error){
        console.log(error)
    }

})