localStorage.setItem("stage", "login");

var socket = io();
var abstrat_list_HTML_all_hidden = "";

var generate = document.getElementById("generate");

generate.addEventListener("click", function() {
    console.log("Key pressed generate");
    var problem_output = "";

    socket.emit("gen", function(result) {
        if (result["done"] == true) {
            // go_next(result['problem_list'],result['answer_list']);
            problem_output += result["problem_list"];
            // answer_output += result["answer_list"];
            go_next(problem_output);
        } else {
            console.log(result["done"]);
        }
    });
});

function go_next(problem_list) {
    localStorage.setItem("problem_list", problem_list);
    // localStorage.setItem("answer_list", answer_list);
    window.location.href = "chat.html";
}
