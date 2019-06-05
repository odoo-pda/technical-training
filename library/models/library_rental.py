from odoo import models, fields, api

class LibraryRental(models.Model):
    _name = "library.rental"
    _description = "Rentals"
    
    rental_date = fields.Date(string="Rental Date")
    return_date = fields.Date(string="Return Date")
    
    customer_id = fields.Many2one('library.customer', string="Customer")
    book_id = fields.Many2one('library.book', string="Book")
    