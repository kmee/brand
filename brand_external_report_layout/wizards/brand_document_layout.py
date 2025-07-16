# Copyright 2022 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import markupsafe

from odoo import api, fields, models
from odoo.addons.web.models.base_document_layout import (
    DEFAULT_PRIMARY,
    DEFAULT_SECONDARY,
)

class BrandDocumentLayout(models.TransientModel):
    _name = "brand.document.layout"
    _description = "Brand Document Layout"
    _inherit = "base.document.layout"

    brand_id = fields.Many2one("res.brand", required=True)
    logo = fields.Binary(related="brand_id.logo", readonly=False)
    report_header = fields.Html(related="brand_id.report_header", readonly=False)
    report_footer = fields.Html(related="brand_id.report_footer", readonly=False)
    paperformat_id = fields.Many2one(related="brand_id.paperformat_id", readonly=False)
    external_report_layout_id = fields.Many2one(related="brand_id.external_report_layout_id", readonly=False)
    font = fields.Selection(related="brand_id.font", readonly=False)
    primary_color = fields.Char(related="brand_id.primary_color", readonly=False)
    secondary_color = fields.Char(related="brand_id.secondary_color", readonly=False)
    company_details = fields.Html(related="brand_id.company_details", readonly=False)
    layout_background = fields.Selection(related="brand_id.layout_background", readonly=False)
    layout_background_image = fields.Binary(related="brand_id.layout_background_image", readonly=False)
    @api.onchange("company_id")
    def _onchange_company_id(self):
        return {}
    @api.onchange("brand_id")
    def _onchange_brand_id(self):
        for wizard in self:
            wizard.logo = wizard.brand_id.logo
            wizard.report_header = wizard.brand_id.report_header
            wizard.report_footer = (
                wizard.brand_id.report_footer
                if isinstance(wizard.brand_id.report_footer, str)
                else wizard.report_footer
            )
            wizard.company_details = (
                wizard.brand_id.company_details
                if isinstance(wizard.brand_id.company_details, str)
                else wizard.company_details
            )
            wizard.paperformat_id = wizard.brand_id.paperformat_id
