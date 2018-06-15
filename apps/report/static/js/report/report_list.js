var ReportListPageVue = CommonListPageVue.extend({
    methods: {
        update_delivered: function (id, event) {
            var currentValue = $(event.target).hasClass('active');
            var target = $(event.target);
            var text = !currentValue ? '可以' : '不可';
            var url = Urls[this.detail_api_tag](id);

            swal({
                title: "更改可否修改",
                text: "确认将问卷变更为\"" + text + "\"修改?",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                closeOnConfirm: true,
                showLoaderOnConfirm: false,
                animation: false
            }, function () {
                $.AdminLTE.apiPost(
                    url,
                    $.param({'is_delivered': !currentValue}),
                    function (resp) {
                        if (currentValue) {
                            target.removeClass('active');
                            target.removeClass('btn-success');
                            target.addClass('btn-danger');
                            target.text('否');
                        } else {
                            target.addClass('active');
                            target.removeClass('btn-danger');
                            target.addClass('btn-success');
                            target.text('是');
                        }
                    }
                );
            });


        }
    }
});

var reportListPageVue = new ReportListPageVue({
        data: {
            // API
            list_api_tag: 'api:report-list',
            detail_api_tag: 'api:report-detail',
            delete_api_tag: 'api:report-delete',
            // page
            create_url_tag: 'report:report-add',
            list_url_tag: 'report:report-list',
            update_url_tag: 'report:report-update',
            detail_url_tag: 'report:report-detail',
            list_url: Urls['api:report-list'](),
            ordering:'-modified_at'
        }
    }
);
