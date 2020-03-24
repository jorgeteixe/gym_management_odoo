# -*- coding: utf-8 -*-
from odoo import http

# class JorgeTeixeiraCrespo(http.Controller):
#     @http.route('/jorge_teixeira_crespo/jorge_teixeira_crespo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jorge_teixeira_crespo/jorge_teixeira_crespo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jorge_teixeira_crespo.listing', {
#             'root': '/jorge_teixeira_crespo/jorge_teixeira_crespo',
#             'objects': http.request.env['jorge_teixeira_crespo.jorge_teixeira_crespo'].search([]),
#         })

#     @http.route('/jorge_teixeira_crespo/jorge_teixeira_crespo/objects/<model("jorge_teixeira_crespo.jorge_teixeira_crespo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jorge_teixeira_crespo.object', {
#             'object': obj
#         })