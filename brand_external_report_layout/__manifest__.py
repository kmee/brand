{
    'name': 'Brand External Report Layout',
    'summary': 'Este módulo permite layout externo diferente por marca.',
    'version': '17.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'ACSONE SA/NV, Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/brand',
    'depends': ['base', 'brand', 'web'],
    'data': [
        'security/brand_document_layout.xml',
        'views/res_brand.xml',
        'views/report_template.xml',
        'wizards/brand_document_layout.xml'
    ],
    'assets': {
        'web.report_assets_common': [
            'static/src/legacy/scss/asset_styles_brand_report.scss'
        ]
    },
    'maintainers': ['sbejaoui'],
    'installable': True,
    'development_status': 'Beta'
}
