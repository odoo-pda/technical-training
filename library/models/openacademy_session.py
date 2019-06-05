from odoo import models, fields, api

class OpenacademySession(models.Model):
    _name = 'openacademy.session'
    
    name = fields.Char(string="Name")
    
    master_id = fields.Many2one('res.partner', string="Master")
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    
    class_id = fields.Many2one('openacademy.class', String="Class")
    
    state = fields.Selection([('preparation','In Preparation'),
                              ('ready','Ready'),
                              ('archived','Archived')], string="State")