function addItem(item) {
    $.get("/add/"+item);
    $("#items").append('<div class="list-group-item"><span class="item">'+item+'</span><input type="checkbox"><button class="btn btn-default btn-delete"><span class="glyphicon glyphicon-trash"></span></button></div>');
}

function deleteItem(item) {
    $.get("/remove/"+item.find(".item").text());
    item.remove();
}

$("#addItemButton").click(function(e) {
    e.preventDefault();
    addItem($("#itemInput").val());
});

$("#items").on("click", ".btn-delete", function(e) {
    deleteItem($(this).parent());
});
