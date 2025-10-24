from odoo import models, fields, api

class Human(models.Model):
    _name = 'human.human'
    _description = 'Human'

    name = fields.Char(string='Full Name', required=True, help="The full name of the human.")    
    age = fields.Integer(string='Age', help="The age of the human in years.")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other') 
    ], string='Gender', help="The gender of the human.")
