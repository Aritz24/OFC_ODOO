# -*- coding: utf-8 -*-

from odoo import models, fields

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Routine(models.Model):

    _name = 'ofc_odoo.routine'
    name = fields.Char()
    exercise= fields.Char()
    private = fields.Boolean()
    time = fields.Float()
    date_end= fields.Datetime()
    date_start = fields.Datetime()
    client = fields.Many2one('res.users', required=True, ofc_admin=False)
    
