// Make connection socket

// const key = client_random_key_gen(); // get the unique random key for this session
// var stage = localStorage.getItem("stage");
// if (stage === "login") {
//     localStorage.setItem("stage", "chat");
// } else {
//     window.location.href = "index.html";
// } /////check if it's reload from itself, if so kick back to login screen.

// var problem_list = localStorage.getItem("problem_list");
// q;
//.replace(/\//gi, "\\").replace("<latex>", "$$").replace("</latex>", "$$");
// var answer_list = localStorage.getItem("answer_list"); //.replace(/\//gi, "\\").replace("<latex>", "$$").replace("</latex>", "$$");
// var current_display = 0;
// console.log("Got result.\n", problem_list, answer_list);

var output = document.getElementById("output"); //,
var problem_list =
    "### ^SPX Hourly Volume change<br>| 09:30 | 10:30 | 11:30 | 12:30 |<br>|:---:|:---:|:---:|:---:|<br>| 43.81 | 519.40 | 12.06 | (68.27) |<br>";
// swap = document.getElementById("swap");
// console.log(problem_list.replace("<br>", "\n"));
var content = marked.parse(problem_list.replaceAll("<br>", "\n"));

output.innerHTML = content.replaceAll("<table", '<table class="fl-table" ');

function readTextFile(file) {
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status == 0) {
                var allText = rawFile.responseText;
                alert(allText);
            }
        }
    };
    rawFile.send(null);
}

// Emit events
// Detect the click event on send key
// swap.addEventListener("click", function() {
//     current_display += 1;
//     if (current_display % 2 == 0) {
//         output.innerHTML = problem_list;
//         MathJax.typeset();
//     } else {
//         output.innerHTML = answer_list;
//         MathJax.typeset();
//     }
// });
// Detect the ENTER key pressed inside the message input box
