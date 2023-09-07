{
    'name' : 'Equip3 Inventory Reports',
    'version' : '1.1.33',
    'category' : 'Extra Tools',
    'depends' : [
                'eq_scrap_order_report',
                'setu_advance_inventory_reports',
                'dev_rma',
                'equip3_inventory_tracking',
                'stock',
                'product',
                'contacts', 'equip3_hashmicro_ui',
                'equip3_general_features',
                'product_expiry'
                ],
    'data' :[
       'security/ir.model.access.csv',
       'views/assets.xml',
       'views/stock_quant_views.xml',
       'views/menu_views.xml',
       "views/smart_button.xml",
       'views/stock_move.xml',
       'views/stock_reservation.xml',
       'views/inventory_in_transit.xml',
       "wizard/setu_stock_movement_report_views.xml",
       "wizard/warehouse_capacity_report_view.xml",
       "wizard/warehouse_capacity_excel_report_view.xml",
       "views/return_order_view.xml",
       "views/expiring_and_expired_stocks_view.xml",
       "views/stock_picking_view.xml",
       "views/product.xml",
       "views/stock_inventory_line_view.xml",
       "views/setu_inventory_outofstock_report_view.xml",
       "views/stock_valuation_layer.xml",
       "views/stock_location.xml",
       "views/inventory_age_analysis_report.xml",
       "views/expiring_product_calendar_views.xml",
       "views/stock_production_lot_views.xml",
       "db_function/inventory_stock_age_report.sql",
       "reports/report_stock_quantity_new_views.xml",
       "reports/report_forecast_quantity_views.xml",
       
    ],
    'qweb': [
        'static/src/xml/stock_per_warehouse_widget.xml',
        'static/src/xml/stock_per_warehouse.xml',
        'static/src/xml/expiring_product_calendar.xml'
    ],
    'demo' :[],
    'installable' : True,
    'application' : True,
    'auto_install' : False
}