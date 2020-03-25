# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Class(models.Model):
    _name = 'gym.class'

    name = fields.Char(compute = '_full_name')
    title = fields.Char(string = 'Class title', required = True)
    price = fields.Float(string='Session price', digits=(5, 2), default=4.90, required=True)

    teacher_id = fields.Many2one('gym.teacher', ondelete='restrict', string='Teacher', required = True)

    session_ids = fields.One2many('gym.session', 'class_id', string = 'Sessions')


    @api.depends('title', 'teacher_id')
    def _full_name(self):
        for r in self:
            if r.title and r.teacher_id:
                r.name = r.title + ' ' + r.teacher_id