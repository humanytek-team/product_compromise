# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Rubén Bravo <rubenred18@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class MrpProduction(models.Model):
    _name = "mrp.production"
    _inherit = 'mrp.production'

    def action_assign(self):
        for production in self:
            if production.sale_id:
                for line in production.sale_id.order_line:
                    for move in line.mrp_move_raw_ids:
                        if move.compromise_qty > 0:
                            raise ValidationError(
                                _('You cannot reserve products with compromised stock'))
        res = super(MrpProduction, self).action_assign()
        return res
