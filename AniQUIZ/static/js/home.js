let numClick = 0
let margin = -405
$('#nextSlide').click(function (e) { 
    if(numClick == $('.cards').children.length) {
        numClick = -1
        margin = 0
    }
    $('.cards').css('margin-left', margin)
    
    console.log('huesos')
    
    e.preventDefault();
    
    numClick += 1
    margin -= 405

    console.log(numClick)
    console.log($('.cards').children.length)
});