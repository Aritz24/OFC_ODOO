
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class comment(models.Model):
    _name = 'ofc_odoo.comment'

    name = fields.Char()
    message = fields.Text()
    valoration = fields.Integer()
    privacity = fields.Boolean()
    data_modify = fields.Datatime()
    data_publication = field.Datatime()
    event = fields.many2one('ofc_odoo.event',string="Event",required=True)
    client = fields.many2one('res.User',string="Client",required=True)
    
        
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100