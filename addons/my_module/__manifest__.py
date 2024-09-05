{
    'name': 'My Module',
    'version': '1.0',
    'summary': 'Short summary of module\'s purpose',
    'description': 'Long description of module\'s purpose',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',  # 确保这一行存在
    ],
    'application': True,
}
