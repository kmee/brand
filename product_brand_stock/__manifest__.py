{
    'name': 'Product Brand Stock',
    'summary': 'Permite trabalhar com product_brand no estoque.',
    'version': '17.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/brand',
    'depends': ['product_brand', 'stock'],
    'data': [
        'views/stock_quant_views.xml',
        'views/stock_move_views.xml',
        'views/stock_move_line_views.xml'
    ],
    'pre_init_hook': 'pre_init_hook',
    'installable': True,
    'development_status': 'Beta'
}
