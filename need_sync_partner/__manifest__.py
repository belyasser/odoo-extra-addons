# -*- coding: utf-8 -*-
# Copyright© 2016-2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    'name': 'Need Synchronization Partner Module',
    'version': '10.0.0.0.7',
    'category': 'Tools',
    'author': 'ICTSTUDIO, André Schenkels',
    'website': 'http://www.ictstudio.eu',
    'license': 'AGPL-3',
    'summary': 'Partner Specific module for seting need sync',
    'depends': [
        'need_sync_base',
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'installable': True,
}