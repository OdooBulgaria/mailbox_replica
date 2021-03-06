# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Eficent (<http://www.eficent.com/>)
#              <contact@eficent.com>
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
##############################################################################
import logging
from openerp.osv import fields, orm


_logger = logging.getLogger(__name__)


class FetchMailServer(orm.Model):
    _inherit = 'fetchmail.server'

    _columns = {
        'user_id': fields.many2one('res.users', string='Owner'),
    }

    def _get_current_user(self, cr, uid, context=None):
        return [uid]

    _defaults = {
        'user_id': _get_current_user,
    }
    _sql_constraints = [
        ('fetchmail_user_uniq', 'unique(user_id)', 'That user already has a '
                                                   'Fetchmail server.'),
    ]
