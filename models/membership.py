# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Membership(models.Model):
    _name = 'gym.membership'

    name = fields.Char(compute = '_full_name')
    title = fields.Char(string = 'Name', required = True)
    description = fields.Text(string = 'Description')
    price = fields.Float(string='Price', digits=(5, 2), default=39.90, required=True)

    subscriber_ids = fields.One2many('gym.subscriber', 'membership_id', string = 'Subscribers')

    @api.depends('title', 'price')
    def _full_name(self):
        for r in self:
            r.name = r.title + ' [' + r.price + ']'
