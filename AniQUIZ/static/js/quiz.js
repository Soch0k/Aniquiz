let question_is = 0

let answers_list = ''

$(document).on('click', '#start_quiz_btn', function(e) {
    ajax_get_question(question_is)
    question_is++
    $(".card").css({display: "none"});
    $('.quiz_container_with_questions').show();
})



$(document).on('click', '#next', function(e) {
    console.log('hui')//delete-this-strok
    var check_is_answer = 0;
    for(let k = 0; k < $('#answers_box_ans div').length; k++) {
        console.log(k)//delete-this-strok
        if($("#answer"+k).is(':checked')) {
            console.log('hui')//delete-this-strok
            answers_list+=$('#idAnswer'+k).val()
            answers_list+=' '
            console.log(answers_list)//delete-this-strok
        }
    }
    if (answers_list !== 0) {
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
            $('#answers_box_ans').empty()
            var n = 0
            response.Answers.forEach(function(item) {

                    var $answers_block = $( '<div class="answer">'+
                                                '<label class="ans" for="answer'+n+'" id="label'+n+'">'+ item.answer +'</label>'+
                                                '<input id="answer'+n+'" type="radio" name="ANSWER" value="0">'+
                                                '<input hidden id="idAnswer'+n+'" value="'+item.id+'">'+
                                            '</div>')

                    $('#answers_box_ans').append($answers_block);

                n++
            })
        },

        error: function(response){
            $.ajax({
                url: 'result/'+$('#quiz_pk').val(),
                type: 'POST',
                //dataType: "json",

                data: {
                    'answers': answers_list,
                    'csrfmiddlewaretoken': token
                },


            })

            window.location.replace("result/"+$('#quiz_pk').val())

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



$('.answer input[type=radio]').change(function (e) { 
    e.preventDefault();
    $('#next').css('background-color', 'red');
    $('.quiz_container_with_questions').css('background-color', 'red');
    array.forEach(element => {
        
    });

    $('.answer .ans').addClass();
});

$('input[type=radio][name=ANSWER]').change(function() {
    $('#next').css('background-color', 'red');
    if (this.value == 'answer0') {
        console.log('huesos')
    }
    else if (this.value == 'transfer') {
        $('#next.next_question').css('background-color', 'red');
    }
});



