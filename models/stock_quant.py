
from odoo import fields, models, api
from datetime import datetime, date, timedelta


class StockQuant(models.Model):
    _inherit = "stock.quant"

    product_category = fields.Many2one("product.category", related="product_id.categ_id", store=True, string="Product category")
    expire_days = fields.Char(string="Expire in (days)", compute='_calculate_expire_day', store=False)
    expire_days_count = fields.Integer(string="Expire in (days)", compute='_calculate_expire_day', store=False)
    expire_date = fields.Datetime('Expiration_date', readonly=True, compute='_compute_lots_expire_date', store=True)
    weight = fields.Float(related='product_id.weight')
    is_update_value = fields.Boolean(compute='get_value_and_location')
    purchase_value_in_lot = fields.Monetary('Value', groups='stock.group_stock_manager', compute='get_value_and_location')
    warehouse_id = fields.Many2one('stock.warehouse', related="location_id.warehouse_id", store=True)
    cluster_area_id = fields.Many2one(comodel_name='cluster.area', string='Cluster Area', compute='get_cluster_area', store=True)

    def get_value_and_location(self):
        for record in self:
            record.is_update_value = False
            # record.purchase_value_in_lot = record.value
            record.sudo().write({'purchase_value_in_lot': record.value})
            if record.product_category.property_cost_method == 'fifo':
                if record.lot_id.product_id.tracking == 'serial' or record.lot_id.product_id.tracking == 'lot':
                    for line in record.lot_id.purchase_order_ids.order_line:
                        if line.product_id.id == record.lot_id.product_id.id:
                            record.sudo().write({'purchase_value_in_lot': line.price_unit})
                            record.sudo().write({'location_id': line.destination_warehouse_id.lot_stock_id.id})
                            putaway_exists = self.env['stock.putaway.rule'].search([('location_in_id', '=', line.destination_warehouse_id.lot_stock_id.id)])
                            for rule in putaway_exists:
                                if record.product_id.id in rule.product_ids.ids:
                                    record.sudo().write({'location_id': rule.location_out_id.id})
    
    def _calculate_expire_day(self):
        today_date = datetime.now()
        for record in self:
            record.expire_days = ""
            record.expire_days_count = 0
            if record.expire_date:
                difference = record.expire_date - today_date
                record.expire_days_count = difference.days
                if difference.days > 0:
                    record.expire_days = str(difference.days) + " Days"
                elif difference.days == 0:
                    record.expire_days = "Today"
                else:
                    record.expire_days = str(abs(difference.days)) + " Days Ago"
    

    @api.depends('lot_id.expiration_date', 'lot_id')
    def _compute_lots_expire_date(self):
        for record in self:
            if record.lot_id.id == False:
                record.expire_date = False
            else:
                record.expire_date = record.lot_id.expiration_date


    @api.depends('location_id')
    def get_cluster_area(self):
        for record in self:
            warehouse_id = record.location_id.warehouse_id.id
            cluster_warehouse_line = self.env['cluster.warehouse.line'].search([('warehouse_id', '=', warehouse_id)], limit=1)
            if cluster_warehouse_line:
                record.cluster_area_id = cluster_warehouse_line.cluster_id.id
