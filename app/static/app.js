var items = [];

function addItem(item) {
    if (item && items.indexOf(item) == -1) {
        $.get("/add/"+item);
        items.push(item);
        $("#items").append('<div class="list-group-item"><span class="item">'+item+'</span><input type="checkbox"><button class="btn btn-default btn-delete"><span class="glyphicon glyphicon-trash"></span></button></div>');
    }
}

function deleteItem(item) {
    var i = items.indexOf(item.find(".item").text());
    if (i != -1) {
        items.splice(i, 1);
    }
    item.remove();
}

$("#addItemButton").click(function(e) {
    e.preventDefault();
    addItem($("#itemInput").val());
});

$("#items").on("click", ".btn-delete", function(e) {
    deleteItem($(this).parent());
});
