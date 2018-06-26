$(document).ready(function () {
    $('.hufupin>span>i').click(function () {
        // console.log('.hufupin>span>i');
        var search = "";
        brandSearch(search);
        $(this).parent().next().toggleClass('active');
    });

    $('.hufupin span input.onkeyDownSearch').focus(function () {
        // console.log('input.focus');
        var search = "";
        brandSearch(search);
        $(this).parent().next().addClass('active');
    }).blur(function (event) {
        var self = this;
        // console.log('input.blur');
        setTimeout(function () {
            $(self).parent().next().removeClass('active');
        }, 400);
    });

    $('.onkeyDownSearch').on('keypress touchend', function (e) {
        // console.log(e);
        // console.log(e.keyCode);
        if (e.keyCode == 37 || e.keyCode == 38 || e.keyCode == 39 || e.keyCode == 40) {
            return;
        }

        var search = $(this).val();
        // console.log('search:' + search);
        brandSearch(search);
        $(this).parent().next().addClass('active')
    });

    $('.hufupin input.span1').focus(function (event) {
        // console.log("span1 focus");
        if ($(this).val()) {
            $(this).next().addClass('active');
        }
    }).blur(function (event) {
        var self = this;
        setTimeout(function () {
            $(self).next().removeClass('active');
        }, 400);
    }).on('keydown', function (e) {
        if (e.keyCode == 37 || e.keyCode == 38 || e.keyCode == 39 || e.keyCode == 40) {
            $(this).trigger('input');
        }
    }).on('input', function (e) {
        // if (e.keyCode == 37 || e.keyCode == 38 || e.keyCode == 39 || e.keyCode == 40) {
        //     return;
        // }
        var self = this;
        var category = $(this).data('category');

        var productsUl = $(this).next();

        var search = $(this).val();
        if (!search) {
            productsUl.html('<li>请输入名称...</li>');
            return;
        }

        var brand_id = $(this).attr('data-brand_id');

        productsUl.html('<li>查询中...</li>');
        $.ajax({
            url: "/api/product/product/search/",
            type: "GET",
            data: {'q': search, 'brand_id': brand_id, 'category': category},
            dataType: "JSON",
            success: function (data) {

                if (data.results.length === 0) {
                    productsUl.html('<li>没有搜索到库内产品，请从下方手动输入产品名称.</li>');
                    return;
                }

                var opt2 = '';
                for (var i = 0; i < data.results.length; i++) {
                    if (data.results.length > 50) {
                        opt2 += '<li data-id="' + data.results[i].id + '" onclick="productClick(this)">' +
                            '<span>' + data.results[i].text + '</span>' +
                            '</li>';
                    } else {
                        opt2 += '<li data-id="' + data.results[i].id + '" onclick="productClick(this)">' +
                            '<img src="' + data.results[i].image + '">' +
                            '<span>' + data.results[i].text + '</span>' +
                            '</li>';
                    }
                }
                productsUl.html(opt2);
            },
            error: function () {
            }
        });
        $(this).next().addClass('active');
    });

});

function brandSearch(search) {
    // brand input box selected, query brand from server
    $.ajax({
        url: "/api/brand/brand/search/",
        type: "GET",
        data: {'q': search},
        dataType: "JSON",
        success: function (data) {
            var brandOptions = '';
            for (var i = 0; i < data.results.length; i++) {
                brandOptions += '<li data-id="' + data.results[i].id + '" onclick="brandClick(this)">' + data.results[i].text + '</li>';
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


function brandClick(tsel) {
    // brand selected, query product with brand_id, and popup product selection window
    // console.log('brand selected');
    var opt2 = '';
    var id = {'id': $(tsel).attr('data-id'), 'cate': $(tsel).parent().attr('cate')};
    var brand_id = $(tsel).attr('data-id');
    $(tsel).parent().prev().find('input').val($(tsel).html());
    $(tsel).parent().prev().find('input').attr('data-id', brand_id);
    $(tsel).parent().next().attr('data-brand_id', brand_id);
    $(tsel).parent().removeClass('active');
    var search = '';
    var productInput = $(tsel).parent().next();
    productInput.prop("disabled", false);

    $.ajax({
        url: "/api/product/product/search/",
        type: "GET",
        data: {'q': search, 'brand_id': brand_id},
        dataType: "JSON",
        success: function (data) {
            for (var i = 0; i < data.results.length; i++) {
                opt2 += '<li data-id="' + data.results[i].id + '" onclick="productClick(this)">' +
                    '<img src="' + data.results[i].image + '">' +
                    '<span>' + data.results[i].text + '</span>' +
                    '</li>';
            }
            $(tsel).parent().next().next().html(opt2);
            productInput.attr('placeholder', '输入名称检索');
            productInput.trigger('focus');
        },
        error: function () {
            $(tsel).parent().next().next().html("");
        }
    });
}

function productClick(li) {
    // product selected from product list
    // console.log('product selected');
    $(li).parent().prev().val('');
    $(li).parent().removeClass('active');

    var name = $(li).text();
    var id = $(li).attr('data-id');
    var addButton = $(li).parent().parent().next().find('.formset-add');
    addButton.trigger("click", [id, name]);

}

function add(aaa) {
    // console.log('add product by name');
    var input = $(aaa).prev();
    if (input.val()) {
        var addButton = $(aaa).next().find('.formset-add');
        addButton.trigger("click", [null, input.val()]);
        input.val('');
        input.focus();
    }
}

function del(ddd) {
    $(ddd).parent().remove();
}
