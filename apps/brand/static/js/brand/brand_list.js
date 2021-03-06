
var brandListPageVue = new CommonListPageVue({
        data: {
            // API
            list_api_tag:   'api:brand-list',
            detail_api_tag: 'api:brand-detail',
            delete_api_tag: 'api:brand-delete',
            // page
            create_url_tag: 'brand:brand-add',
            list_url_tag:   'brand:brand-list',
            update_url_tag: 'brand:brand-update',
            detail_url_tag: 'brand:brand-detail',
            list_url:       Urls['api:brand-list']()
        }
    }
);
