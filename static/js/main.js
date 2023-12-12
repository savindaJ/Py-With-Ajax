$('#btnSave').on('click',function () {
    $.ajax({
        url:"/save",
        type:"POST",
        data:{
            cusId: $('#cusId').val(),
            name: $('#name').val(),
            address: $('#address').val(),
            salary: $('#salary').val()
        },
        success:function (res) {
            if (res.state==='200'){
                alert("successfully saved !")
            }else {
                alert("bad request !")
            }
        },
        error:function (err) {

        }
    })
});

$('#delete').on('click',function () {
    $.ajax({
        url:"/delete",
        type:"DELETE",
        data:{
            cusId: $('#cusId').val()
        },
        success:function (res) {
            if (res.state==='200'){
                alert("successfully deleted !")
            }else {
                alert("bad request !")
            }
        },
        error:function (err) {

        }
    })
});

$('#update').on('click',function () {
    $.ajax({
        url:"/update",
        type:"PUT",
        data:{
            cusId: $('#cusId').val(),
            name: $('#name').val(),
            address: $('#address').val(),
            salary: $('#salary').val()
        },
        success:function (res) {
            if (res.state==='200'){
                alert("successfully updated !")
            }else {
                alert("bad request !")
            }
        },
        error:function (err) {

        }
    })
});