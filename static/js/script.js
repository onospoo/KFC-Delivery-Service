$(document).ready(function () {
    $("#cat_act").addClass("active");
    $(".order-field").children("input").addClass("form-control");
    $(".order-field").children("select").addClass("form-control");
    $("#show_date").click(function() {
        $("#date-order").removeClass("hidden");
        $("#show_date").addClass("btn-primary");
        $("#close_date").removeClass("btn-primary");
    });
    $("#close_date").click(function() {
        $("#date-order").addClass("hidden");
        $("#show_date").removeClass("btn-primary");
        $("#close_date").addClass("btn-primary");
    });
    function clear_date() {
        document.getElementById('id_date_order_day').value='';document.getElementById('id_date_order_month').value='';document.getElementById('id_date_order_year').value='';document.getElementById('id_time_order').value='';
    };
});