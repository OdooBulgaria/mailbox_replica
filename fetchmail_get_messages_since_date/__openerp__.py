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

{
    'name': 'Fetch mails from IMAP since a date',
    'version': '1.0',
    'description': """
Fetch mails from IMAP since a date
==================================
Adds the possibility to fetch emails from IMAP from a specific date.

    """,
    'author': 'Eficent',
    'website': 'http://www.eficent.com',
    "category": "Tools",
    "depends": ['fetchmail'],
    'data': [
        'security/ir.model.access.csv',
        'views/fetchmail_server.xml',
    ],
    'js': [],
    'installable': True,
    'active': False,
    'certificate': '',
}
