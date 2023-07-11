from odoo import models, fields, api


class Appointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference")
    prescription = fields.Html(string='prescription')





    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

