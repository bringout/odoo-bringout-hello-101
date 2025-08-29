# -*- coding: utf-8 -*-
{
    'name': 'Hello 101',
    'version': '16.0.1.0.0',
    'category': 'Custom',
    'summary': 'Hello 101',
    'description': """
Hello 101
=========

Hello 101

Features:
---------
* Custom menu with interactive hello message
* OWL JavaScript integration
* Modern web interface

    """,
    'author': 'Bringout',
    'website': 'https://www.bring.out.ba',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'data/menu_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hello_101/static/src/js/hello_component.js',
            'hello_101/static/src/xml/hello_templates.xml',
            'hello_101/static/src/css/hello_styles.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
