
var skintypeListPageVue = new CommonListPageVue({
        data: {
            // API
            list_api_tag:   'api:skintype-list',
            detail_api_tag: 'api:skintype-detail',
            delete_api_tag: 'api:skintype-delete',
            // page
            create_url_tag: 'analysis:skintype-add',
            list_url_tag:   'analysis:skintype-list',
            update_url_tag: 'analysis:skintype-update',
            detail_url_tag: 'analysis:skintype-detail',
            list_url:       Urls['api:skintype-list'](),
            ordering:'dimension,lower_bound'
        }
    }
);
