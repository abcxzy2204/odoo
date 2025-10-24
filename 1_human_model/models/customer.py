from odoo import models, fields

class Customer(models.Model):
    # Tên kỹ thuật duy nhất của model
    _name = 'human.customer' 
    _description = 'Customer'
    
    # Kế thừa Ủy quyền (Delegation Inheritance)
    # Model Customer sẽ ủy quyền các trường của 'human.human'
    # thông qua trường Many2one là 'human_id'.
    _inherits = {'human.human': 'human_id'} 

    # ----------------------------------------------------
    # Khóa ngoại để thiết lập Kế thừa Ủy quyền
    # ----------------------------------------------------
    
    # Trường Many2one trỏ đến model Human.
    # Trường này là BẮT BUỘC khi sử dụng _inherits.
    human_id = fields.Many2one(
        'human.human', 
        string='Human Link', 
        required=True, 
        ondelete='cascade', # Nếu Human bị xóa, Customer cũng bị xóa
        index=True
    )
    
    # ----------------------------------------------------
    # Các trường đặc trưng cho Customer
    # ----------------------------------------------------
    
    customer_ref = fields.Char(
        string='Customer Reference', 
        required=True, 
        copy=False, 
        readonly=True, 
        default=lambda self: self.env['ir.sequence'].next_by_code('human.customer') or '/'
    )

    customer_level = fields.Selection([
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('platinum', 'Platinum')
    ], string='Level', default='bronze')
    
    total_sales = fields.Float(string='Total Sales ($)', digits='Product Price', default=0.0)
    
    joining_date = fields.Date(string='Joining Date', default=fields.Date.today())
    
    is_active_customer = fields.Boolean(string='Active Customer', default=True)