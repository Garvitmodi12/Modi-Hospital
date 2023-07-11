from odoo import models, fields, api
from datetime import date


class Hospital(models.Model):
    _name = "hospital.patient"
    _description = "Hospital"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "ref"

    name = fields.Char(string="NAME", tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    ref = fields.Char(string="Reference")
    age = fields.Char(string="AGE",  tracking=True)
    photo = fields.Binary(string='Image')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender',
                              tracking=True)
    student_blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve')])
    active = fields.Boolean(string='Active', default=True)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')


    # @api . depends('date of birth')
    # def _compute_age(self):
    #     for rec in self :
    #         today = date.today()
    #         if rec.date_of_birth:
    #             rec.age = today.year - rec.date_of_birth.year
    #         else:
    #             rec.age = 1

