{
    'name': 'Custom Product Discount',
    'version': '1.0',
    'summary': 'Adds a discount field to products',
    'description': 'This module adds a discount field to the product form.',
    'author': 'Obaid Nieroukh',
    'website': 'https://github.com/your-username',
    'depends': ['product'],
    'data': [
        'views/product_template_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}