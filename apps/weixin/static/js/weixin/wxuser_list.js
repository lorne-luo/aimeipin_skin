
var wxUserListPageVue = new CommonListPageVue({
        data: {
            // API
            list_api_tag:   'api:wxuser-list',
            detail_api_tag: 'api:wxuser-detail',
            delete_api_tag: 'api:wxuser-delete',
            // page
            list_url_tag:   'weixin:wxuser-list',
            detail_url_tag: 'weixin:wxuser-detail',
            list_url:       Urls['api:wxuser-list']()
        }
    }
);
