var reportListPageVue = new CommonListPageVue({
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
            list_url: Urls['api:report-list']()
        }
    }
);
