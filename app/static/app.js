function addItem(item) {
    $.get("/add/"+encodeURIComponent(item), function(data) {
        if (data) {
            $("#items").append('<div class="list-group-item"><span class="item">'+item+'</span><input type="checkbox"><button class="btn btn-default btn-delete"><span class="glyphicon glyphicon-trash"></span></button></div>');
        }
    });
}

function removeItem(item) {
    $.get("/remove/"+encodeURIComponent(item.find(".item").text()));
    item.remove();
}

function getSuggestions() {
    $("#suggestions").html('');
    $.get("/suggestions", function(data) {
        arr = data.split(',');
        for (var i = 0; i < arr.length; i++) {
            if (arr[i]) {
                $("#suggestions").append('<div class="list-group-item"><span class="item">'+arr[i]+'</span><input type="checkbox"><button class="btn btn-default btn-delete"><span class="glyphicon glyphicon-trash"></span></button></div>');
            }
        }
    });
}

function removeSuggestion(item) {
    $.get("/removesuggestion/"+encodeURIComponent(item.find(".item").text()));
    item.remove();
}

$("#addItemButton").click(function(e) {
    e.preventDefault();
    addItem($("#itemInput").val());
    //getSuggestions(); TODO
});

$("#items").on("click", ".btn-delete", function(e) {
    removeItem($(this).parent());
    //getSuggestions(); TODO
});

$("#suggestions").on("click", ".btn-delete", function(e) {
    removeSuggestion($(this).parent());
    //getSuggestions(); TODO
});
