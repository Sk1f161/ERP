# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Cubic ERP - Teradata SAC (<http://cubicerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Peru Localization Chart Account",
    "version": "1.0",
    "description": """
Peruvian accounting chart and tax localization. Acording the PCGE 2010

Plan contable peruano e impuestos de acuerdo a disposiciones vigentes de la SUNAT 2011 (PCGE 2010)

    """,
    "author": ["Cubic ERP"],
    "website": "http://cubicERP.com",
    "category": "Localization/Account Charts",
    "depends": [
			"account_chart",
			],
	"data":[
        "account_tax_code.xml",
        "l10n_pe_chart.xml",
        "account_tax.xml",
        "l10n_pe_wizard.xml",			
			],
    "demo_xml": [
			],
    "update_xml": [
			],
    "active": False,
    "installable": True,
    "certificate" : "0045046493412",
    'images': ['images/config_chart_l10n_pe.jpeg','images/l10n_pe_chart.jpeg'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
