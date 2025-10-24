# -*- coding: utf-8 -*-
{
    'name': "Human Management System",
    'summary': "Module quản lý các thực thể Người (Human, Superhuman, Customer).",
    'description': """
        Module này định nghĩa các model cơ bản:
        - Human: Model cơ sở.
        - Superhuman: Kế thừa (Inheritance) từ Human.
        - Customer: Kế thừa Ủy quyền (Delegation Inheritance) từ Human.
    """,
    'author': "Your Name",
    'website': "http://www.yourwebsite.com",

    # Thông tin cơ bản
    'category': 'Management',
    'version': '1.0', 

    # Các module phụ thuộc (chỉ cần 'base')
    'depends': ['base'],

    # Dữ liệu sẽ được tải theo thứ tự: Security, Views, Menu
    'data': [
        # 1. Security: Cần tải trước để các model có thể truy cập được
        'security/ir.model.access.csv', 
        
        # 2. Views: Tải các định nghĩa giao diện
        'views/human_view.xml',        # Views cho human.human
        'views/superhuman_views.xml',   # Views cho human.superhuman
        'views/customer_view.xml',     # Views cho human.customer (Bao gồm cả sequence)
        
        # 3. Menu: Tải cuối cùng để các menu item trỏ đúng đến các action đã định nghĩa
        'views/menu.xml',               
    ],

    'installable': True,
    'application': True, # Hiển thị module trong danh sách Apps
    'auto_install': False,
    'license': 'LGPL-3',
}