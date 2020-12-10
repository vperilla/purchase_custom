from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    request_reference = fields.Char('Request Reference')
