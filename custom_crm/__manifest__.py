 
{
    'name': 'Custom CRM Enhancements',
    'version': '1.0',
    'summary': 'Adds custom fields and views to the CRM module',
    'description': 'This module enhances the Odoo CRM module with a Priority Level field.',
    'author': 'Obaid Nieroukh',
    'website': 'https://github.com/your-username',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}