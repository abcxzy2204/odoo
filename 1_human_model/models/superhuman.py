# -*- coding: utf-8 -*-
from odoo import models, fields, api
class SuperHuman(models.Model):
    _name = 'human.superhuman'
    _inherit = 'human.human'   
    _description = 'Super Human' 

    power = fields.Char(
        string='Super Power', 
        required=True, 
        help="The unique power of the superhuman."
    )
    origin = fields.Selection([
        ('earth', 'Earth'),
        ('alien', 'Alien'),
        ('magic', 'Magic'),
        ('tech', 'Technology')
    ], string='Origin', default='earth', help="The source or origin of their powers.")
    
    weakness = fields.Char(string='Weakness', help="The specific weakness of the superhuman, like Kryptonite.")

    is_team_leader = fields.Boolean(string='Team Leader', default=False)
    
    # Bạn có thể thêm các mối quan hệ (relational fields) ở đây
    # Ví dụ: Mối quan hệ với chính nó để tạo nhóm/team
    parent_id = fields.Many2one(
        'human.superhuman', 
        string='Report To (Leader)'
    )
    child_ids = fields.One2many(
        'human.superhuman', 
        'parent_id', 
        string='Team Members'
    )