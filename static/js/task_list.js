$(function () {
    // 全局查
    $(document).ready(function () {
        // var data = JSON.stringify({
        //     project_id:$('#api-menu-project-id').data('id')
        // });
        $.ajax({
            url:'/api/all_case',
            type:'GET',
            dataType:'json',
            success:function (data) {
                    var html = '';
                    for(var i = 0; i < data.length; i++) {
                        html = html + "<tr data-id = 1>" +
                            "<td><input type='checkbox'></td>" +
                            "<td>"+data[i].value+"</td>" +
                            "<td>"+data[i].title+"</td>" +
                            "</tr>";
                        document.getElementById("table-tbody").innerHTML=html;
                    }
                }

        });
        $.ajax({
            url:'/api/scene_list',
            type:'GET',
            dataType:'json',
            success:function (data) {
                    var html = '';
                    var list=data.datas.scene_list;
                    for(var i = 0; i < list.length; i++) {
                        html = html + "<tr data-id = 1>" +
                            "<td><input type='checkbox'></td>" +
                            "<td>"+list[i].id+"</td>" +
                            "<td>"+list[i].scene_name+"</td>" +
                            "</tr>";
                        document.getElementById("table-scene").innerHTML=html;
                    }
                }

        });
    });

});
$('#create_task').on('click', function () {
        alert("test");
    });