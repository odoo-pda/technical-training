from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Books of the Library"
    
    name = fields.Char(string="Title")
    
    author_ids = fields.Many2many('res.partner', string="Authors")
    editor_id = fields.Many2one('res.partner', string="Editor")
    
    year_edition = fields.Date(string="Year of Edition")
    
    rental_ids = fields.One2many('library.rental', 'book_id', string="Rentals")