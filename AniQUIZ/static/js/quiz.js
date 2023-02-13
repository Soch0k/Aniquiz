


$(document).on('click', '#start_quiz_btn', function(e) {
    ajax_get_question(i)
    i++
    $(".card").css({display: "none"});
    $('.quiz_container_with_questions').show();
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
            //console.log(response.Answers.answer)
            response.Answers.forEach(function(item) {
                if (item.question_pk == i+1) {
                    var $answers_block = $( '<div class="answer">'+
                                                '<input id="answer0" type="radio" name="ANSWER" value="0">'+
                                                '<label class="ans" for="answer0">'+ item.answer +'</label>'+
                                            '</div>')
                    $('#answers_box').append($answers_block)
                }
            })
        },

        error: function(response){
            console.log('Something went wrong');
            $('#blat_gde').text('huesos')
        },
    });
}
let i = 0
$(document).on('click', '#blat_gde', function(e) {
//    ajax_get_question(i)
//    i++
})











