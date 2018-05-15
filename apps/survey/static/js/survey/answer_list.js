var answerListPageVue = new CommonListPageVue({
        data: {
            // API
            list_api_tag: 'api:answer-list',
            detail_api_tag: 'api:answer-detail',
            delete_api_tag: 'api:answer-delete',
            // page
            create_url_tag: 'survey:answer-add',
            list_url_tag: 'survey:answer-list',
            update_url_tag: 'survey:answer-update',
            detail_url_tag: 'survey:answer-detail',
            list_url: Urls['api:answer-list']()
        }
    }
);
