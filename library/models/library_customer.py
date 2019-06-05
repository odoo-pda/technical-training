from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = "library.customer"
    _description = "Customers of the Library"
    
    name = fields.Char(string="Name")
    address = fields.Char(string="Address")
    email = fields.Char(string="Email")
    
    rental_ids = fields.One2many('library.rental', 'customer_id', string="Rentals")