from django.contrib import admin

# Register your models here.
from aplicacion_5.models import registroClientes

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'email', 'ciudad')


admin.site.register(registroClientes, UsuariosAdmin)