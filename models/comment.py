
# -*- coding: utf-8 -*-

from odoo import models, fields, api

class comment(models.Model):
    _name = 'ofc_odoo.comment'

    name = fields.Char(required=True)
    message = fields.Text(required=True)
    valoration = fields.Integer()
    privacity = fields.Boolean(required=True)
    data_modify = fields.Datatime()
    data_publication = field.Datatime(required=True)
    event = fields.many2one('ofc_odoo.event',string="Event",required=True)
    client = fields.many2one('res.User',string="Client",required=True)
    