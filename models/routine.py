# -*- coding: utf-8 -*-

from odoo import models, fields, api

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Routine(models.Model):
 

    name = fields.Char()
    exercise= fields.Char()
    private = fields.Boolean()
    time = fields.Float()
    date_end= fields.Datetime()
    date_start = fields.Datetime()
    client = fields.Many2One('res.users')
