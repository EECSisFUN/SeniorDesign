
function myOnload() {
    $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Twitch",
            Func: "getViewerCount",
            Params: [],
            ExpectReturn: true
        }, function (data) {
            console.log(data)
            $("#count").html(data);
            $.getJSON("http://127.0.0.1:5001" + '/data', {
                Name: "Twitch",
                Func: "getModerators",
                Params: [],
                ExpectReturn: true
            }, function (data) {
                console.log(data)
                data.data.forEach(element => {
                    $("#mods").html(element.user_name);
                });
                
                $.getJSON("http://127.0.0.1:5001" + '/data', {
                    Name: "Twitch",
                    Func: "getBans",
                    Params: [],
                    ExpectReturn: true
                }, function (data) {
                    console.log(data)
                    data.data.forEach(element => {
                        $("#bans").html(element.user_name);
                    });
                    $.getJSON("http://127.0.0.1:5001" + '/data', {
                        Name: "Twitch",
                        Func: "getSubscriptions",
                        Params: [],
                        ExpectReturn: true
                    }, function (data) {
                        console.log(data)
                        data.data.forEach(element => {
                            $("#subs").html(element.user_name);
                        });
                        getChat(); // starts the chat read loop
                    });
                });
            });
    });
    
   
   
}

$(function () {
    $('#commerical').on("click", function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Twitch",
            Func: "startCommercial",
            Params: [],
            ExpectReturn: false
        }, function (data) {
            
        });
        return false;
    });
});

$(function () {
    $('#subcheckbutton').on("click", function () {
        var user = $("#subcheck").val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Twitch",
            Func: "checkSubscribed",
            Params: user,
            ExpectReturn: false
        }, function (data) {
            $("#subcheckret").innerHTML = "false"
        });
        return false;
    });
});

$(function () {
    $('#descbutton').on("click", function () {
        var desc = $("#desc").val();
        console.log(desc)
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Twitch",
            Func: "updateDescription",
            Params: desc,
            ExpectReturn: true
        }, function (data) {
            $("#descret").html("false");
        });
        return false;
    });
});

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

function getChat() {
    var channel = "maxzilla2017";
    $.getJSON("http://127.0.0.1:5001" + '/data', {
        Name: "Twitch",
        Func: "getChat",
        Params: channel,
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
        // hmm, the recursive stack will surely overflow
        getChat();
        
    });
    
}

$(function () {
    $('#chatbutton').on("click", function () {
        // hmm what should this while predicate be? Just wait for this js to be unloaded, I guess?
        getChat();
    });
});
