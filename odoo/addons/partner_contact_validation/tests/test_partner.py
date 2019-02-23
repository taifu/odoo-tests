import logging

from odoo.tests.common import TransactionCase, SingleTransactionCase, SavepointCase

_logger = logging.getLogger(__name__)


class ResPartnerTest(TransactionCase):
    at_install = False

    def setUp(self):
        super().setUp()
        # 1
        # Fallisce senza flag sopra (il default è post_install = False e at_install = True
        # Passa con
        #   post_install = True
        #   at_install = False
        # Passa con
        #   post_install = False
        #   at_install = False
        # Fallisce con
        #   post_install = False
        #   at_install = True
        # Passa con
        #   at_install = False
        self.partner = self.env['res.partner'].create({'name': "Pippo"})

        # 2 ok
        # self.partner = self.env['res.partner'].new()
        # self.partner.name = "Pippo"

        # 3 ok
        # ResPartner = self.env['res.partner']
        # vals = ResPartner.default_get(ResPartner._fields.keys())
        # vals['name'] = "Pippo"
        # self.partner = ResPartner.create(vals)

    def test_name(self):
        self.assertEqual(self.partner.name, "Pippo")
