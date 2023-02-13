


$(document).on('click', '#start_quiz_btn', function(e) {
    ajax_get_question(i)
    i++
    $(".card").css({display: "none"});
    $('.quiz_container_with_questions').show();
})

$(document).on('click', '#next', function(e) {
    ajax_get_question(i)
    i++
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

$(document).ready(function() {


})


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
                                                '<label class="ans" for="answer'+n+'">'+ item.answer +'</label>'+
                                            '</div>')

                    $('#answers_box').append($answers_block)
                }
                n++
            })
        },

        error: function(response){
            console.log('Something went wrong');
            $('#blat_gde').text('huesos')
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
  console.log( "clicked: " + event.target.nodeName );
});


let i = 0
$(document).on('click', '#blat_gde', function(e) {
//    ajax_get_question(i)
//    i++
})











