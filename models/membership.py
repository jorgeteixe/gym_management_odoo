# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Membership(models.Model):
    _name = 'gym.membership'

    name = fields.Char(compute = '_full_name')
    title = fields.Char(string = 'Name', required = True)
    description = fields.Text(string = 'Description')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env['res.currency'].search([('name', '=', "EUR")], limit=1))
    price = fields.Monetary('Price', 'currency_id', default=39.90, required=True)

    subscriber_ids = fields.One2many('gym.subscriber', 'membership_id', string = 'Subscribers')

    @api.depends('title', 'price')
    def _full_name(self):
        for r in self:
            if r.title:
                r.name = r.title + ' [' + str(r.price) + ']'
