const btn_add_answer = document.getElementById('btn_add_answer');
const btn_add_question = document.getElementById('btn_add_question');

/*
let answer_laber = document.createElement('label');
answer_laber.className = 'answer';
answer_laber.innerHTML = 'напишите ответ';
*/
let answer_input = document.createElement('input');
answer_input.id = 'answer';


function add_answer () {
    const answers_add_box = document.getElementById('answer_add_box');
    if (answers_add_box.children.length == 12) {
        btn_add_answer.hidden = true;
    }
    else {
        let answer_laber = document.createElement('label');
        answer_laber.className = 'answer' + (answers_add_box.children.length / 2 + 1);
        answer_laber.for = 'answer' + answers_add_box.children.length / 2;
        answer_laber.innerHTML = 'напишите ответ ' + (answers_add_box.children.length / 2 + 1);
        

        

        let answer_input = document.createElement('input');
        answer_input.id = 'answer' + answers_add_box.children.length / 2;
        
        answers_add_box.append(answer_laber);
        answers_add_box.append(answer_input);
    }
    if (answers_add_box.children.length == 12) {
        btn_add_answer.hidden = true;
    }
}
btn_add_answer.addEventListener('click', (e) => {
    add_answer();
});


