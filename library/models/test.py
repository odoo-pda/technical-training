from odoo import models, fields, api

class Test(models.Model):
    _name = 'library.test'

    hello = fields.Char(string='HelloOOOOOOOOoooooo')