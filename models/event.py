# -*- coding: utf-8 -*-
from odoo import models, fields

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Event(models.Model):

    _name = 'ofc_odoo.event'
    name = fields.Char(required = True)
    activity = fields.Char()
    capacity = fields.Integer(required = True)
    date = fields.Datetime(required = True)
    place = fields.Char(required = True)
    price = fields.Float(digits = (5,2) ,help = "€" )
    admin = fields.Many2one('res.users',required=True, ofc_admin=True)
    coments = fields.One2many('ofc_odoo.comment','event',required=True)
    clients = fields.Many2many('res.users', ofc_admin=False)
    sponsors = fields.Many2many('ofc_odoo.sponsor')
     
     
    @api.onchange('name')
    def _validate_lenght_name(self):
        if len(str(self.name)) > 30:
            return {
                'warning': {
                    'title':"Incorrect 'name' lenght",
                    'message':"the name field cannot be greater than 30",
                }
        }
        
    @api.constrains('name')
    def _validate_lenght_name_exc(self):
        if len(str(self.name)) > 30:
            raise ValidationError("the name field cannot be greater than 30")
        
        
    @api.onchange('capacity')
    def _validate_lenght_capacity(self):
        if self.capacity < 0:
            return {
                'warning': {
                    'title':"Incorrect 'capacity' value",
                    'message': "the capacity field cannot be less than 0",
                }
        }
        
    @api.constrains('capacity')
    def _validate_lenght_capacity_exc(self):
        if len(str(self.capacity)) > 30:
            raise ValidationError("the capacity field cannot be greater than 30")
        
    @api.onchange('place')
    def _validate_lenght_place(self):
        if len(str(self.place)) > 30:
            return {
                'warning': {
                    'title':"Incorrect 'place' lenght",
                    'message':"the place field cannot be greater than 30",
                }
        }
        
    @api.constrains('place')
    def _validate_lenght_place_exc(self):
        if len(str(self.place)) > 30:
            raise ValidationError("the place field cannot be greater than 30")
        
    @api.constrains('date')
    def _validate_date_exc(self):
        date_today = fields.Datetime.now()
        if self.date < date_today:
            raise ValidationError("the selected date cannot be earlier than today")

