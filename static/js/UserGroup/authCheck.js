/**
 * Created by SvenWeng on 2017/3/28.
 */
$(document).ready(function () {
    authCheck(99)
});

function authCheck(level) {
    var userToken = localStorage.getItem(['loginToken']);
    if (userToken) {
        data = {
            'usertoken': userToken,
            'level': level
        };
        $.get('/usergroup/checkauth/', data, function (result) {
            if (result['error_no'] == 'UG0000') {
                $("#title").text('新增用户')
            }else {
                alert(result['error_msg']);
                window.location.href = '/usergroup/usercenter/'
            }
        })
    }else {
        alert("您暂未登录");
        window.location.href = '/usergroup/'
    }
}