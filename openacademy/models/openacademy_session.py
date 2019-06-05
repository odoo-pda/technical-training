from odoo import models, fields, api

class OpenacademySession(models.Model):
    _name = 'openacademy.session'
    _description = "Sessions for OpenAcademy"
    
    name = fields.Char(string="Name")
    
    master_id = fields.Many2one('res.partner', string="Master")
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    
    class_id = fields.Many2one('openacademy.class', string="Class")
    
    state = fields.Selection([('preparation','In Preparation'),('ready','Ready')], string="State")
    archived = fields.Boolean(string="Archived")