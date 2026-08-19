# -*- coding: utf-8 -*-
{
    'name': "Shopify Connector",

    'summary': """
        Real-time two-way sync between Shopify and Odoo.
        Orders, products, inventory, customers, invoices and fulfillment.
    """,

    'description': """
Shopify Integration for Odoo
============================

Connect your Shopify store to Odoo with a managed cloud sync service.
No CSV exports, no cron scripts, no server maintenance.

Key Features:
- Real-time order sync to Odoo with products, customers and line items
- Two-way sync for products, inventory levels, customers and fulfillment
- Real-time Odoo to Shopify inventory sync, including multi-location
- Automatic invoice and payment sync, refund flow included
- Bulk import of historical orders, products and customers
- Abandoned cart checkouts sent to Odoo CRM as sales leads
- Fulfilment and tracking numbers pushed back to Shopify
- Full audit log of every record synchronised

Compatibility:
- Odoo 16, 17, 18 and 19+
- Odoo Online, Odoo.sh and on-premise
- All Shopify plans, including Shopify Plus
- App available in English, Spanish, French, German and Italian

How It Works:
1. Install the app from the Shopify App Store
2. Connect your Odoo instance
3. Choose what to sync and in which direction
4. Data flows automatically - first sync in minutes

Pricing:
From $35/month with a 30-day free trial, billed through the
Shopify App Store.

Data Processing Notice:
This connector transmits store and Odoo record data to the TechMarbles
cloud sync service in order to perform synchronisation. Data is
processed only to provide the sync service. Full details in the privacy
policy at https://techmarbles.com/odoo-app-privacy-policy/
    """,

    'author': "TechMarbles",
    'website': "https://apps.shopify.com/odoo-integrator",
    'support': "support@techmarbles.com",
    'live_test_url': "https://apps.shopify.com/odoo-integrator",
    'category': 'Sales/Sales',
    'version': '16.0.1.0.2',

    'depends': ['base', 'stock', 'sale_management', 'account'],

    'data': [],

    'images': ['static/description/banner.png'],

    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'EUR',

    'installable': True,
    'application': True,
    'auto_install': False,
}
