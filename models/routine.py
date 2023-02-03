# -*- coding: utf-8 -*-


from odoo import models, fields, api, exceptions 

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Routine(models.Model):

    _name = 'ofc_odoo.routine'
    name = fields.Char(String="Name", required=True)
    exercise= fields.Char(String="Exercise", required=True)
    private = fields.Boolean()
    time = fields.Float(String="Time",required=True)
    date_end = fields.Datetime(String="Date_end")
    date_start = fields.Datetime(String="Date_start", required=True)
    client = fields.Many2one('res.users', required=True, ofc_admin=False)
    
    
    @api.onchange('time')
    def _check_time_is_positive(self):
        if self.time < 0:
            return {
                'warning': {
                    'title':"Incorrect 'time' value",
                    'message': "The time mustn't be lower than 0",
                },
        }
        
    @api.constrains("time")
    def _verify_time_is_positive(self):
        if self.time < 0:
            raise exceptions.ValidationError("The time mustn't be lower than 0")

   

    @api.constrains("date_start", "date_end")
    def _verify_start_date_is_lower_than__end_date (self):
        if self.date_start > self.date_end:
            raise exceptions.ValidationError("The end_date mustn't be lower than date_start")
        
        
        
    @api.onchange('name')
    def _check_name_is_lower_than_30(self):
        if len(str(self.name)) > 30:
            return {
                'warning': {
                    'title':"Incorrect 'name' value",
                    'message': "The name lenght can`t be higher than 30",
                },
        }   
        
        
    @api.constrains("name")
    def _verify_check_name_is_lower_than_30(self):
        if len(str(self.name)) > 30:
            raise exceptions.ValidationError("The name lenght can`t be higher than 30")

            


