$(function () {


    $('input[status="True"]').prop('checked', 'checked');
    if ($('input[status="True"]').length == $('input[status]').length) {
        $('#all_select').prop('checked', true);
    }
    else {
        $('#all_select').prop('checked', false);
    }
    $('#all_select').change(function () {
        $.ajax({
            'url': '/purchase/select_purchase/',
            'type': 'post',
            'data': {
                'all_select': Number($(this).prop('checked'))
            },
            success: function (result) {
                if (result.code == '888') {
                    window.location.href = '/purchase/query_purchase/'
                }
            }
        })
    });


    $('input[status]').change(function () {
        $.ajax({
            'url': '/purchase/select_purchase/',
            'type': 'post',
            'data': {
                'id': Number($(this).attr('id')),
                'status': Number($(this).prop('checked')),
            },
            success: function (result) {
                if (result.code == '888') {
                    window.location.href = '/purchase/query_purchase/'
                }
            }
        });

    });
});