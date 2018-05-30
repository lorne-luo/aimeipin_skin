$(document).ready(function () {
    $('.hufupin>span>i').click(function () {
        // console.log('.hufupin>span>i');
        var search = "";
        ullistSearch(search);
        $(this).parent().next().toggleClass('active');
    });

    $('.hufupin span input.onkeyDownSearch').focus(function () {
        // console.log('input.focus');
        var search = "";
        ullistSearch(search);
        $(this).parent().next().addClass('active');
    }).blur(function (event) {
        var self = this;
        // console.log('input.blur');
        // console.log(event);
        setTimeout(function () {
            $(self).parent().next().removeClass('active');
        }, 200);
    });

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

    $('.hufupin input.span1').focus(function (event) {
        if ($(this).attr('data-brand_id')) {
            $(this).next().addClass('active');
        }
    }).blur(function (event) {
        var self = this;
        setTimeout(function () {
            $(self).next().removeClass('active');
        }, 200);
    }).keyup(function (e) {
        if (e.keyCode == 37 || e.keyCode == 38 || e.keyCode == 39 || e.keyCode == 40) {
            return;
        } else {
            var search = $(this).val();
            var self = this;
            console.log('search:' + search);
            var brand_id = $(this).attr('data-brand_id');
            console.log('brand_id:' + brand_id);

            $.ajax({
                url: "/api/product/product/autocomplete/",
                type: "GET",
                data: {'q': search, 'brand_id': brand_id},
                dataType: "JSON",
                success: function (data) {
                    var opt2 = '';
                    for (var i = 0; i < data.results.length; i++) {
                        opt2 += '<li data-id="' + data.results[i].id + '" onclick="liClick(this)">' +
                            '<img src="' + data.results[i].image + '">' +
                            '<span>' + data.results[i].text + '</span>' +
                            '</li>';
                    }
                    $(self).next().html(opt2)
                },
                error: function () {
                }
            });
        }
        $(this).next().addClass('active');
    });

});

function ullistSearch(search) {
    $.ajax({
        url: "/api/brand/brand/autocomplete/",
        type: "GET",
        data: {'q': search},
        dataType: "JSON",
        success: function (data) {
            var brandOptions = '';
            for (var i = 0; i < data.results.length; i++) {
                brandOptions += '<li data-id="' + data.results[i].id + '" onclick="selChange(this)">' + data.results[i].text + '</li>';
            }
            $('.hufupin .hufupin1').html(brandOptions);
            $('.hufupin .hufupin11').html(brandOptions);
            $('.hufupin .hufupin12').html(brandOptions);
            $('.hufupin .hufupin13').html(brandOptions);
            $('.hufupin .hufupin14').html(brandOptions);
            $('.hufupin .hufupin15').html(brandOptions);
            $('.hufupin .hufupin16').html(brandOptions);
        },
        error: function () {
            brandOptions = '';
        }
    });

}


function selChange(tsel) {
    // console.log('selChange');
    var opt2 = '';
    // $(tsel).parent().next().val("请选择产品");
    var id = {'id': $(tsel).attr('data-id'), 'cate': $(tsel).parent().attr('cate')};
    var brand_id = $(tsel).attr('data-id');
    $(tsel).parent().prev().find('input').val($(tsel).html());
    $(tsel).parent().prev().find('input').attr('data-id', brand_id);
    $(tsel).parent().next().attr('data-brand_id', brand_id);
    $(tsel).parent().removeClass('active');
    var search = '';

    $.ajax({
        url: "/api/product/product/autocomplete/",
        type: "GET",
        data: {'q': search, 'brand_id': brand_id},
        dataType: "JSON",
        success: function (data) {
            for (var i = 0; i < data.results.length; i++) {
                opt2 += '<li data-id="' + data.results[i].id + '" onclick="liClick(this)">' +
                    '<img src="' + data.results[i].image + '">' +
                    '<span>' + data.results[i].text + '</span>' +
                    '</li>';
            }
            $(tsel).parent().next().next().html(opt2);
        },
        error: function () {
            $(tsel).parent().next().next().html("");
        }
    });
}

function spanClick(span) {
    return;
    if ($(span).next().next().children().length == 0) {
//             alert("此品牌无产品！");
        var bodyHeight = parseFloat($('body').css('height')) + 60;
        $('#mask').css('height', bodyHeight + "px");
        $('#mask').show();
        $('#mask>div>textarea').html("此品牌无产品!");
        $('#goon').on('click', function () {
            $('#mask').hide();
        });
        return;

    }
    $(span).next().next().toggleClass('active');
}

function liClick(li) {
    $(li).parent().prev().val('');
    // $(li).parent().prev().prev().attr('data-id', $(li).attr('data-id'));
    $(li).parent().removeClass('active');
    var name = $(li).text();
    var id = $(li).attr('data-id');
    var lilist = '<li data-id="' + id + '"><b>' + name + '</b><span onclick="del(this)">删除</span></li>';
    $(li).parent().parent().next().find('ul.ulcontainer').append(lilist);
}

function add(aaa) {
    // add product by name
    var input = $(aaa).prev();
    if (input.val()) {
        var li = '<li data-id=""><b>' + input.val() + '</b><span onclick="del(this)">删除</span></li>';
        $(aaa).next().append(li);
        input.val('');
        input.focus();
    }
}

function del(ddd) {
    $(ddd).parent().remove();
}


function bthClick() {
    // swal({
    //   title: "Good job!",
    //   text: "You clicked the button!",
    //   icon: "success",
    // });
}
