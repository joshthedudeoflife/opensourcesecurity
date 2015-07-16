from django.contrib import admin

# Register your models here.
#after adding a model add it here
from .models import Portscanner

class PortscannerAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "port_number", "timestamp"]
	class Meta:
		model = Portscanner

admin.site.register(Portscanner, PortscannerAdmin)