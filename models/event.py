# -*- coding: utf-8 -*-

from odoo import models, fields

class Event(models.Model):
     _name = 'ofc_odoo.event'
     name = fields.Char(Required = True)
     activity = fields.Char(digits = (5,2) ,help = "€" )
     capacity = fields.Integer(required = True)
     date = fields.Datetime(required = True)
     place = fields.Char(required = True)
     price = fields.Float()
     admin = fields.Many2one('res.users',required=True, ofc_admin=True)
     coments = fields.One2many('ofc_odoo.comment','event',required=True)
     clients = fields.Many2many('res.users', ofc_admin=False)
     sponsors = fields.Many2many('ofc_odoo.sponsor')
