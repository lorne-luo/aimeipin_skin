$(document).ready(function () {
    document.getElementById("file1").addEventListener("change", function () {
        $(this).css('opacity', '1');
        $(this).next().css('opacity', '0');
    });
    document.getElementById("file2").addEventListener("change", function () {
        $(this).css('opacity', '1');
        $(this).next().css('opacity', '0');
    });
    document.getElementById("file3").addEventListener("change", function () {
        $(this).css('opacity', '1');
        $(this).next().css('opacity', '0');
    });


    $('.hufupin>span>i').click(function () {
        console.log('.hufupin>span>i');
        var search = "";
        ullistSearch(search);
        $(this).parent().next().toggleClass('active');
    });

    $('.hufupin span input.onkeyDownSearch').focus(function () {
        console.log('input.focus');
        var search = "";
        ullistSearch(search);
        $(this).parent().next().addClass('active');
    }).blur(function (event) {
        var self = this;
        console.log('input.blur');
        console.log(event);
        setTimeout(function () {
            $(self).parent().next().removeClass('active');
        }, 500);
    });

    // $("*").not("[cate]").click(function (e) {
    //     $("ul[cate]").removeClass('active');
    // });

    $('.onkeyDownSearch').keyup(function (e) {
        if (e.keyCode == 37 || e.keyCode == 38 || e.keyCode == 39 || e.keyCode == 40) {
            return;
        } else {
            var search = $(this).val();
            console.log('search:' + search);
            ullistSearch(search);
        }
        $(this).parent().next().addClass('active')
    });

});

function ullistSearch(search) {
    $.ajax({
        url: "/api/brand/brand/autocomplete/",
        type: "GET",
        data: {'q': search},
        dataType: "JSON",
        success: function (data) {
                var opt1 = '';
                for (var i = 0; i < data.results.length; i++) {
                    opt1 += '<li data-id="' + data.results[i].id + '" onclick="selChange(this)">' + data.results[i].text + '</li>';
                }
                $('.hufupin .hufupin1').html(opt1);
                $('.hufupin .hufupin11').html(opt1);
                $('.hufupin .hufupin12').html(opt1);
                $('.hufupin .hufupin13').html(opt1);
                $('.hufupin .hufupin14').html(opt1);
                $('.hufupin .hufupin15').html(opt1);
                $('.hufupin .hufupin16').html(opt1);
        },
        error: function () {
        }
    });
}


function selChange(tsel) {
    var opt2 = '';
    $(tsel).parent().next().val("请选择产品")
    var id = {'id': $(tsel).attr('data-id'), 'cate': $(tsel).parent().attr('cate')};
    $(tsel).parent().prev().find('input').val($(tsel).html())
    $(tsel).parent().prev().find('input').attr('data-id', $(tsel).attr('data-id'))
    $(tsel).parent().removeClass('active')
    $.ajax({
        url: "http://servers.jianghujoy.cn:8084/index.php/product/brand_product",
        type: "POST",
        dataType: "JSON",
        data: id,
        success: function (data) {
            if (data.code == 10000) {
                for (var i = 0; i < data.msg.length; i++) {
                    opt2 += '<li data-id="' + data.msg[i].id + '" onclick="liClick(this)">' +
                        '<img src="' + data.msg[i].image + '">' +
                        '<span>' + data.msg[i].name + '</span>' +
                        '</li>';
                }
                $(tsel).parent().next().next().next().html(opt2)
            } else {
                $(tsel).parent().next().next().next().html("")
            }
        },
        error: function () {
        }
    });
}

function spanClick(span) {
    if ($(span).next().next().children().length == 0) {
//             alert("此品牌无产品！");
        var bodyHeight = parseFloat($('body').css('height')) + 60;
        $('#mask').css('height', bodyHeight + "px");
        $('#mask').show();
        $('#mask>div>textarea').html("此品牌无产品!");
        $('#goon').on('click', function () {
            $('#mask').hide();
        })
        return;

    }
    $(span).next().next().toggleClass('active');
}

