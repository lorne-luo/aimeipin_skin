var premiumProductListPageVue = new CommonListPageVue({
        data: {
            // API
            list_api_tag:   'api:premiumproduct-list',
            detail_api_tag: 'api:premiumproduct-detail',
            delete_api_tag: 'api:premiumproduct-delete',
            // page
            create_url_tag: 'premium_product:premiumproduct-add',
            list_url_tag:   'premium_product:premiumproduct-list',
            update_url_tag: 'premium_product:premiumproduct-update',
            detail_url_tag: 'premium_product:premiumproduct-detail',
            list_url:       Urls['api:premiumproduct-list']()
        }
    }
);
