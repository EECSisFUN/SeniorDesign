
$(function () {
    $('#ExampleButton').on('click', function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Twitch",
            Func: "getTopGames",
            Params: [],
            ExpectReturn: true
        }, function (data) {
            console.log(data.data[0].name);
            //document.getElementById("ExampleButton").innerHTML = data.text
            for (rep = 0; rep < data.data.length; rep++) {
                document.getElementById("games").innerHTML = document.getElementById("games").innerHTML +("<div>" + data.data[rep].name+ "</div> </br>")
                console.log(data.data[rep].name);
            }
        });
    });
});
