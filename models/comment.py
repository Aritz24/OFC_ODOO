# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class Comment(models.Model):
    _name = 'ofc_odoo.comment'

    name = fields.Char(required=True)
    message = fields.Text(required=True)
    valoration = fields.Integer()
    privacity = fields.Boolean()
    date_publication = fields.Date(required=True)
    event = fields.Many2one('ofc_odoo.event', string="Events", required=True)
    comclient = fields.Many2one('res.users', required=True, ofc_admin=False)
    
    @api.onchange('date_publication')
    def _onchange_date_publication(self):
        current_date = fields.Date().today()
        if self.date_publication:
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
        current_date = fields.Date().today()
        if self.date_publication > current_date:
            raise ValidationError("BAD DATE, Isn't current date")
        if self.date_publication < current_date:
            raise ValidationError("BAD DATE, Isn't current date")
        
    @api.constrains('valoration')
    def _check_valoration(self):
        print(self.valoration)
        if self.valoration > 10:
            raise ValidationError("Range is't 1 - 10 your rate: %s" % self.valoration)
        if self.valoration < 0:
            raise ValidationError("Range is't 1 - 10 your rate: %s" % self.valoration)    