/**
 * Created by SvenWeng on 2017/3/28.
 */
$(document).ready(function () {
    CheckLogin()
});

function CheckLogin() {
    var userToken = localStorage.getItem(['loginToken']);
    if (userToken) {
        data = {
            'usertoken': userToken
        };
        $.get('/usergroup/checktoken/', data, function (result) {
            if (result['error_no'] == 'UG0000') {
                $("#nickname").html(result['nickname'] + '<span class="caret"></span>');
                $("#title").text('欢迎您! ' + result['nickname'])
            }else {
                alert(result['error_msg']);
                window.location.href = '/usergroup/'
            }
        })
    } else {
        alert("您暂未登录");
        window.location.href = '/usergroup/'
    }

}
