//页面加载时运行
$(function(){
    //查询的列表
     var test="";
        $.ajax({
        url:'/api/',
        dataType:"json",
        success:function(json){
            test=json.datas;  //将数据保存到变量里边使用
            //接口中存在pro_info层级，所以循环这个
            for (var i=0;i<json.datas.pro_info.length;i++) {
                var pro_name=json.datas.pro_info[i].pro_name;
                $("#select-pro").append("<option selected = \"selected\" value="+pro_name+" >"+pro_name+"</option>");
            }

            for (var i=0;i<json.datas.ver_info.length;i++){
                var ver_name=json.datas.ver_info[i].ver_name;
                $("#select-ver").append("<option selected = \"selected\" value="+ver_name+" >"+ver_name+"</option>");
            }
            for (var i=0;i<json.datas.mod_info.length;i++){
                var mod_name=json.datas.mod_info[i].mod_name;
                $("#select-mod").append("<option selected = \"selected\" value="+mod_name+" >"+mod_name+"</option>");
            }
        }});

    $('select#select-pro').change(function () {
        if($(this).val()!='none'){alert("test");}
        var te=$(this).val();
        //alert(te);
    });

    //根据pro_id 和ver_id 和mod_id进行查找
    $('#api-apilist').click(function(){
        var trans_list=new Array();
        var item={};

    var pro_name=$('select#select-pro').val();
    var ver_name=$('select#select-ver').val();
    var mod_name=$('select#select-mod').val();
    var pro_id=0;
    var ver_id=0;
    var mod_id=0;
    //test表示从上边的接口中获取到的数据
    for (var i=0;i<test.pro_info.length;i++){
        if(pro_name==test.pro_info[i].pro_name){
            pro_id=test.pro_info[i].pro_id;
            break
        }
    }
    for (var i=0;i<test.ver_info.length;i++){
        if(ver_name==test.ver_info[i].ver_name){
            ver_id=test.ver_info[i].ver_id;
            break
        }
    }
    for (var i=0;i<test.mod_info.length;i++){
        if(mod_name==test.mod_info[i].mod_name){
            mod_id=test.mod_info[i].mod_id;
            break
        }
    }


    $.get('/api/case_select_list',{pro_id:pro_id,ver_id:ver_id,mod_id:mod_id},
        function(data){
        for (var i=0;i<data.datas.case_list.length;i++){
                item['importUnitId']=data.datas.case_list[i].inter_id;
                item['importUnitName']=data.datas.case_list[i].case_name;
                item['flag']=false;
                trans_list.push(item);
            }

        $('#transferContainer').transfer('refresh', trans_list);
        });


});
//创建穿梭框

    $('#transferContainer').transfer({

            titles: ['所有可选接口列表', '已选择的接口列表'],
            search: true,
            uniqueId: "importUnitId",//唯一id

            dataSource: null,
            maxSelect: 6,
            diffKey: 'flag',
            unselectColumns: [{
                    field: 'flag',
                    checkbox: true
                },
                {
                    field: 'importUnitName',
                    title: '选择所有接口'
                }
            ]
        });
    });


    //     [{
    //
    //     "importUnitId": "950258484706803712",
    //     "importUnitName": "caca",
    //     "flag": false,
    //
    // },
    // {
    //     "importUnitId": "949202813861232640",
    //     "importUnitName": "对比1",
    //     "flag": false,
    // },
    // {
    //     "importUnitId": "948380218236600320",
    //     "importUnitName": "测试2",
    //     "flag": false,
    // },
    // {
    //     "importUnitId": "946590730653007872",
    //     "importUnitName": "对比4",
    //     "flag": false,
    // },
    // {
    //     "importUnitId": "946590730653007889",
    //     "importUnitName": "对比954",
    //     "flag": true,
    // },
    // {
    //     "importUnitId": "946590730653008647",
    //     "importUnitName": "对比88",
    //     "flag": true,
    // }
    //
    // ]

//点击选择完成之后的按钮
$('#btn').click(function(){
	// var data= $('#transferContainer').transfer('getData', 'selectData', 'importUnitId');
	// console.log(data)
    var h1=document.getElementById('transferContainer');
    var h2=document.getElementById('sence_data');
    if(h1.style.display=='none'){
        h1.style.display='block';
        h2.style.display='none';
    }else{
        h1.style.display='none';
        h2.style.display='block';
    }
    });
