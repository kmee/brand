# Copiado da versão 16.0. Iniciar adaptação para Odoo 17.0.
# ...código original do partner.py...
from odoo import fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    brand_id = fields.Many2one("res.brand", string="Brand")
    brand_logo = fields.Image(
        string="Brand logo",
        related="brand_id.partner_id.image_128"
    )
