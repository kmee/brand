# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
import os

from odoo import _, api, fields, models, tools

class ResBrand(models.Model):
    _inherit = "res.brand"

    def _get_default_brand_logo(self):
        return base64.b64encode(
            open(
                os.path.join(
                    tools.config["root_path"],
                    "addons",
                    "base",
                    "static",
                    "img",
                    "res_company_logo.png",
                ),
                "rb",
            ).read()
        )

    logo = fields.Binary(
        related="partner_id.image_1920",
        default=_get_default_brand_logo,
        string="Brand Logo",
        readonly=False,
    )
    external_report_layout_id = fields.Many2one(
        comodel_name="ir.ui.view", string="Document Template"
    )
    report_header = fields.Html(
        help="Appears by default on the top right corner of your printed documents (report header).",
    )
    report_footer = fields.Html(
        translate=True,
        help="Footer text displayed at the bottom of all reports.",
    )
    paperformat_id = fields.Many2one(
        "report.paperformat",
        "Paper format",
        default=lambda self: self.env.ref("base.paperformat_euro", raise_if_not_found=False),
    )
    font = fields.Selection([
        ("Lato", "Lato"),
        ("Roboto", "Roboto"),
        ("Open_Sans", "Open Sans"),
        ("Montserrat", "Montserrat"),
        ("Oswald", "Oswald"),
    ], string="Font")
    primary_color = fields.Char(string="Primary Color")
    secondary_color = fields.Char(string="Secondary Color")
    company_details = fields.Html(string="Company Details")
    layout_background = fields.Selection([
        ("none", "None"),
        ("image", "Image"),
        ("color", "Color"),
    ], string="Layout Background")
    layout_background_image = fields.Binary(string="Layout Background Image")
