import logging

from odoo.tests.common import TransactionCase, SingleTransactionCase, SavepointCase

_logger = logging.getLogger(__name__)


class MyTestClass(TransactionCase):
    cls_boolean_value = None
    self_boolean_value = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        _logger.info("Setting up class from 'setUpClass'...")

        cls.cls_boolean_value = True

    def setUp(self):
        super().setUp()

        _logger.info("Setting up class from 'setUp'...")

        self.self_boolean_value = True

    def test_my_first_test(self):
        _logger.info("This is my very first test written inside Odoo!")

        self.assertTrue(self.cls_boolean_value)
        self.assertTrue(self.self_boolean_value)

    def test_my_second_one(self):
        _logger.info("This is the second one...")

        self.assertTrue(self.cls_boolean_value)
        self.assertTrue(self.self_boolean_value)

    def test_my_last_but_not_least(self):
        _logger.info("This should be the last test of this transaction...")

    def test_some_assert(self):
        _logger.info("This should be fine...")
        self.assertTrue(True)

        _logger.error("Not so fast... ;)")
        self.assertTrue(False)

        _logger.info("This should be fine too!")
        self.assertTrue(True)
