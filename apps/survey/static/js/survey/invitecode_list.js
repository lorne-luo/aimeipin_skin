
var invitecodeListPageVue = new CommonListPageVue({
        data: {
            // API
            list_api_tag:   'api:invitecode-list',
            detail_api_tag: 'api:invitecode-detail',
            delete_api_tag: 'api:invitecode-delete',
            // page
            create_url_tag: 'survey:invitecode-add',
            list_url_tag:   'survey:invitecode-list',
            update_url_tag: 'survey:invitecode-update',
            detail_url_tag: 'survey:invitecode-detail',
            list_url:       Urls['api:invitecode-list']() + '?',
            ordering:'-expiry_at,-id'
        }
    }
);
