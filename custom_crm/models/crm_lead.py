 
from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    priority_level = fields.Selection(
        selection=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        string='Priority Level',
        default='medium',
        help="Set the priority level for this lead."
    )