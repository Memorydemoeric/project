$(function () {
    $('#location').change(function () {
        console.log('修改1。。。');
        $.ajax({
            url: '/create_pur_order/',
            type: 'post',
            data: {
                'location': $('#location').val(),
            },
            success: function (result) {
                $('#cust_name option').remove();
                for (i of result.cust_info) {
                    console.log(i.id)
                    $('#cust_name').append('<option name="' + i.id + '">' + i.name + '</option>')
                }
                var $cust_id = $('#cust_name option:selected').attr('name');
                $('#secret_cust_id').val($cust_id);
            },
        })
    });


    $('#cust_name').change(function () {
        var $cust_id = $('#cust_name option:selected').attr('name');
        console.log($cust_id);
        $('#secret_cust_id').val($cust_id);
    });


    $('.del_order').click(function () {
        var $order_id = $(this).attr('name');
        $.ajax({
            'url': '/delete_pur_order/',
            'type': 'post',
            'data': {'id': $order_id},
            success: function (res) {
                if (res.code1 == '888') {

                    $('tr[name=' + $order_id + ']').remove()
                }
            }
        })
    });


});