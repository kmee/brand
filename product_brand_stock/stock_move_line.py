from odoo import fields, models

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    product_brand_id = fields.Many2one(
        "product.brand",
        related="product_id.product_brand_id",
        string="Brand",
        store=True
    )
# Copiado da versão 16.0. Iniciar adaptação para Odoo 17.0.
# ...código original do stock_move_line.py...
