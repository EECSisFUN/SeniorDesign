
$(function () {
    $('#gamesbutton').on("click", function () {
        var channel = $("#channel").val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Twitch",
            Func: "getTopGames",
            Params: [],
            ExpectReturn: true
        }, function (data) {
            console.log(data);
            for (rep = 0; rep < data.data.length; rep++) {
                console.log(data.data[rep])
                document.getElementById("topgames").innerHTML = 
                document.getElementById("topgames").innerHTML 
                + ("<div>" + data.data[rep]["name"] +  "</div>")
                + ("<img src=" + data.data[rep]["box_art_url"].replace("{width}", "72").replace("{height}", "128") + ">")
            }
            
        });
        return false;
    });
});

$(function () {
    $('#button').on("click", function () {
        var channel = $("#channel").val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Twitch",
            Func: "getFakeText",
            Params: [],
            ExpectReturn: true
        }, function (data) {
            console.log(data);
            console.log(data[0]);

            for (var item in data) {
                console.log(item)
                document.getElementById("chat").innerHTML = 
                document.getElementById("chat").innerHTML 
                + ("<div>" + data[item][0] + " : " + data[item][1]+ "</div> </br>")
            }
            
        });
        return false;
    });
});