// //页面加载时运行
// $(function(){
//     //选择项目时，动态加载该项目下的所有测试套
//     $('select#project').change(function(){
//         if ($(this).val() != 'none'){
//             $.post('/suite', {'type': 'get_suite', 'project': $(this).val()}, function(data){
//                 var obj = $('select#suite');
//                 obj.empty();
//                 var html = '<option value="none">请选择测试套</option>';
//                 for (i=0;i<data.suite.length;i++){
//                     html = html + '<option value="' + data.suite[i] + '">' + data.suite[i] + '</option>';
//                 };
//                 obj.html(html);
//             });
//         }
//         else{
//             $('select#suite').empty();
//             $('select#suite').html('<option value="none">请选择测试套</option>');
//             $('div#suite_data').hide();
//         };
//     });
//
//     $('select#project').get(0).selectedIndex=1
//     $("select#project").trigger("change");
//
//     //选择查看测试套时，加载项目所有
//     $('select#suite').change(function(){
//         if ($(this).val() != 'none'){
//             $('div#suite_data').show();
//             $('div#suite_data').find('tr.dam').remove();
//             //查询该项目的所有场景
//             $.post('/suite', {'type': 'get_scene', 'suite': $(this).val(), 'project': $('select#project').val()}, function(data){
//                 var html = ''
//                 for (i=0;i<data.all_scene.length;i++){
//                     html = html + '<tr class="dam"><td>' + data.all_scene[i] + '</td><td align="center"><button style="padding:1px 12px" class="btn btn-success" id="add">>></button></td></tr>';
//                 };
//                 $('table#all_scene').find('tr').last().after(html);
//                 html = '';
//                 for (i=0;i<data.scene.length;i++){
//                     html = html + '<tr class="dam"><td>' + data.scene[i] + '</td><td align="center"><button style="padding:1px 12px" class="btn btn-success" id="del"><<</button></td></tr>';
//                 };
//                 $('table#my_scene').find('tr').last().after(html);
//             });
//         }
//         else{
//             $('div#suite_data').find('tr.dam').remove();
//             $('div#suite_data').hide();
//         };
//     });
//
//     //场景的添加
//     $('table#all_scene').on('click', 'button#add', function(){
//         var tr = $(this).parents('tr');
//         var scene = tr.find('td').eq(0).text();
//         tr.remove();
//         var html = '<tr class="dam"><td>' + scene + '</td><td align="center"><button class="btn btn-success" id="del" style="padding:1px 12px"><<</button></td></tr>';
//         $('table#my_scene').find('tr').last().after(html)
//     });
//
//     //场景的删除
//     $('table#my_scene').on('click', 'button#del', function(){
//         var tr = $(this).parents('tr');
//         var scene = tr.find('td').eq(0).text();
//         tr.remove();
//         var html = '<tr class="dam"><td>' + scene + '</td><td align="center"><button class="btn btn-success" id="add" style="padding:1px 12px">>></button></td></tr>';
//         $('table#all_scene').find('tr').last().after(html)
//     });
//
//     //测试套修改
//     $('button#modify').on('click', function(){
//         if ($('select#suite').val()=='none'){
//             $("h4#myModalLabel").text("提示");
//             $("div.modal-body").text("请选择要修改的测试套！");
//             $("button#send_alert").trigger("click");
//             return
//         };
//         var trs = $('table#my_scene').find('tr.dam');
//         var scene_data = []
//         for (i=0;i<trs.length;i++){
//             scene_data[i] = trs.eq(i).find('td').eq(0).text();
//         };
//         $.post('/suite', {'type': 'modify_suite', 'data': JSON.stringify(scene_data), 'name': $('select#suite').val(), 'project': $('select#project').val()}, function(data){
//             if (data.code == 200){
//                 $("h4#myModalLabel").text("提示");
//                 $("div.modal-body").text(data.message);
//                 $("button#send_alert").trigger("click");
//             }
//             else{
//                 $("h4#myModalLabel").text("错误");
//                 $("div.modal-body").text("修改测试套失败！");
//                 $("button#send_alert").trigger("click");
//             };
//         });
//
//     });
//
//     // 新增测试套
//     $('button#new_suite').on('click', function(){
//         var project = $('select#project').val();
//         var suite = $('input#suite_name').val();
//         if (project=='' || suite==''){
//             $("h4#myModalLabel").text("提示");
//             $("div.modal-body").text("请选择项目和输入测试套名");
//             $("button#send_alert").trigger("click");
//             return
//         };
//         $.post('/suite', {'type': 'new_suite', 'suite': suite, 'project': project}, function(data){
//             $("h4#myModalLabel").text("提示");
//             $("div.modal-body").text(data.msg);
//             $("button#send_alert").trigger("click");
//             if (data.msg=="新增测试套成功"){
//                 $('select#suite').append('<option value="'+suite+'">'+suite+'</option>');
//                 $('select#suite').val(suite);
//                 $('select#suite').trigger("change");
//                 $('input#suite_name').val('')
//             }
//         });
//     });
//
//     // 删除测试套
//     $('button#del_s').on('click', function(){
//         var project = $('select#project').val();
//         var suite = $('select#suite').val();
//         if (project=='' || suite==''){
//             $("h4#myModalLabel").text("提示");
//             $("div.modal-body").text("请选择要删除的测试套");
//             $("button#send_alert").trigger("click");
//             return
//         };
//         $.post('/suite', {'type': 'del_suite', 'suite': suite, 'project': project}, function(data){
//             $("h4#myModalLabel").text("提示");
//             $("div.modal-body").text(data.msg);
//             $("button#send_alert").trigger("click");
//             if (data.msg=="删除成功"){
//                 $('select#suite option[value="'+suite+'"]').remove();
//                 $('select#suite').get(0).selectedIndex=0
//                 $('select#suite').trigger("change");
//             }
//         });
//     });
// });