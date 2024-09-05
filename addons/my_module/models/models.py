from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my_module.my_model'  # 模型的技术名称
    _description = 'My Model'  # 模型的人类可读描述

    # 字段定义
    name = fields.Char(string='Name', required=True)  # 名称字段，必填
    description = fields.Text(string='Description')  # 描述字段，文本类型
    date = fields.Date(string='Date')  # 日期字段
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='Status', default='draft')  # 状态字段，选择类型，默认为草稿状态

    # 确认动作方法
    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'  # 将状态更改为已确认

    # 完成动作方法
    def action_done(self):
        for record in self:
            record.state = 'done'  # 将状态更改为已完成
