const btn_add_answer = document.getElementById('btn_add_answer');
const btn_add_question = document.getElementById('btn_add_question');

/*
let answer_laber = document.createElement('label');
answer_laber.className = 'answer';
answer_laber.innerHTML = 'напишите ответ';
*/


function add_answer () {
    const answers_add_box = document.getElementById('answer_add_box');
    if (answers_add_box.children.length !== 24) {
        let answer_laber = document.createElement('label');
        answer_laber.className = 'answer' + (answers_add_box.children.length / 4 + 1);
        answer_laber.for = 'answer' + answers_add_box.children.length / 4;
        answer_laber.innerHTML = 'напишите ответ ' + (answers_add_box.children.length / 4 + 1);
        
        let answer_is_correct = document.createElement('label')
        answer_is_correct.id = 'correct_answer_' + answers_add_box.children.length / 4;
        answer_is_correct.innerHTML = 'ответ правильный?';
        answer_is_correct.className = 'is_correct';


        let answer_input = document.createElement('input');
        answer_input.id = 'answer' + answers_add_box.children.length / 4;
        
        let answer_correct_check = document.createElement('input');
        answer_correct_check.type = 'checkbox';
        answer_correct_check.id = answers_add_box.children.length / 4;

        answers_add_box.append(answer_laber);
        answers_add_box.append(answer_is_correct);
        answers_add_box.append(answer_correct_check);
        answers_add_box.append(answer_input);
        
    }
    if (answers_add_box.children.length == 24) {
        btn_add_answer.hidden = true;
    }
}
btn_add_answer.addEventListener('click', (e) => {
    add_answer();
});




function addquestions () {
    let pk =

    for (let k = 1; k < document.getElementById('answer_add_box').children.length+1; k++) {
        let formData_answer = new FormData();
        let id_name = 'answer' + k;
        let correct_answer = 'correct_answer_' + k;
        formData_answer.append('answer', $('#id_name').val());
        formData_answer.append('correct', $('#correct_answer').val());
        formData_answer.append('question_pk', $('#pk_question').val());

        $.ajax({
            type: 'POST',
            url: "{% url 'add_quiz_answers'  %}",
            data: formData_answer,
            cache: false,
            processData: false,
            contentType: false,
            enctype: 'multipart/form-data',
            success: function (){
                alert('the post has been created')
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ":" + xhr.responseText)
            },
        })
    }
}

$(document).on('click', '#btn_save', function(e) {
    addquestions();
})

