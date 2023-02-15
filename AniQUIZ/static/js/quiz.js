let question_is = 0

var answers_list = {}

$(document).on('click', '#start_quiz_btn', function(e) {
    ajax_get_question(question_is)
    question_is++
    $(".card").css({display: "none"});
    $('.quiz_container_with_questions').show();
})



$(document).on('click', '#next', function(e) {
    var check_is_answer = 0;
    for(let k = 0; k < $('#answers_box div').length; k++) {
        if($("#answer"+k).is(':checked')) {
            answers_list['question_'+question_is] = question_is;
            answers_list['answer_'+question_is] = 'answer'+k
            check_is_answer++
        }
    }
    if (check_is_answer !== 0) {
        ajax_get_question(question_is)
        question_is++
    }else {
        alert('Выберите ответ')
    }
})

//$.ajax({
//    url: "{% url 'jquery' %}",
//    datatype: 'json',
//    type: 'GET',
//    data
//    success: function (response) {
//        console.log(response)
//    }
//});



//$.ajax("{% url 'jquery' %}", {
//    data: 1,
//    success: function(data) {
//        data.forEach(function(el) {
//            console.log(data);
//            const img = document.createElement('img');
//            img.src = el.thumbnail;
//            document.querySelector('body').appendChild(img);
//        });
//    }
//});

function redirectOnQuizResult () {
     var xhr = new XMLHttpRequest();
     xhr.open('GET', "{% url 'home' %}");
}

var a = document.cookie.split(';');
var token = ''
for (i = 0; i < a.length; i++) {
    var b = a[i].split('=')
    b[0] = b[0].replace(/\s+/g, '')
    if (b[0] == 'csrftoken') {
        token = b[1]
    }
}

function ajax_get_question (i) {
    $.ajax({
        url: ''+$('#quiz_pk').val()+'/'+i,
        method: 'GET',
        dataType: "json",
        //data: {
        //    thisQuiz: $('#ThisQuiz').val(),
        //},
        success: function(response){
            $('#question_text').text(response.Question.question)
            $('#question_image').attr('src', '/'+response.Question.image);
            $('#answers_box').empty()
            //console.log(response.Answers.answer)
            var n = 0
            response.Answers.forEach(function(item) {
                if (item.question_pk == i+1) {
                    var $answers_block = $( '<div class="answer">'+
                                                '<input id="answer'+n+'" type="radio" name="ANSWER" value="0">'+
                                                '<label class="ans" for="answer'+n+'" id="label'+n+'">'+ item.answer +'</label>'+
                                            '</div>')

                    $('#answers_box').append($answers_block)
                }
                n++
            })
        },

        error: function(response){
        console.log(answers_list)
            $.ajax({
                url: 'result/'+$('#quiz_pk').val(),
                type: 'POST',
                //dataType: "json",

                data: {
                    'quiz_pk': $('#quiz_pk').val(),
                    'dict': JSON.stringify(answers_list),
                    'csrfmiddlewaretoken': token
                },

            })
            //window.location.replace("result/"+$('#quiz_pk').val())

        },
    });
}

//if ($('input[name="ANSWER"]').is(':checked')) {
//    $('label[for="'+ $('input[name="ANSWER"]').id +'"]').css("background-color", "yellow")
//}

//$('.ans').click(function(){
//    $('label[for="'+ $('input[name="ANSWER"]').id +'"]').css("background-color", "yellow")
//
//})

//$('.ans').change(function(){
//    if(this.checked){
//        console.log(this.avl())
//    }else{
//        console.log('huesos')
//    }
//})

//$('#answers_box').on('change', 'input[name="ANSWER"]', function() {
//  console.log('радио изменен');
//  console.log($(this).val());
//
//});

//$(document).on('click', '[name="ANSWER"]', function () {
//    if($(this).is(':checked')) {
//        console.log('hui')
//    }
//})

$( "#answers_box" ).click(function( event ) {

    if($('#label'+event.target.id.slice(6))) {
        for(let i = 0; i < $('#answers_box div').length; i++) {
            $('#label'+i).css('color', 'white')
        }
        $('#label'+event.target.id.slice(6)).css('color', '#d4ef25')
    }
});


















