# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Users(models.Model):
    _name = 'res.users'
    _inherit = "res.users"
    lastPasswordChange = fields.Datetime()
    ofc_status = fields.Boolean()
    ofc_comment = fields.One2many("ofc_odoo.comment", 'comclient')
    ofc_routine = fields.One2many("ofc_odoo.routine", 'client')
    ofc_admin = fields.Boolean()
    ofc_event = fields.Many2many("ofc_odoo.event") 
