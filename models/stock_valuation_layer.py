from odoo import models, fields, api, _

class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    warehouse_id = fields.Many2one('stock.warehouse', 'Warehouse', compute='get_warehouse_id' , store=True)
    secondary_uom = fields.Many2one('uom.uom', 'Secondary UoM', related='product_id.secondary_uom_id')
    qty_of_secondary_uom = fields.Float('Quantity of Secondary UoM', compute='compute_qty_of_secondary_uom')
    location_id = fields.Many2one('stock.location', 'Location', compute='get_warehouse_id' , store=True)
    date = fields.Datetime(string='Date', related='stock_move_id.date', store=True)

    def compute_qty_of_secondary_uom(self):
        self.qty_of_secondary_uom = 0
        if self.secondary_uom:
            if self.secondary_uom.factor_inv > 0:
                self.qty_of_secondary_uom = self.quantity/self.secondary_uom.factor_inv

    @api.depends('stock_move_id')
    def get_warehouse_id(self):
        for record in self:
            if record.stock_move_id.location_id.warehouse_id:
                record.warehouse_id = record.stock_move_id.location_id.warehouse_id.id
                record.location_id = record.stock_move_id.location_id.id
            elif record.stock_move_id.location_dest_id.warehouse_id:
                record.warehouse_id = record.stock_move_id.location_dest_id.warehouse_id.id
                record.location_id = record.stock_move_id.location_dest_id.id
            else:
                record.warehouse_id = False
                record.location_id = False