from django.contrib import admin
from .models import Server, AnsibleRole

admin.site.register(Server)
admin.site.register(AnsibleRole)
