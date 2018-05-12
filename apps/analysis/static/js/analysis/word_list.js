
var wordListPageVue = new CommonListPageVue({
        data: {
            // API
            list_api_tag:   'api:word-list',
            detail_api_tag: 'api:word-detail',
            delete_api_tag: 'api:word-delete',
            // page
            create_url_tag: 'analysis:word-add',
            list_url_tag:   'analysis:word-list',
            update_url_tag: 'analysis:word-update',
            detail_url_tag: 'analysis:word-detail',
            list_url:       Urls['api:word-list']()
        }
    }
);
