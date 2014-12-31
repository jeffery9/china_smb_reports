# -*- coding: utf-8 -*-
{
    'name': "report_customized",

    'summary': """
        中国中小型企业财务报表
        1，资产负债表
        2，利润表
        3，现金流量表""",

    'description': """
        
    """,

    'author': "jeffery chen fan ",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'china_smb_financial_report_data.xml',
    ],
}