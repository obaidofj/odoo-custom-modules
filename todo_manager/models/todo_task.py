 
from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    is_done = fields.Boolean(string='Done', default=False)