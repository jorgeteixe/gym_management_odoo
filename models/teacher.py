# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'gym.teacher'
    _inherit = 'gym.subscriber'

    class_ids = fields.One2many('gym.class', 'teacher_id', string = 'Classes')

    membership_id = fields.Many2one('gym.membership', ondelete='restrict', string='Membership', domain="[('price','=',0)]")