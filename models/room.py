# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Room(models.Model):
    _name = 'gym.room'

    name = fields.Char(string = 'Name', required = True)
    description = fields.Text(string = 'Description')

    session_ids = fields.Many2one('gym.session', 'room_id', string = 'Sessions')
