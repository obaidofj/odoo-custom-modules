from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount = fields.Float(string='Discount (%)', help="Discount percentage for this product.")