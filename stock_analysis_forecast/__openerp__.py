# -*- coding: utf-8 -*-
# Copyright 2016 Alex Comba - Agile Business Group
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Stock Analysis Forecast',
    'summary': """
        Analysis wiew for stock forecast""",
    'version': '8.0.1.0.0',
    'category': 'Inventory, Logistic, Storage',
    'license': 'LGPL-3',
    'author': 'Agile Business Group, Odoo Community Association (OCA)',
    'website': 'https://www.agilebg.com',
    'depends': [
        'product',
        'stock',
    ],
    'data': [
        'views/report_stock_forecast.xml',
    ],
}
