"use strict";
const socket = require("socket.io"), // socket for serving the chat service
    express = require("express"),
    path = require("path"),
    app = express(),
    server = require("http").Server(app),
    server_io = socket(server); // the io for chat server
// const express = require("express"),
//     app = express(),
//     server = require("http").Server(app),
//     server_io = require("socket.io")(server), //, { serveClient: false }),
//     path = require("path");
// server_io = socket(server); // the io for chat server

/////// set the http listen and httpd working directory
app.set("view engine", "html")
    .get("/", function(req, res) {
        res.sendFile(path.join(__dirname + "/public/"));
    })
    .use(express.static(path.join(__dirname, "public")));

if (module === require.main) {
    const PORT = process.env.PORT || 8080;
    server.listen(PORT, () => {
        console.log(`App listening on port ${PORT}`);
        console.log("Press Ctrl+C to quit.");
    });
}

// try_js_py()
server_io.on("connection", function(socket) {
    console.log(`made socket connection ${socket.id}`, socket.id);

    socket.on("gen", function(
        // problem_num,
        // num_of_col,
        // question_type_list_string,
        cb_function
    ) {
        console.log(
            "received client gen request"
            // problem_num,
            // num_of_col,
            // question_type_list_string
        );
        try {
            var ps = require("python-shell");
            var options = {
                args: []
                //     problem_num,
                //     num_of_col,
                //     question_type_list_string,
                //     "There_is_no_page_key_input" // new means to generate new page key
                // ]
            };
            ps.PythonShell.run("./js_interface.py", options, function(
                err,
                results
            ) {
                if (err) {
                    console.log(err);
                    cb_function({
                        done: err
                    });
                } else {
                    // console.log(results);
                    // results = fix_python_backslash_error(results);
                    console.log("Get problem HTML from python code.");
                    // results = replace_latex_for_multiple__strings(results);
                    // console.log("Converted latex to svg finished");
                    cb_function({
                        done: true,
                        problem_list: results[1]
                        // answer_list: results[1]
                        // 'page_key': results[2]
                    });
                    // console.log(results['problem_list'])
                }
            });
        } catch (err) {
            cb_function({
                done: err
            });
            // TabNine::semSemantic completion enabled.
        }
    });
}); /// end of io connect

// function fix_python_backslash_error(input_string) {
//     var replace_table = [
//         [String.raw `\\div`, String.raw `\div`]
//     ];
//     for (var i = 0; i < input_string.length; i++) {
//         for (var j = 0; j < replace_table.length; j++) {
//             input_string[i].replace(replace_table[j][0], replace_table[j][1]);
//         }
//     }
//     return input_string;
// }

// ////////////////////////////////////////////////////////////////
