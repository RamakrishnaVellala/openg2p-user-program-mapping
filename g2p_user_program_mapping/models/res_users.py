from odoo import models, tools
class ResUsers(models.Model):
    _inherit = "res.users"

class G2PProgram(models.Model):
    _inherit = ["g2p.program"]



