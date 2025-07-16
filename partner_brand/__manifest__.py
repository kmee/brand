{
    'name': 'Partner Brand',
    'summary': 'Define marca registrada em parceiros conforme configuração de marca.',
    'version': '17.0.1.0.0',
    'author': 'Odoo Community Association (OCA), Akretion',
    'category': 'Product',
    'maintainers': ['bealdav'],
    'website': 'https://github.com/OCA/brand',
    'license': 'AGPL-3',
    'depends': ['brand', 'contacts'],
    'data': ['views/partner.xml'],
    'demo': [
        'data/res_brand_demo.xml',
        'data/res_partner_demo.xml'
    ],
    'installable': True,
    'development_status': 'Beta'
}
