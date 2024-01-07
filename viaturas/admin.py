from django.contrib import admin
from .models import Viatura, Armamento, Municao, ConsumoMun, Alteracao

admin.site.register(Viatura)
admin.site.register(Armamento)
admin.site.register(Municao)
admin.site.register(ConsumoMun)
admin.site.register(Alteracao)

