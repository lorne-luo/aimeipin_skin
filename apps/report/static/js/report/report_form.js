jQuery(document).ready(function ($) {
    $('.premiumproduct-name').click(function () {
        premiumProductSearch(this);
        $(this).closest('table').next().removeClass('hide');
    }).focus(function () {
        // premiumProductSearch(this);
    }).blur(function () {
        var self = this;
        setTimeout(function () {
            $(self).closest('table').next().addClass('hide');
        }, 200);
    }).on('input', function () {
        premiumProductSearch(this);
        $(this).closest('table').next().removeClass('hide');
    });

    $('.premiumproduct-skin_type').focus(function () {
        premiumProductSearch(this);
    }).blur(function () {
        $(this).closest('table').next().addClass('hide');
    }).on('change', function () {
        premiumProductSearch(this);
        $(this).closest('table').next().removeClass('hide');
    });

    $('.premiumproduct-purpose').focus(function () {
        premiumProductSearch(this);
    }).blur(function () {
        $(this).closest('table').next().addClass('hide');
    }).on('change', function () {
        premiumProductSearch(this);
        $(this).closest('table').next().removeClass('hide');
    });

    $('.premiumproduct-category').focus(function () {
        premiumProductSearch(this);
    }).blur(function () {
        $(this).closest('table').next().addClass('hide');
    }).on('change', function () {
        premiumProductSearch(this);
        $(this).closest('table').next().removeClass('hide');
    });

});

function premiumProductSearch(event) {
    var search = $(event).closest('table').find('#id_premiumproduct_select-name').val();
    var skin_type = $(event).closest('table').find('#id_premiumproduct_select-skin_type').val();
    var purpose = $(event).closest('table').find('#id_premiumproduct_select-purpose').val();
    var category = $(event).closest('table').find('#id_premiumproduct_select-category').val();
    var ul = $(event).closest('table').next();

    data = {};
    if (skin_type !== '------') {
        data['skin_type'] = skin_type;
    }
    if (purpose !== '------') {
        data['purpose'] = purpose;
    }
    if (category !== '------') {
        data['category'] = category;
    }

    console.log(JSON.stringify(data));

    $.ajax({
        url: "/api/premium_product/premium_product/search/",
        type: "GET",
        data: {'forward': JSON.stringify(data), 'q': search},
        dataType: "JSON",
        success: function (data) {
            var productOptions = '';
            for (var i = 0; i < data.results.length; i++) {
                if (data.results.length > 50) {
                    productOptions += '<li data-id="' + data.results[i].id + '" onclick="productClick(this)">' +
                        '<span>' + data.results[i].text + '</span>' +
                        '</li>';
                } else {
                    productOptions += '<li data-id="' + data.results[i].id + '" onclick="productClick(this)">' +
                        '<img src="' + data.results[i].image + '">' +
                        '<span>' + data.results[i].text + '</span>' +
                        '</li>';
                }

            }
            ul.html(productOptions);
        },
        error: function () {
            productOptions = '';
        }
    });
}

function productClick(event) {
    var name = $(event).text();
    var id = $(event).attr('data-id');
    console.log(name);
    console.log(id);

    var addButton = $(event).closest("div.formset-div").find('.formset-add');
    console.log(addButton);
    addButton.trigger("click", [id, name]);
}