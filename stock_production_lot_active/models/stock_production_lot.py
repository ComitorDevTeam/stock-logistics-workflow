# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    active = fields.Boolean(string="Active", default=True)

    @api.multi
    def toggle_active(self):
        """ Inverse the value of the field active on the records in self. """
        for record in self:
            record.active = not record.active
