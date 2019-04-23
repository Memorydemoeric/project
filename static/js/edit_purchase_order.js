$(function () {
    var $modify = $('#modify_date');
    var $ord_id = $('#modify_date').attr('name')
    $('#modify_date').click(function () {
        $(this).parent().replaceWith('<td><input type="date" id="modify"></td>');
        $modify = $('#modify');


        $modify.change(function () {
            var $new_date = $('#modify').val();

            $.ajax({
                'url': '/purchase/edit_pur_date/',
                'type': 'post',
                'data': {
                    'order_id': $ord_id,
                    'new_date': $new_date,
                },
                success: function (res) {
                    if (res.code1 == '888') {
                        window.location.href = '/purchase/edit_pur_order/?ord_id=' + $ord_id
                    }
                }
            });
        });
    });
    document.getElementById('pro_id').focus();
    $('#order_detail').scrollTop(100000)

    $('#file_upload_button').click(function () {
        $('#file_in').click();
        $('#file_in').change(function () {
            $('#pur_submit').click();
        });
    });
});