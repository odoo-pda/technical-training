from odoo import models, fields, api

class OpenacademyClass(models.Model):
    _name = 'openacademy.class'
    _description = "Classes for OpenAcademy"
    
    name = fields.Char(string="Name")
    
    level = fields.Integer(string="Level")
    
    session_ids = fields.One2many('openacademy.session', 'class_id', string="Sessions")
    
    