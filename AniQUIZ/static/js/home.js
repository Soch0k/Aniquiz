let numClick = 1
let margin = -405
$('#nextSlide').click(function (e) { 
    if(numClick == $('.cards').children.length) {
        numClick = 0
        margin = 0
    }
    $('.cards').css('margin-left', margin)

    e.preventDefault();
    
    numClick += 1
    margin -= 405

    console.log(numClick)
    console.log($('.cards').children.length)
});