from email.policy import default
from odoo import models, fields

class Liqtax(models.Model):
    _name = "mcliqtax"

    name = fields.Char("Codigo", required=True)
    description = fields.Char("Descripción")
    status = fields.Boolean("Activo", default=True)