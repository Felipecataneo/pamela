from django.contrib import admin
from .models import *

class PacienteAdmin(admin.ModelAdmin):
    # fields = ('nome','uniqueId','slug','date_created','last_updated')

    search_fields = ['nome']


admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Image)
