from email.policy import default
import re
from odoo import models, fields

class Liqtax(models.Model):
    _name = "mcliqtax"

    name = fields.Char("Codigo", required=True)
    description = fields.Char("Descripción", required=True)
    status = fields.Boolean("Activo", default=True)