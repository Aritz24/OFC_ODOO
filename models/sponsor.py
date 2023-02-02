# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models, fields, api

class Sponsor(models.Model):
    _name = 'ofc_odoo.sponsor'
    name = fields.Char(required = True)
    email = fields.Char()
    state = fields.Boolean()
    date = fields.Datetime()
    phone = fields.Integer()
    adType = fields.Boolean()
    event = fields.Many2many('ofc_odoo.event', string ="Events")
    admin = fields.Many2one('res.Users', required = True, ofc_admin=True)
    
