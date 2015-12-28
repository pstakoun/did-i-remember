function addItem(item) {
    $.get("/add/"+encodeURIComponent(item), function(data) {
        if (data) {
            $("#items").prepend('<div class="list-group-item"><span class="item">'+item+'</span><input type="checkbox"><button class="btn btn-default btn-delete"><span class="glyphicon glyphicon-trash"></span></button></div>');
            getSuggestions();
        }
    });
}

function removeItem(item) {
    $.get("/remove/"+encodeURIComponent(item.find(".item").text()), function(data) {
        getSuggestions();
    });
    item.remove();
}

function getSuggestions() {
    $("#suggestions").html('');
    $.get("/suggestions", function(data) {
        arr = data.split(',');
        for (var i = 0; i < arr.length; i++) {
            if (arr[i]) {
                $("#suggestions").prepend('<div class="list-group-item"><span class="item">'+arr[i]+'</span><input type="checkbox"><button class="btn btn-default btn-delete"><span class="glyphicon glyphicon-trash"></span></button></div>');
            }
        }
    });
}

function removeSuggestion(item) {
    $.get("/removesuggestion/"+encodeURIComponent(item.find(".item").text()), function(data) {
        getSuggestions();
    });
    item.remove();
}

$("#addItemButton").click(function(e) {
    e.preventDefault();
    addItem($("#itemInput").val());
});

$("#items").on("click", ".btn-delete", function(e) {
    removeItem($(this).parent());
});

$("#suggestions").on("click", ".btn-delete", function(e) {
    removeSuggestion($(this).parent());
});
