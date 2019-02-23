import logging

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase  # , SingleTransactionCase, SavepointCase

_logger = logging.getLogger(__name__)


class ResPartnerTest(TransactionCase):
    post_install = True
    at_install = False

    def setUp(self):
        super().setUp()
        self.ResPartner = self.env['res.partner']
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
        # Passa ma viene eseguito solo la prima volta
        #   at_install = False
        self.partner = self.ResPartner.create({'name': "Pippo"})

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

    def test_phone_bad_multiple(self):
        self.ResPartner.create({'name': "Top1"})
        self.ResPartner.create({'name': "Top2"})
        partners = self.ResPartner.search([("name", "ilike", "Top%")])
        with self.assertRaisesRegex(ValidationError, "Bad phone"):
            partners.write({'phone': 'XXX'})

    def test_phone_ok_multiple(self):
        self.ResPartner.create({'name': "Top1"})
        self.ResPartner.create({'name': "Top2"})
        partners = self.ResPartner.search([("name", "ilike", "Top%")])
        partners.write({'phone': '0332123123'})

    def test_phone_bad(self):
        with self.assertRaisesRegex(ValidationError, "Bad phone"):
            self.ResPartner.create({'name': 'Pluto', 'phone': "BAD"})

    def test_phone_ok(self):
        phone = '+39-0332-459081'
        partner = self.ResPartner.create({'name': 'Topolino', 'phone': phone})
        self.assertEqual(partner.phone, phone)
