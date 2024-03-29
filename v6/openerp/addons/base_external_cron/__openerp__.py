# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
#   base_external_cron for OpenERP                                            #
#   Copyright (C) 2012 Akretion David BEAL <david.beal@akretion.com>           #
#                                                                             #
#   This program is free software: you can redistribute it and/or modify      #
#   it under the terms of the GNU Affero General Public License as            #
#   published by the Free Software Foundation, either version 3 of the        #
#   License, or (at your option) any later version.                           #
#                                                                             #
#   This program is distributed in the hope that it will be useful,           #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU Affero General Public License for more details.                       #
#                                                                             #
#   You should have received a copy of the GNU Affero General Public License  #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################



{
    'name': 'base_external_cron',
    'version': '6.1.0',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': """empty""",
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': ['base_external_referentials'],
    'init_xml': [],
    'update_xml': [
           'external_cron_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}

