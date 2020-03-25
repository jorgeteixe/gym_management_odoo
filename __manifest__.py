# -*- coding: utf-8 -*-
{
    'name': "Gym management",

    'summary': """
        Simple module to manage gym memberships and additional classes""",

    'description': """
        With this module you're able to create different memberships, the subscribers are allowed to select the sessions
        that they're going and check their billing.
    """,

    'author': "Jorge Teixeira",
    'website': "http://jorgeteixeira.es",

    'category': 'Events',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/class.xml',
        'views/membership.xml',
        'views/room.xml',
        'views/session.xml',
        'views/subscriber.xml',
        'views/teacher.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}