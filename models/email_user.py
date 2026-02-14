from odoo import models, fields, api #error 1: tengo que importar la api

class EmailUser(models.Model):
    _name = "email.user"
    _description = "Usuario de correo electrónico"

    name = fields.Char(string="Nombre completo", required=True)
    email = fields.Char(string="Dirección de correo", required=True)
    password = fields.Char(string="Contraseña", required=True)
    quota = fields.Integer(string="Cuota (MB)", default=1024)
    active = fields.Boolean(string="Activo", default=True)

    #Ejercicio añadido para campo calculado
    quota_gb = fields.Float(string="Quota GB", compute="_calcular_quotaGB", store=True)
     #error 2: tenia puesto {store="true"} cuando es sin comillas porque eso era para los booleanos


    domain = fields.Char(string="Dominio", default="midominio.com")
    forwarding = fields.Char(string="Reenvío a")
    notes = fields.Text(string="Notas")

    @api.depends("quota")
    def _calcular_quotaGB(self): #error 3: tenia unida esta linea 
        for registro in self:
            registro.quota_gb = registro.quota/1024
