# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models
from odoo import exceptions
from odoo import api
from odoo.exceptions import ValidationError 

class Comment(models.Model):
    _name = 'ofc_odoo.comment'

    name = fields.Char()
    message = fields.Text()
    valoration = fields.Integer()
    privacity = fields.Boolean()
    date_publication = fields.Datetime()
    event = fields.Many2one('ofc_odoo.event', string="Events")
    comclient = fields.Many2one('res.users', required=True, ofc_admin=False)
    
    @api.onchange('date_publication')
    def _onchange_date_publication(self):
        current_date = fields.Datetime.now()
        print('current: %s' % current_date ,'date: %s' % self.date_publication)
        if self.date_publication > current_date:
            return{
                'warning': {
                    'title': "Bad date setted",
                    'message': "The date isn't equals with the current date"
                }
            }   
        if self.date_publication < current_date:
            return{
                'warning': {
                    'title': "Bad date setted",
                    'message': "The date isn't equals with the current date"
                }
            }   
    @api.constrains('date_publication')
    def _check_date_publication(self):
        current_date = fields.Datetime.now()
        if self.date_publication > current_date:
            raise ValidationError("BAD DATE %s" % self.date_publication)
