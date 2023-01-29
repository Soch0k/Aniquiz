const BtnStart = document.getElementById("start_quiz");
const Quiz_container = document.getElementById("quiz_container");

function hide_quiz_container() {
    Quiz_container.hidden = true;
}

BtnStart.addEventListener('click', (e) => {
    hide_quiz_container();
});