
# -*- coding: utf-8 -*-

from odoo import models, fields

class Comment(models.Model):
    _name = 'ofc_odoo.comment'

    name = fields.Char(required=True)
    message = fields.Text(required=True)
    valoration = fields.Integer()
    privacity = fields.Boolean(required=True)
    data_modify = fields.Datetime()
    data_publication = fields.Datetime(required=True)
    event = fields.Many2one('ofc_odoo.event', string="Events",required=True)
    comclient = fields.Many2one('res.users', string="Client",required=True, ofc_admin=False)
    
    