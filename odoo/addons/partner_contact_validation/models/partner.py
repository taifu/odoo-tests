import re

from odoo import api, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.one
    @api.constrains('phone')
    def _validate_phone(self):
        if re.sub("[-0-9+ ]*", "", self.phone):
            raise ValidationError(_("Bad phone number"))
