$(document).ready(function () {
    $(".list-group-item-action").click(function () {
        let user_name = $(this).attr('id');
        $.get("http://127.0.0.1:8000/write/" + user_name)
            .then(function (result) {
                $("#detailModalLocation").text('지역: ' + result.location);
                $("#detailModal").modal('show');
            });
    });
});