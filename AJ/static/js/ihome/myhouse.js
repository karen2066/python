$(document).ready(function(){
    $(".auth-warn").show();
})

// 用get请求加载
$.get('/user/auths/', function (msg){
    // 如果请求成功
    if(msg.code == '200'){
        // 如果能够拿到id_name，就说明已经实名认证了
        if(msg.data.id_name){
            // 就把要求实名认证的提示隐藏起来
            $('.auth-warn').hide()
            $('#houses-list').show()
        }else {
            $('.auth-warn').show()
            $('#houses-list').hide()
        }
    }
});