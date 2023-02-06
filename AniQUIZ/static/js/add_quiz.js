
function add_answer () {
    const answers_add_box = document.getElementById('answer_add_box');
    if (answers_add_box.children.length !== 6) {
        let answer_laber = document.createElement('label');
        answer_laber.className = 'answer' + (answers_add_box.children.length   + 1);
        answer_laber.for = 'answer' + answers_add_box.children.length ;
        answer_laber.innerHTML = 'напишите ответ ' + (answers_add_box.children.length  + 1);

        let div_ans = document.createElement('div');

        let answer_is_correct = document.createElement('label')

        answer_is_correct.id = 'correct_answer_' + (answers_add_box.children.length+1) ;
        answer_is_correct.innerHTML = 'ответ правильный?';
        answer_is_correct.className = 'is_correct';


        let answer_input = document.createElement('input');
        answer_input.id = 'answer' + (answers_add_box.children.length+1);

        let answer_correct_check = document.createElement('input');
        answer_correct_check.type = 'radio';
        answer_correct_check.name = 'correct';
        answer_correct_check.id = "is_correct" + (answers_add_box.children.length+1) ;

        div_ans.append(answer_laber);
        div_ans.append(answer_is_correct);
        div_ans.append(answer_correct_check);
        div_ans.append(answer_input);
        answers_add_box.append(div_ans);

    }
    if (answers_add_box.children.length == 6) {
        btn_add_answer.style.display = 'none';
    }
}
//document.querySelector('#btn_add_answer').onclick = function() {
//    add_answer()
//}

$(document).on('click', '#btn_add_answer', function(e) {
    add_answer();
    const answers_add_box = document.getElementById('answer_add_box');
    for (let i = 1; i < answers_add_box.children.length+1; i++) {

        let id_name = 'answer' + i;
        console.log(id_name)
    }

})



//function addquestions () {
//    let pk =
//
//    for (let k = 1; k < document.getElementById('answer_add_box').children.length+1; k++) {
//        let formData_answer = new FormData();
//        let id_name = 'answer' + k;
//        let correct_answer = 'correct_answer_' + k;
//        formData_answer.append('answer', $(id_name).val());
//        formData_answer.append('correct', $(correct_answer).val());
//        formData_answer.append('question_pk', $('#pk_question').val());
//
//        $.ajax({
//            type: 'POST',
//            url: "{% url 'add_quiz_answers'  %}",
//            data: formData_answer,
//            cache: false,
//            processData: false,
//            contentType: false,
//            enctype: 'multipart/form-data',
//            success: function (){
//                alert('the post has been created')
//            },
//            error: function(xhr, errmsg, err) {
//                console.log(xhr.status + ":" + xhr.responseText)
//            },
//        })
//    }
//}

var serverResponse = document.querySelector('#response')

document.forms.answerForm.onsubmit = function() {
    e.preventDefault();
    var answers_add_box = document.getElementById('answer_add_box');

    var question = $('#pk_question').val();

    console.log(question);

    var formData_answer = new FormData(document.forms.answerForm);

    //for (let i = 1; i < answers_add_box.children.length+1; i++) {
    //    let answer = 'answer'+i;
    //    let answer_id = '#answer'+i;
    //
    //
    //    console.log($(answer_id).val())
    //
    //    formData_answer.append(answer, $(answer_id).val())
    //
    //}
    var xhr = new XMLHttpRequest();

    xhr.open('POST', "{% url 'add_quiz_answers' %}");

    xhr.setRequestHeader('Content-Type', 'application/x-www-urlencoded')

    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4 && xhr.status === 200) {
            serverResponse.textContent = xhr.responseText
        }
    }

    xhr.send('answer', $('#answer1'));

};

//$(document).on('click', '#btn_save', function(e) {
//    const answers_add_box = document.getElementById('answer_add_box');
//    let formData_answer = new FormData();
//    for (let i = 1; i < answers_add_box.children.length+1; i++) {
//
//        let id_name = '#answer' + i;
//        let correct_answer = '#correct_answer_' + i;
//
//
//        console.log(id_name)
//        console.log($(id_name).val())
//        console.log($(correct_answer).val())
//        console.log(answers_add_box.children.length)
//
//
//        formData_answer.append('popit', $('#answer1').val());
//        formData_answer.append(correct_answer, $(correct_answer).val());
//        formData_answer.append('question_pk', $('#pk_question').val());
//
//
//    }
//    formData_answer.append('quantity', $(answers_add_box.children.length));
//    $.ajax({
//         type: 'POST',
//         url: "{% url 'add_quiz_answers' %}",
//         data: formData_answer,
//         cache: false,
//         processData: false,
//         contentType: false,
//         enctype: 'multipart/form-data',
//         success: function (){
//             alert('the post has been created')
//         },
//         error: function(xhr, errmsg, err) {
//             //console.log(xhr.status + ":" + xhr.responseText)
//         },
//    })
//    console.log(formData_answer)
//
//})

