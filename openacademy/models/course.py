# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import Warning
import logging

_logger = logging.getLogger(__name__)

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('openacademy.partner', string="Responsible")
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    level = fields.Selection([(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], string="Difficulty Level")


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"), ('done', "Done")], default='draft')

    start_date = fields.Date(default=fields.Date.context_today)
    duration = fields.Float(digits=(6, 2), help="Duration in days", default=1)

    instructor_id = fields.Many2one('openacademy.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('openacademy.partner', string="Attendees")

    max_attendees = fields.Integer(string="Max")
    nb_attendees = fields.Integer(string="Number of Attendees", compute='_compute_attendees', store=True)
    
    @api.depends('attendee_ids')
    def _compute_attendees(self):
        self.nb_attendees = len(self.attendee_ids)
        
    """@api.constrains('max_attendees','attendee_ids')
    def check_nb_attendees(self):
        _logger.info("CONSTRAINS-------------------NB ATT BEFORE %s-------" % self.nb_attendees)
        if self.nb_attendees > self.max_attendees:
            #return {'warning': {
            #    'title': 'Too many attendees',
            #    'message': 'The room has available seats and there is attendees registered'
            #}}
            raise Warning("Too much attendees for this session.")
        _logger.info("CONSTRAINS-------------------NB ATT AFTER %s-------" % self.nb_attendees)
    """
        
    _sql_constraints = [
        # possible only if taken_seats is stored
        ('session_full', 'CHECK(nb_attendees <= max_attendees)', 'The room is full'),
    ]