function liClick(li) {
    $(li).parent().prev().prev().val($(li).find('span').html());
    $(li).parent().prev().prev().attr('data-id', $(li).attr('data-id'));
    $(li).parent().removeClass('active')
}

function add(aaa) {
//    var lilist = " ";
//    $(aaa).parent().html("");
    var sel = $(aaa).prev().prev().prev().prev().prev().find('input').val();
    var id = $(aaa).prev().prev().prev().attr('data-id');
    var spa = $(aaa).prev().prev().prev().val();
    var inputSear = $(aaa).prev().prev().val();
    var reg = /^[0-9]{1,1000}$/;
    var ssspa = sel + spa;
    if (id == undefined && inputSear.length == 0) {
//        alert("请选择产品！")
        var bodyHeight = parseFloat($('body').css('height')) + 60;
        $('#mask').css('height', bodyHeight + "px");
        $('#mask').show();
        $('#mask>div>textarea').html("请选择产品!");
        $('#goon').on('click', function () {
            $('#mask').hide();
        })
        return;
    } else if (reg.test(inputSear)) {
//        alert("产品输入不能为数字！")
        var bodyHeight = parseFloat($('body').css('height')) + 60;
        $('#mask').css('height', bodyHeight + "px");
        $('#mask').show();
        $('#mask>div>textarea').html("产品输入不能为数字!");
        $('#goon').on('click', function () {
            $('#mask').hide();
        })
        return;
    } else if (id != undefined && inputSear.length == 0) {
        var ppp = 0;
        $(aaa).next().find('b').each(function (i, val) {
            if (ssspa == $(aaa).next().find('b')[i].innerHTML) {
//                alert('请不要添加重复产品！')
                $('#mask').css('height', bodyHeight + "px");
                $('#mask').show();
                $('#mask>div>textarea').html("请不要添加重复产品!");
                $('#goon').on('click', function () {
                    $('#mask').hide();
                })
                ppp = 1
                return;
            }
        })
        if (ppp == 0) {
            var lilist = '<li data-id="' + id + '"><b>' + ssspa + '</b><span onclick="del(this)">删除</span></li>';
        }
    } else if (id == undefined && inputSear.length != 0) {
        var ppp1 = 0;
        $(aaa).next().find('b').each(function (i, val) {
            if (inputSear == $(aaa).next().find('b')[i].innerHTML) {
//                alert('请不要添加重复产品！')
                $('#mask').css('height', bodyHeight + "px");
                $('#mask').show();
                $('#mask>div>textarea').html("请不要添加重复产品!");
                $('#goon').on('click', function () {
                    $('#mask').hide();
                })
                ppp1 = 1
                return;
            }
        })
        if (ppp1 == 0) {
            var lilist = '<li data-id="' + inputSear + '"><b>' + inputSear + '</b><span onclick="del(this)">删除</span></li>';
        }
    } else if (id != undefined && inputSear.length != 0) {
        var ppp2 = 0;
        $(aaa).next().find('b').each(function (i, val) {
            if (ssspa == $(aaa).next().find('b')[i].innerHTML || inputSear == $(aaa).next().find('b')[i].innerHTML) {
//                alert('请不要添加重复产品！')
                $('#mask').css('height', bodyHeight + "px");
                $('#mask').show();
                $('#mask>div>textarea').html("请不要添加重复产品!");
                $('#goon').on('click', function () {
                    $('#mask').hide();
                })
                ppp2 = 1
                return;
            }
        })
        if (ppp2 == 0) {
            var lilist = '<li data-id="' + id + '"><b>' + ssspa + '</b><span onclick="del(this)">删除</span></li>' +
                '<li data-id="' + inputSear + '"><b>' + inputSear + '</b><span onclick="del(this)">删除</span></li>';
        }
    }
    $(aaa).prev().prev().val('');
    $(aaa).prev().prev().prev().val('请选择产品');
    $(aaa).prev().prev().prev().removeAttr('data-id');
    $(aaa).prev().prev().prev().prev().prev().find('input').val('');
    $(aaa).prev().prev().prev().prev().prev().find('input').removeAttr('data-id');
    $(aaa).next().append(lilist);
    $(aaa).prev().html("");
}

