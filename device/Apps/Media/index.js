
$(function () {
    $('#TextButton').on('click', function () {
        console.log("Hello")
        var text = document.getElementById("textbox").value
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Plex",
            Func: "getObject",
            Params: text,
            ExpectReturn: true
        }, function (data) {
            console.log(data);
            document.getElementById("Titles").innerHTML = data
        });
    });
});

$(function () {
    $('#PauseButton').on('click', function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Plex",
            Func: "pressSpacebar",
            Params: [],
            ExpectReturn: true
        }, function (data) {
        });
    });
});