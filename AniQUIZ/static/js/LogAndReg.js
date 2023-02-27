$(document).on('click', '.containerLogAndReg .btns .btnReg', function(e) {
    $('.register').css({display: "flex"});
    $('.containerLogAndReg .login').css({display: "none"})
})
$(document).on('click', '.containerLogAndReg .btns .btnLog', function(e) {
    $('.containerLogAndReg .login').css({display: "flex"});
    $('.register').css({display: "none"})
})