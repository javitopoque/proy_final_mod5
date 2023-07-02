from django.contrib import admin
from .models import Ambiente
from .models import Inquilino
from .models import Servicio
from .models import AmbienteInquilino
from .models import ServicioAmbiente

# Register your models here.
admin.site.register(Ambiente)

admin.site.register(Servicio)
admin.site.register(AmbienteInquilino)
admin.site.register(ServicioAmbiente)

"""
Inquilino
"""

class InquilinoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "ciudad", "ci")
    ordering = ["apellido"]
    search_fields = ["nombre"]
    list_filter = ["ciudad"]
admin.site.register(Inquilino, InquilinoAdmin)
