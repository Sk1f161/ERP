# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2009 Akretion (<http://www.akretion.com>). All Rights Reserved
#    authors: Raphaël Valyi, Sharoon Thomas
#    Copyright (C) 2010-2011 Akretion Sébastien BEAU <sebastien.beau@akretion.com>
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Base Sale MultiChannels',
    'version': '6.1.2',
    'category': 'Generic Modules/Sale',
    'description': """
This module provide an abstract common minimal base to multi-channels sales.
Say you want to expose your product catalog to
* several instances of flashy-sluggish Magento web sites
* a cutting edge Spree web shop
* a Neteven online Marketplace
* EBay
* Amazon
* Google Base
* an external Point Of Sale system
* ...
Then this module allows you to:
* use several external references ids on every OpenERP object matching those all those external referentials
* per referential instance, use several sale sub platform entities (ex: several Magento websites per instance)
* per sub platform, use several shops (ex: several Magento web shops per website)

For each sale shop (matching OpenERP sale.shop object), this module abstract the interfaces to:
* export the catalog, shop warehouse stock level wise, shop pricelist wise
* import the catalog
* import orders
* export orders/picking status
    """,
    'author': 'Akretion, Sharoon Thomas (Openlabs.co.in)',
    'website': 'http://www.akretion.com',
    'depends': [
        'sale_automatic_workflow',
        'sale_exceptions',
        'base_external_referentials',
        'delivery',
        'base_onchange_player',
    ],
    'init_xml': [],
    'update_xml': [
        'security/ir.model.access.csv',
        'sale_view.xml',
        'partner_view.xml',
        'invoice_view.xml',
        'wizard/import_order.xml',
        'delivery_view.xml',
        'base_sale_data.xml',
        'settings/sale.exception.csv',
        'settings/external.referential.category.csv',
        'stock_view.xml',
        'payment_method_view.xml',
        'account_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'certificate': '',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
