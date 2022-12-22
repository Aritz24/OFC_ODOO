# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Event(models.Model):
     _name = 'ofc_odoo.event'

     name = fields.Char(Required = True)
     activity = field.Char(digits = (5,2) ,help = "€" )
     capacity = field.Integer(required = True)
     date = field.Datetime(required = True)
     place = field.Char(required = True)
     price = field.Float()
     admin = field.Many2one('res.users',required=True)
     coments = field.One2many('ofc_odoo.coment','event',required=True)
     clients = field.Many2many('res.users')
     sponsors = field.Many2many('ofc_odoo.sponsor')