function del(ddd) {
    $(ddd).parent().remove();
}


function bthClick() {
    var re_name = "";
    var skin_name = "";
    var skin_w_name = "";
    var skin_m_name = "";
    var elite_name = "";
    var facial_name = "";
    var s_name = "";
    $("#re_name li").each(function () {
        re_name += $(this).attr('data-id') + ',';
    });
    re_name = re_name.substring(0, re_name.length - 1);
    $('.re_name').val(re_name)
    $("#skin_name li").each(function () {
        skin_name += $(this).attr('data-id') + ',';
    });
    skin_name = skin_name.substring(0, skin_name.length - 1);
    $('.skin_name').val(skin_name)
    $("#skin_w_name li").each(function () {
        skin_w_name += $(this).attr('data-id') + ',';
    });
    skin_w_name = skin_w_name.substring(0, skin_w_name.length - 1);
    $('.skin_w_name').val(skin_w_name)
    $("#skin_m_name li").each(function () {
        skin_m_name += $(this).attr('data-id') + ',';
    });
    skin_m_name = skin_m_name.substring(0, skin_m_name.length - 1);
    $('.skin_m_name').val(skin_m_name)
    $("#elite_name li").each(function () {
        elite_name += $(this).attr('data-id') + ',';
    });
    elite_name = elite_name.substring(0, elite_name.length - 1);
    $('.elite_name').val(elite_name)
    $("#facial_name li").each(function () {
        facial_name += $(this).attr('data-id') + ',';
    });
    facial_name = facial_name.substring(0, facial_name.length - 1);
    $('.facial_name').val(facial_name)
    $("#s_name li").each(function () {
        s_name += $(this).attr('data-id') + ',';
    });
    s_name = s_name.substring(0, s_name.length - 1);
    $('.s_name').val(s_name)

    var quesArray = [];
    quesArray[0] = $("input[name='name']").val()
    quesArray[1] = $("input[name='sex']:checked").val()
    quesArray[2] = $("#file1").val()
    quesArray[3] = "第4题"
    quesArray[4] = "第5题"
    quesArray[5] = $("input[name='age']").val()
    if ($("input[name='height']").val() == "" || $("input[name='weight']").val() == "") {
        quesArray[6] = ""
    } else {
        quesArray[6] = $("input[name='height']").val() + $("input[name='weight']").val();
    }
    quesArray[7] = $("input[name='work']").val()
    quesArray[8] = $("input[name='pay']:checked").val()
    quesArray[9] = $("input[name='weixin']").val()
    quesArray[10] = $("input[name='phone']").val()
    quesArray[11] = $("input[name='question1']:checked").val()
    quesArray[12] = $("input[name='question2']:checked").val()
    quesArray[13] = $("input[name='question3']:checked").val()
    quesArray[14] = $("input[name='question4']:checked").val()
    quesArray[15] = $("input[name='question5']:checked").val()
    quesArray[16] = $("input[name='question6']:checked").val()
    quesArray[17] = $("input[name='question7']:checked").val()
    quesArray[18] = $("input[name='question8']:checked").val()
    quesArray[19] = $("input[name='question9']:checked").val()
    quesArray[20] = $("input[name='question10']:checked").val()
    quesArray[21] = $("input[name='question11']:checked").val()
    quesArray[22] = $("input[name='question12']:checked").val()
    quesArray[23] = $("input[name='question13']:checked").val()
    quesArray[24] = $("input[name='question14']:checked").val()
    quesArray[25] = $("input[name='question15']:checked").val()
    quesArray[26] = $("input[name='question16']:checked").val()
    quesArray[27] = $("input[name='question17']:checked").val()
    quesArray[28] = $("input[name='question18']:checked").val()
    quesArray[29] = $("input[name='question19']:checked").val()
    quesArray[30] = $("input[name='question20']:checked").val()
    quesArray[31] = $("input[name='question21']:checked").val()
    quesArray[32] = $("input[name='question22']:checked").val()
    quesArray[33] = $("input[name='question23']:checked").val()
    quesArray[34] = $("input[name='question24']:checked").val()
    quesArray[35] = $("input[name='question25']:checked").val()
    quesArray[36] = $("input[name='question26']:checked").val()
    quesArray[37] = $("input[name='question27']:checked").val()
    quesArray[38] = $("input[name='question28']:checked").val()
    quesArray[39] = $("input[name='question29']:checked").val()
    quesArray[40] = $("input[name='question30']:checked").val()
    quesArray[41] = $("input[name='question31']:checked").val()
    quesArray[42] = $("input[name='question32']:checked").val()
    quesArray[43] = $("input[name='question33']:checked").val()
    quesArray[44] = $("input[name='question34']:checked").val()
    quesArray[45] = $("input[name='question35']:checked").val()
    quesArray[46] = $("input[name='question36']:checked").val()
    quesArray[47] = $("input[name='question37']:checked").val()
    quesArray[48] = $("input[name='question38']:checked").val()
    quesArray[49] = $("input[name='toilet']:checked").val()
    quesArray[50] = $("input[name='day1']:checked").val()
    quesArray[51] = $("input[name='day2']:checked").val()
    quesArray[52] = $("input[name='day3']:checked").val()
    quesArray[53] = $("input[name='day4']:checked").val()
    quesArray[54] = $("input[name='day5']:checked").val()
    quesArray[55] = $("input[name='night1']:checked").val()
    quesArray[56] = $("input[name='night2']:checked").val()
    quesArray[57] = $("input[name='night3']:checked").val()
    quesArray[58] = $("input[name='night4']:checked").val()
    quesArray[59] = $("input[name='night5']:checked").val()
    quesArray[60] = $("input[name='night6']:checked").val()
    quesArray[61] = $("input[name='night7']:checked").val()
    quesArray[62] = $("input[name='mr']:checked").val()
    quesArray[63] = $("input[name='illness']:checked").val()
    quesArray[64] = re_name
    quesArray[65] = skin_name
    quesArray[66] = skin_w_name
    quesArray[67] = skin_m_name
    quesArray[68] = elite_name
    quesArray[69] = facial_name
    quesArray[70] = s_name
    quesArray[71] = $("#textarea1").val()
    quesArray[72] = $("#textarea2").val()


    var str = "";
    for (var i = 0; i < quesArray.length; i++) {
        if (quesArray[i] == "" || quesArray[i] == undefined) {
            str += (i + 1) + ',';
        }
    }
    if (str != "") {
        str = str.slice(0, str.length - 1)
        var bodyHeight = parseFloat($('body').css('height')) + 60;
        $('#mask').css('height', bodyHeight + "px");
//                  $('#mask>div').css('marginTop',(bodyHeight-500)+"px");
        $('#mask').show();
        $('#mask>div>textarea').html("第" + str + "题没有填写，请填写完成");
        $('#goon').on('click', function () {
            $('#mask').hide();
        })
    } else {

//              var regPhone = /^1[3|4|5|7|8][0-9]{9}$/;
//              if($('#phone').val()==""||!regPhone.test($('#phone').val())){
//                  $('#mask').show();
//                  $('#mask>div>textarea').html("请输入正确格式电话号码！");
//                  $('#goon').on('click',function(){
//                      $('#mask').hide();
//                  })
//              }

        var formData = new FormData($('#form')[0]);
        var status = location.search.split("=")[1];
        $.ajax({
            url: "/index.php/index/judge?status=" + status,
            type: "POST",
            dataType: "JSON",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                if (data.code == 10000) {
                    var id = data.msg.user_id;
                    var time = data.msg.time;
                    window.localStorage.setItem('id', id);
                    window.localStorage.setItem('time', time);
                    window.location.href = 'score.html';
                } else {
                    alert(data.msg)
                }
            },
            error: function () {
            }
        });
    }
}