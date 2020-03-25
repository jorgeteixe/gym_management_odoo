# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class Session(models.Model):
    _name = 'gym.session'

    name = fields.Char(compute = '_full_name')
    start_date = fields.Datetime(string = 'Start date', required = True)
    duration = fields.Integer(string = 'Duration (minutes)', required = True)
    end_date = fields.Datetime(string="End date", store=True, compute='_get_end_date')

    class_id = fields.Many2one('gym.class', ondelete='restrict', string='Class')

    subscribers_ids = fields.Many2many('gym.subscriber', string = 'Subscribers',
                                       relation = 'gym_session_subscribers', ondelete = 'set null',
                                       column1 = 'session_id', column2 = 'subscriber_id')

    room_id = fields.Many2one('gym.room', ondelete='restrict', string='Room')

    @api.depends('start_date', 'class_id')
    def _full_name(self):
        for r in self:
            r.name = r.start_date + ' ' + r.class_id

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            duration = timedelta(minutes=r.duration)
            r.end_date = r.start_date + duration

    @api.constrains('duration')
    def _max_duration(self):
        for r in self:
            if 120 <= r.duration < 10:
                raise ValidationError('Duration is not correct, has to be between 10 and 120 minutes.')

