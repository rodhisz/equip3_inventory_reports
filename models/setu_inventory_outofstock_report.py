from odoo import models, api, fields


class SetuInventoryOutOfStockReport(models.TransientModel):

    _inherit = 'setu.inventory.outofstock.report'

    company_id = fields.Many2one('res.company', string='Company', readonly=True,
        default=lambda self: self.env.company)
    company_ids = fields.Many2many(default=lambda self:self.env.user.company_id.ids)

    def download_report_in_listview(self):
        rec = super(SetuInventoryOutOfStockReport, self).download_report_in_listview()
        rec.update({'name': ("Inventory Demand Forecast Analysis")})
        return rec
    
    def get_file_name(self):
        filename = "inventory_demand_forecast_analysis.xlsx"
        return filename

class SetuInventoryOverstockReport(models.TransientModel):
    _inherit = 'setu.inventory.overstock.report'

    company_id = fields.Many2one('res.company', string='Company', readonly=True,
        default=lambda self: self.env.company)
    company_ids = fields.Many2many(default=lambda self:self.env.user.company_id.ids)

class SetuInventoryTurnoverReport(models.TransientModel):

    _inherit = 'setu.inventory.turnover.analysis.report'

    company_id = fields.Many2one('res.company', string='Company', readonly=True,
        default=lambda self: self.env.company)
    company_ids = fields.Many2many(default=lambda self:self.env.user.company_id.ids)

class SetuInventoryFSNReport(models.TransientModel):

    _inherit = 'setu.inventory.fsn.analysis.report'

    company_id = fields.Many2one('res.company', string='Company', readonly=True,
        default=lambda self: self.env.company)
    company_ids = fields.Many2many(default=lambda self:self.env.user.company_id.ids)

class SetuInventoryXYZReport(models.TransientModel):

    _inherit = 'setu.inventory.xyz.analysis.report'

    company_id = fields.Many2one('res.company', string='Company', readonly=True,
        default=lambda self: self.env.company)
    company_ids = fields.Many2many(default=lambda self:self.env.user.company_id.ids)

class SetuInventoryFSNXYZReport(models.TransientModel):

    _inherit = 'setu.inventory.fsn.xyz.analysis.report'

    company_id = fields.Many2one('res.company', string='Company', readonly=True,
        default=lambda self: self.env.company)
    company_ids = fields.Many2many(default=lambda self:self.env.user.company_id.ids)