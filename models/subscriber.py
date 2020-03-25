# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subscriber(models.Model):
    _name = 'gym.subscriber'
    _sql_constraints = [('unique_mail', 'unique(email)', 'This email already exists')]

    name = fields.Char(string = 'Name', required = True)
    id_number = fields.Char(string = 'ID Number', required = True)
    address = fields.Text(string = 'Address')
    phone = fields.Char(string = 'Phone number')
    email = fields.Char(string = 'Email', required = True)

    membership_id = fields.Many2one('gym.membership', ondelete='restrict', string='Membership')

    session_ids = fields.One2many('gym.session', 'class_id', string = 'Sessions')

