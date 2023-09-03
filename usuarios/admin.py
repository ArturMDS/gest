from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


campos = list(UserAdmin.fieldsets)
campos.append(
    ('Outros', {'fields': ('acesso', 'numero')})
)
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Usuario, UserAdmin)


