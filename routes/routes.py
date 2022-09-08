all_routes = {
    'account': {
        'new': '/account/new',
        'update': '/account/update/{username}/{password}/mobile/{mobile}',
        'delete': '/account/delete/{id}',
        'login': '/account/login/{username}/{password}',
    },
    'login': {
        'new': '/login/new',
        'get_id': '/login/{id}',
        'get_all': '/login/all/{id}',
        'search': '/login/search',
        'update': '/login/update/{id}',
        'delete': '/login/delete/{id}'
    },
    'loginnote': {
        'new': '/loginnote/new',
        'get_id': '/loginnote/{id}',
        'get_all': '/loginnote/all/{id}',
        'search': '/loginnote/search',
        'update': '/loginnote/update',
        'delete': '/loginnote/delete/{id}'
    },
    'note': {
        'new': '/note/new',
        'get_id': '/note/{id}',
        'get_all': '/note/all/{id}',
        'search': '/note/search',
        'update': '/note/update',
        'delete': '/note/delete/{id}'
    },
    'password': {
        'new': '/password/new',
        'get_id': '/password/{id}',
        'get_all': '/password/all/{id}',
        'search': '/password/search',
        'update': '/password/update/{id}',
        'delete': '/password/delete/{id}'
    }
}
