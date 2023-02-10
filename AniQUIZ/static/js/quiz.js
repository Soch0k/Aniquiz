


$(document).on('click', '#start_quizker', function(e) {
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


$(document).on('click', '#blat_gde', function(e) {
    console.log($('#quiz_pk').val())
    $.ajax({
        url: '/quiz/'+$('#quiz_pk').val()+'/1',
        type: 'GET',
        success: function(resp){
            //resp.data.forEach(elwm => {
            //    console.log(elwm)
            //})
            console.log(resp);
            resp.forEach(elem => console.log(elem));
        },

        error: function(resp){
            console.log('Something went wrong');
        },
    });
})











