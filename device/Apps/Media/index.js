function setup(){
    $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "WindowsProgramControl",
            Func: "getOpenWindows",
            Params: [],
            ExpectReturn: true
        }, function (data) {
            console.log(data)
            data.forEach(makeRadioButtons)
        });
}

function makeRadioButtons(value, index){
    var id = value
    var input = '<input type="radio" id=' + id + ' name="window" value=' + id + '>'
    var label = '<label for=' + id + '>' + id + '</label><br></br>' 
    $("#radioholder").append(input)
    $("#radioholder").append(label)
}

$(function () {
    $('#PauseButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressSpacebar",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#MinimizeButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressESC",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#SkipBackwardsButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressLeftArrow",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#SkipForwardButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressRightArrow",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#VolUpButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressUpArrow",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#VolDownButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressDownArrow",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#FullScreenButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "Fullscreen",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#0SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum0",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#10SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum1",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#20SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum2",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#30SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum3",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#40SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum4",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#50SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum5",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#60SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum6",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#70SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum7",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#80SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum8",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#90SecButton').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "pressNum9",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#SkipToNextItem').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "skipToNextItem",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#openPlayer').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "openPlayer",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});

$(function () {
    $('#closePlayer').on('click', function () {
        var prog = $('input[name="window"]:checked').val();
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "Media",
            Func: "closePlayer",
            Params: prog,
            ExpectReturn: true
        }, function (data) {
        });
    });
});