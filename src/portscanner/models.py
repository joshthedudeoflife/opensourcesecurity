from django.db import models

# Create your models here.
class Portscanner(models.Model):
	ip_address = models.GenericIPAddressField(blank=False)
	port_number = models.DecimalField(max_digits=19, decimal_places=10)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)

	def __unicode__(self):
		return str(self.ip_address)
		#figure out what to run next